import pandas as pd

# 1. Carregar o arquivo CSV
df = pd.read_csv('mais_ouvidas_2024.csv')

# Verificar se o carregamento foi bem-sucedido
print(df.head())
print(df.info())

# 2. Identificar e converter colunas numéricas
# As colunas a serem convertidas
numeric_cols = [
    'Spotify Streams', 'YouTube Views', 'TikTok Views', 'Pandora Streams', 
    'Soundcloud Streams', 'Spotify Popularity', 'YouTube Views', 
    'TikTok Likes', 'Shazam Counts'
]

# Substituir caracteres indesejados (como vírgulas) e converter para numérico
for col in numeric_cols:
    if col in df.columns:
        df[col] = df[col].replace({'\,': ''}, regex=True).astype(float)

# 3. Corrigir o formato da coluna 'Release Date'
df['Release Date'] = pd.to_datetime(df['Release Date'], errors='coerce')

# 4. Criar novas colunas
df['Streaming Popularity'] = df[['Spotify Popularity', 'YouTube Views', 'TikTok Likes', 'Shazam Counts']].mean(axis=1)
df['Total Streams'] = df[['Spotify Streams', 'YouTube Views', 'TikTok Views', 'Pandora Streams', 'Soundcloud Streams']].sum(axis=1)

# 5. Filtrar faixas
filtered_df = df[(df['Spotify Popularity'] > 80) & (df['Total Streams'] > 1_000_000)]

# 6. Salvar o DataFrame resultante em um novo arquivo JSON
filtered_df.to_json('faixas_filtradas.json', orient='records', lines=True)

# Verificar se o arquivo foi salvo corretamente
import os
print(f"Arquivo salvo em: {os.path.abspath('faixas_filtradas.json')}")