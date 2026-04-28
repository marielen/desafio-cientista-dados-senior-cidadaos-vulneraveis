from pathlib import Path

import pandas as pd
import requests

from src.collectors.base import DataCollector


class PublicHolidayCollector(DataCollector):
    """
    Coleta feriados nacionais brasileiros via Public Holiday API.

    Documentação: https://date.nager.at/Api
    """

    BASE_URL = "https://date.nager.at/api/v3/PublicHolidays"
    PAIS = "BR"

    def __init__(
        self,
        anos: list[int],
        output_path: str | Path = "data/raw/feriados.parquet",
    ):
        super().__init__(output_path)
        self.anos = anos

    def _fetch_data(self) -> pd.DataFrame:
        frames = []

        for ano in self.anos:
            url = f"{self.BASE_URL}/{ano}/{self.PAIS}"
            response = requests.get(url, timeout=30)
            response.raise_for_status()

            data = response.json()

            if not data:
                raise ValueError(f"Nenhum feriado retornado para o ano {ano}.")

            frames.append(pd.DataFrame(data))

        df = pd.concat(frames, ignore_index=True)
        df["date"] = pd.to_datetime(df["date"])
        df = df.rename(columns={"date": "data", "localName": "nome"})
        df = df[["data", "nome"]]

        return df
