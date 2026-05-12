import pandas as pd

# =========================
# EXTRACT
# =========================

# leitura do dataset
df = pd.read_csv('nyc_flights.csv', sep=',')

# =========================
# TRANSFORM
# =========================

# remoção de voos sem informação de atraso
df = df.dropna(subset=['dep_delay', 'arr_delay'])

# criação de variável binária indicando atraso na chegada
df['is_delay'] = df['arr_delay'].apply(lambda x: 1 if x > 0 else 0)

# criação de coluna de data
df['date'] = pd.to_datetime(df[['year', 'month', 'day']])

# função para categorização do período do dia
def periodo(h):
    if pd.isna(h):
        return 'Desconhecido'
    elif 5 <= h < 12:
        return 'Manhã'
    elif 12 <= h < 18:
        return 'Tarde'
    else:
        return 'Noite'

# conversão da hora
def converter_hora(x):
    if pd.isna(x):
        return None
    return int(x / 100)

# criação da variável período do dia
df['periodo_dia'] = df['dep_time'].apply(converter_hora).apply(periodo)
    
# =========================
# LOAD
# =========================

# exportação do dataset tratado
df.to_csv('nyc_flights_tratado.csv', index=False)

print('ETL OK')
