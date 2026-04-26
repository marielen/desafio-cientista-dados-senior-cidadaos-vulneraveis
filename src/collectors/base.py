from abc import ABC, abstractmethod
from pathlib import Path

import pandas as pd


class DataCollector(ABC):
    """
    Classe base abstrata para todos os coletores de dados do projeto.

    O fluxo padrão é: se o parquet local já existe, carrega direto;
    se não, busca da fonte, salva e retorna.
    """

    def __init__(self, output_path: str | Path):
        self.output_path = Path(output_path)
        self.output_path.parent.mkdir(parents=True, exist_ok=True)

    @abstractmethod
    def _fetch_data(self) -> pd.DataFrame:
        """Busca os dados na fonte. Implementado por cada subclasse."""
        pass

    def fetch(self) -> pd.DataFrame:
        """
        Retorna os dados. Carrega do parquet local se existir;
        caso contrário, busca da fonte e salva automaticamente.
        """
        if self.output_path.exists():
            print(f"[{self.__class__.__name__}] Carregando de {self.output_path}")
            return self.load()

        print(f"[{self.__class__.__name__}] Buscando da fonte...")
        df = self._fetch_data()
        self._save(df)
        return df

    def _save(self, df: pd.DataFrame) -> None:
        """Persiste o DataFrame em parquet."""
        df.to_parquet(self.output_path, index=False)
        print(f"[{self.__class__.__name__}] Salvo em {self.output_path} ({len(df):,} linhas)")

    def load(self) -> pd.DataFrame:
        """Carrega o parquet local."""
        return pd.read_parquet(self.output_path)
