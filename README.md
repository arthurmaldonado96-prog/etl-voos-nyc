## Objetivo

Este projeto tem como objetivo analisar padrões de atrasos em voos, identificando fatores que impactam a pontualidade e a eficiência operacional.

---

## Dataset

O projeto utiliza o dataset **NYC Flights 2013**, contendo informações sobre voos, atrasos, companhias aéreas e aeroportos.

---

## Tecnologias Utilizadas

* Python (Pandas)
* Power BI

---

## Pipeline de Dados (ETL)

O projeto segue as etapas:

1. **Extract** → leitura do dataset
2. **Transform** → limpeza, tratamento e criação de variáveis
3. **Load** → exportação para análise e visualização

---

## Principais Transformações

* Remoção de valores nulos
* Criação da variável `is_delay`
* Criação da variável `periodo_dia`
* Construção de coluna de data

---

## Dashboard

O dashboard foi desenvolvido no Power BI e contém:

### 🔹 Análise Geral

* Total de voos
* Percentual de atrasos
* Atraso médio

### 🔹 Análise Operacional

* Atraso médio por companhia aérea
* Atraso médio por aeroporto de origem

### 🔹 Análise Temporal

* Atraso médio por dia da semana
* Quantidade de atrasos ao longo do ano

---

## Principais Insights

* Voos no período noturno apresentam maior atraso médio
* Determinadas companhias possuem maior atraso que outras
* Existe um padrão temporal nos atrasos ao longo do ano

---

## Possíveis Melhorias

* Implementar modelo de Machine Learning para previsão de atrasos
* Automatizar pipeline ETL
* Criar API para consumo dos dados

---

## Autor

Arthur M
