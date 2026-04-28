# Desafio Técnico - Cientista de Dados Sênior
## Programa Pequenos Cariocas (PIC)

---

## Contexto

O **Programa Pequenos Cariocas** é uma iniciativa intersetorial da Prefeitura do Rio de Janeiro que acompanha crianças de 0 a 6 anos e gestantes em situação de vulnerabilidade, integrando dados de Saúde, Educação e Assistência Social.

Como Cientista de Dados no PIC, você trabalhará com dados complexos de múltiplas fontes, construindo modelos preditivos para antecipar riscos e priorizar intervenções com recursos limitados.

Este desafio usa **dados públicos do 1746** para avaliar suas habilidades em análise exploratória, feature engineering, modelagem preditiva e geração de insights acionáveis para gestão pública.

---

## Instruções

1. Crie um **fork público desse repositório** com suas respostas
2. Use **Jupyter Notebooks** (.ipynb) bem documentados
3. Inclua **README.md** explicando abordagem e como reproduzir


---

## Dados

### Tabela Principal
**`datario.adm_central_atendimento_1746.chamado`** (14M+ registros, 2015-2024)

### Tabelas Auxiliares
- `datario.dados_mestres.bairro`
- `datario.dados_mestres.area_planejamento`
- `datario.dados_mestres.regiao_administrativa`
- `datario.dados_mestres.subprefeitura`

### APIs Externas
- [Public Holiday API](https://date.nager.at/Api)
- [Open-Meteo Historical Weather API](https://open-meteo.com/)

**⚠️ IMPORTANTE**: A tabela tem 14M+ linhas. Use sempre **filtros de partição**: `WHERE data_particao >= '2023-01-01'`

---

## Parte 1: Análise Exploratória com APIs Externas

**Use as APIs públicas e análise geoespacial para responder às questões 1-4:**

### 1. Clima e Demanda de Serviços

Usando a **Open-Meteo API**, investigue a relação entre condições climáticas (temperatura, precipitação) e o volume de chamados do 1746 no Rio de Janeiro no período 2023-2024.

**Entregue**: Análise de correlação entre variáveis climáticas e diferentes tipos de chamados, com interpretação sobre quais categorias são mais sensíveis ao clima.

### 2. Padrões Geoespaciais de Demanda

Analise a distribuição geoespacial dos chamados do 1746 no Rio de Janeiro (2023-2024). Explore padrões territoriais: há concentração em determinadas regiões? Categorias de chamados variam por território?

**Entregue**: Análise geoespacial com visualizações (mapas, heatmaps), identificação de clusters territoriais e insights sobre desigualdades ou padrões de demanda por região administrativa, bairro ou área de planejamento.

### 3. Eventos Extremos e Feriados

Investigue como **eventos climáticos extremos** e **feriados** (use Public Holiday API) impactam o volume e padrão de chamados no período 2023-2024.

**Entregue**: Análise comparativa entre dias normais, feriados e eventos extremos (defina seus critérios), incluindo tipos de chamados mais afetados, distribuição territorial e interpretação dos padrões observados.

### 4. Previsão de Demanda Multidimensional

Construa um modelo de regressão para prever o volume diário de chamados usando features **climáticas** (temperatura, precipitação), **temporais** (dia da semana, feriados) e **geoespaciais** (região, bairro).

**Entregue**: Dataset agregado, modelo treinado (treino: 2023, teste: 2024), métricas de performance e análise de feature importance. Quais dimensões (clima, tempo, território) são mais relevantes para predição?

---

## Parte 2: Modelagem Preditiva - Resolução de Chamados

**Objetivo**: Prever se um chamado será resolvido em até 7 dias.

### 5. Feature Engineering

Crie um dataset de **50.000 chamados do período 2023-2024** (amostra aleatória) para prever se um chamado será resolvido em até 7 dias.

Construa features que capturem aspectos **temporais** (dia, hora, feriado), **climáticos** (temperatura, chuva via API), **geoespaciais** (região administrativa, bairro, coordenadas), **categóricos** (tipo de chamado) e **contextuais** (reclamações).

**Entregue**: Dataset processado, documentação das transformações aplicadas (tratamento de missings, encoding, normalização) e justificativa das escolhas de feature engineering.

### 6. Modelagem Baseline

Treine um modelo baseline de **Logistic Regression** para classificar se um chamado será resolvido em até 7 dias.

**Entregue**: Modelo treinado (treino: 2023, teste: 2024), métricas de performance (precision, recall, F1, AUC-ROC) e justificativa sobre qual métrica você priorizaria no contexto de gestão pública e por quê.

### 7. Modelos Avançados e Tuning

Treine **pelo menos 2 algoritmos** além do baseline (ex: Random Forest, XGBoost, LightGBM) e faça tuning de hiperparâmetros em ao menos um deles.

**Entregue**: Comparação de performance entre modelos, curvas ROC e Precision-Recall do melhor modelo, e análise sobre qual algoritmo você recomendaria para produção.

### 8. Interpretabilidade

Analise a interpretabilidade do melhor modelo usando SHAP ou feature importance nativa.

**Entregue**: Top 10 features mais importantes com interpretação (incluindo relevância de variáveis climáticas e geoespaciais), análise de erros por dimensão (temporal, territorial, categórica) e insights sobre o que o modelo aprendeu que pode informar decisões de gestão.

---

## Parte 3: Sistema de Priorização

### 9. Score de Prioridade

O órgão tem capacidade para dar atenção especial a apenas **20% dos chamados**. Crie um score de priorização que combine a probabilidade do modelo com outras dimensões relevantes (urgência, impacto, contexto climático, equidade territorial).

**Entregue**: Fórmula do score proposto com justificativa dos pesos e critérios escolhidos. Como você equilibraria eficiência (priorizar chamados com maior risco de atraso) e equidade (não negligenciar regiões vulneráveis)?

### 10. Simulação e Impacto

Simule no conjunto de teste duas estratégias de priorização: seleção aleatória de 20% dos chamados vs. top 20% pelo seu score. Compare a efetividade de cada abordagem.

**Entregue**: Métricas comparativas (precision, recall nos chamados priorizados), visualização de lift curve e recomendação fundamentada sobre qual estratégia implementar, quantificando o ganho esperado.

---

## Avaliação

Você será avaliado em cada uma das categorias abaixo, com seus respectivos pesos:

- **SQL e Manipulação de Dados**: peso 1
- **Modelagem e Python**: peso 2
- **Visualização e Comunicação**: peso 1

Uma média ponderada será calculada e os melhores candidatos serão chamados para a etapa de entrevistas.

**Dica**: procure fazer algo diferente! Devido à grande quantidade de candidatos, é possível que uma boa média não seja suficiente para te garantir uma entrevista. Tente se destacar!

---

## Estrutura Sugerida do Repositório

```
desafio-pic-ds/
├── README.md
├── notebooks/
│   ├── 01_analise_apis_clima.ipynb
│   ├── 02_modelagem_resolucao.ipynb
│   └── 03_sistema_priorizacao.ipynb
├── data/                    # (não commitar arquivos grandes)
│   └── .gitkeep
├── results/
│   └── figures/
└── requirements.txt
```

---

## FAQ

**1. Como economizar cota do BigQuery?**
- Use sempre `WHERE data_particao >= 'YYYY-MM-DD'`
- Teste queries com `LIMIT 100` antes de rodar completo
- Salve resultados intermediários como CSV

**2. Posso usar bibliotecas específicas?**
Sim! Sugestões: pandas, scikit-learn, xgboost, lightgbm, shap, requests, matplotlib, seaborn, plotly, geopandas, folium, kepler.gl.

**3. Preciso fazer todas as perguntas?**
Sim, mas profundidade importa mais que completude. Melhor fazer menos com excelência.

**4. Como obter dados das APIs?**
- Public Holiday API: `requests.get('https://date.nager.at/api/v3/PublicHolidays/2023/BR')` (também para 2024)
- Open-Meteo: Ver documentação em https://open-meteo.com/en/docs

---

## Contato

Dúvidas? Envie um email para **selecao.pcrj@gmail.com**

Boa sorte! 🚀