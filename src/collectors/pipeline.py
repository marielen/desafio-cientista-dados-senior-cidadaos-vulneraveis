from pathlib import Path

import pandas as pd

from src.collectors.bigquery import ChamadosCollector, DadosMestresCollector
from src.collectors.holidays import PublicHolidayCollector
from src.collectors.openmeteo import OpenMeteoCollector

# Raiz do projeto: pasta que contém o pyproject.toml
PROJECT_ROOT = Path(__file__).resolve().parents[2]
DATA_RAW = PROJECT_ROOT / "data" / "raw"


class DataPipeline:
    """
    Orquestra a coleta de todas as fontes de dados do projeto.

    Exemplo de uso:
        pipeline = DataPipeline(
            billing_project_id="meu-projeto-gcp",
            start_date="2023-01-01",
            end_date="2024-12-31",
        )
        dados = pipeline.run()
    """

    TABELAS_MESTRES = [
        "bairro",
        "area_planejamento",
        "regiao_administrativa",
        "subprefeitura",
    ]

    def __init__(
        self,
        billing_project_id: str,
        start_date: str,
        end_date: str,
    ):
        self.billing_project_id = billing_project_id
        self.start_date = start_date
        self.end_date = end_date
        self.anos = list(range(int(start_date[:4]), int(end_date[:4]) + 1))

    def run(self) -> dict[str, pd.DataFrame]:
        """
        Executa a coleta de todas as fontes e retorna um dicionário
        com os DataFrames organizados por nome.
        """
        dados = {}

        print("=== Coletando chamados do 1746 ===")
        dados["chamados"] = ChamadosCollector(
            billing_project_id=self.billing_project_id,
            start_date=self.start_date,
            end_date=self.end_date,
            output_path=DATA_RAW / "chamados.parquet",
        ).fetch()

        print("\n=== Coletando dados mestres ===")
        for tabela in self.TABELAS_MESTRES:
            dados[tabela] = DadosMestresCollector(
                billing_project_id=self.billing_project_id,
                table_name=tabela,
                output_path=DATA_RAW / f"{tabela}.parquet",
            ).fetch()

        print("\n=== Coletando dados climáticos ===")
        dados["clima"] = OpenMeteoCollector(
            start_date=self.start_date,
            end_date=self.end_date,
            output_path=DATA_RAW / "clima.parquet",
        ).fetch()

        print("\n=== Coletando feriados ===")
        dados["feriados"] = PublicHolidayCollector(
            anos=self.anos,
            output_path=DATA_RAW / "feriados.parquet",
        ).fetch()

        print("\n=== Coleta concluída ===")
        for nome, df in dados.items():
            print(f"  {nome}: {len(df):,} linhas")

        return dados
