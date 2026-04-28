"""
Execute este script uma vez após clonar o repositório e rodar `poetry install`.
Ele registra a raiz do projeto no ambiente virtual para que os imports
funcionem nos notebooks sem configuração adicional de path.

Uso:
    poetry run python setup_dev.py
"""
import site
import sys
from pathlib import Path

project_root = Path(__file__).resolve().parent
pth_filename = "desafio-pic-ds.pth"

site_packages = site.getsitepackages()
if not site_packages:
    print("Erro: não foi possível encontrar o diretório site-packages.")
    sys.exit(1)

pth_path = Path(site_packages[0]) / pth_filename

pth_path.write_text(str(project_root) + "\n", encoding="utf-8")
print(f"Configurado com sucesso: {pth_path}")
print(f"Aponta para: {project_root}")
