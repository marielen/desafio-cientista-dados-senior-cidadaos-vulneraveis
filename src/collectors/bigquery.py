from pathlib import Path

import basedosdados as bd
import pandas as pd

from src.collectors.base import DataCollector


class ChamadosCollector(DataCollector):
    """
    Coleta os chamados do 1746 do BigQuery.

    Usa filtro de partição obrigatório para controlar o volume
    de dados lidos e evitar consumo desnecessário de cota.
    """

    TABLE = "datario.adm_central_atendimento_1746.chamado"

    def __init__(
        self,
        billing_project_id: str,
        start_date: str,
        end_date: str,
        output_path: str | Path = "data/raw/chamados.parquet",
    ):
        super().__init__(output_path)
        self.billing_project_id = billing_project_id
        self.start_date = start_date
        self.end_date = end_date

    def _fetch_data(self) -> pd.DataFrame:
        query = f"""
            SELECT *
            FROM `{self.TABLE}`
            WHERE data_particao >= '{self.start_date}'
              AND data_particao <= '{self.end_date}'
        """
        return bd.read_sql(query, billing_project_id=self.billing_project_id)


class DadosMestresCollector(DataCollector):
    """
    Coleta tabelas auxiliares de dados mestres do BigQuery.

    Parametrizada pelo nome da tabela, já que todas seguem
    o mesmo padrão de acesso sem filtros complexos.

    Tabelas disponíveis:
        - bairro
        - area_planejamento
        - regiao_administrativa
        - subprefeitura
    """

    DATASET = "datario.dados_mestres"
    TABELAS_VALIDAS = {
        "bairro",
        "area_planejamento",
        "regiao_administrativa",
        "subprefeitura",
    }

    def __init__(
        self,
        billing_project_id: str,
        table_name: str,
        output_path: str | Path | None = None,
    ):
        if table_name not in self.TABELAS_VALIDAS:
            raise ValueError(
                f"Tabela '{table_name}' inválida. "
                f"Opções: {self.TABELAS_VALIDAS}"
            )
        self.billing_project_id = billing_project_id
        self.table_name = table_name

        if output_path is None:
            output_path = f"data/raw/{table_name}.parquet"

        super().__init__(output_path)

    def _fetch_data(self) -> pd.DataFrame:
        query = f"SELECT * FROM `{self.DATASET}.{self.table_name}`"
        return bd.read_sql(query, billing_project_id=self.billing_project_id)
