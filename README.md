# Desafio Técnico — Cientista de Dados Sênior
## Programa Pequenos Cariocas (Prefeitura do Rio de Janeiro)

---

## Escopo entregue

O desafio propõe dez questões distribuídas em três partes. Dada a janela de tempo disponível, priorizei profundidade em vez de cobertura e entreguei as questões 1 e 2 da Parte 1 (Clima e Demanda; Padrões Geoespaciais), que são as que mais se conectam diretamente ao contexto do Programa Pequenos Cariocas: entender onde a demanda se concentra e o que a modula.

---

## Principais resultados

**Clima e demanda de serviços.** Dias mais quentes no Rio geram mais chamados ao 1746, com efeito mais pronunciado nos chamados de "Serviço", que concentra demandas operacionais urbanas. A chuva, ao contrário do que se poderia esperar, não explica o aumento de demanda: a correlação com precipitação é praticamente zero. Isso tem implicação direta para planejamento operacional: ondas de calor são um sinal previsível de pressão sobre a rede de serviços, e a prefeitura pode se antecipar reforçando equipes nos dias de maior temperatura prevista.

**Distribuição territorial da demanda.** A demanda não se distribui igualmente pela cidade, e o tipo de problema que os moradores reportam também varia por território. Comunidades como Complexo da Maré, Complexo do Alemão, Jacarezinho e Cidade de Deus apresentam proporção mais alta de chamados classificados como críticos em relação à média da cidade. A Rocinha se destaca como caso isolado, com a maior proporção de chamados críticos de todo o conjunto analisado. Esse padrão sugere que uma política de atendimento baseada apenas em volume absoluto de chamados tende a subatender territórios que já partem de condições de serviço piores. Para uma análise técnica detalhada com mapas, correlações e metodologia, consulte o `parte_1.ipynb`.

---

## Fluxo de trabalho

Antes de responder qualquer pergunta, investi tempo em construir uma base de dados confiável e reproduzível. O ponto de partida foi o módulo `src/collectors/`, que encapsula a coleta de cada fonte em uma classe separada: BigQuery para os chamados e tabelas mestres, Open-Meteo para os dados climáticos e Public Holiday API para os feriados. O `DataPipeline` em `pipeline.py` orquestra tudo em uma única chamada e implementa cache local: se o Parquet já existe em `data/raw/`, a coleta é pulada, evitando custo de BigQuery e chamadas repetidas às APIs.

Com os dados disponíveis localmente, o `parte_0.ipynb` serviu para entender o que estava sendo trabalhado antes de formular qualquer hipótese: volume e período dos chamados, qualidade dos dados, distribuições, cobertura geográfica e variáveis disponíveis. Só depois disso o `parte_1.ipynb` foi desenvolvido para responder as questões de análise.

---

## Estrutura do repositório

```
desafio-cientista-dados-senior-cidadaos-vulneraveis/
├── notebooks/
│   ├── parte_0.ipynb
│   └── parte_1.ipynb
├── src/
│   └── collectors/
│       ├── base.py
│       ├── bigquery.py
│       ├── openmeteo.py
│       ├── holidays.py
│       └── pipeline.py
├── data/
│   └── raw/
├── results/
│   └── figures/
├── setup_dev.py
├── pyproject.toml
├── poetry.lock
└── requirements.txt
```

---

## Como reproduzir

**Pré-requisitos:** Python 3.11 e um projeto GCP com billing configurado (os dados do `datario` são públicos, mas o BigQuery cobra o processamento na conta de quem consulta).

**Instalação com Poetry (recomendado):**

```bash
pip install poetry
poetry install
poetry run python setup_dev.py
poetry run python -m ipykernel install --user --name desafio-pic
```

**Instalação com pip:**

```bash
pip install -r requirements.txt
python setup_dev.py
python -m ipykernel install --user --name desafio-pic
```

**Coleta dos dados:** execute `parte_0.ipynb` substituindo `billing_project_id` pelo ID do seu projeto GCP. Os dados são salvos em `data/raw/` como Parquet e reutilizados nas execuções seguintes.

**Análise:** com os dados em `data/raw/`, execute `parte_1.ipynb` em ordem. Nenhuma conexão externa é necessária nessa etapa.
