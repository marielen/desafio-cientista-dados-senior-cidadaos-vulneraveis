from pathlib import Path

import pandas as pd
import requests

from src.collectors.base import DataCollector

# Coordenadas do centro do Rio de Janeiro
RIO_LAT = -22.9068
RIO_LON = -43.1729

# Variáveis climáticas coletadas
VARIAVEIS_CLIMATICAS = [
    "temperature_2m_max",
    "temperature_2m_min",
    "temperature_2m_mean",
    "precipitation_sum",
    "wind_speed_10m_max",
]


class OpenMeteoCollector(DataCollector):
    """
    Coleta dados climáticos históricos diários do Rio de Janeiro
    via Open-Meteo Historical Weather API.

    Documentação: https://open-meteo.com/en/docs/historical-weather-api
    """

    BASE_URL = "https://archive-api.open-meteo.com/v1/archive"

    def __init__(
        self,
        start_date: str,
        end_date: str,
        latitude: float = RIO_LAT,
        longitude: float = RIO_LON,
        output_path: str | Path = "data/raw/clima.parquet",
    ):
        super().__init__(output_path)
        self.start_date = start_date
        self.end_date = end_date
        self.latitude = latitude
        self.longitude = longitude

    def _fetch_data(self) -> pd.DataFrame:
        params = {
            "latitude": self.latitude,
            "longitude": self.longitude,
            "start_date": self.start_date,
            "end_date": self.end_date,
            "daily": VARIAVEIS_CLIMATICAS,
            "timezone": "America/Sao_Paulo",
        }

        response = requests.get(self.BASE_URL, params=params, timeout=30)
        response.raise_for_status()

        data = response.json()

        if "daily" not in data:
            raise ValueError(
                f"Resposta inesperada da API: campo 'daily' ausente. "
                f"Resposta recebida: {data}"
            )

        df = pd.DataFrame(data["daily"])
        df["time"] = pd.to_datetime(df["time"])
        df = df.rename(columns={"time": "data"})

        return df
