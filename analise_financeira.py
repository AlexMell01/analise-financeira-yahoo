import pandas as pd
import matplotlib.pyplot as plt

# Caminho do arquivo
arquivo = "archive/yahoo_data.xlsx"

# Leitura do Excel
df = pd.read_excel(arquivo)

# Exibe as 5 primeiras linhas
print("Primeiras linhas da planilha:")
print(df.head())

# Verifica colunas disponíveis
print("\nColunas disponíveis:")
print(df.columns)

# Exibe informações gerais sobre o DataFrame (colunas, tipos, valores nulos)
print(df.info())

# Estatísticas descritivas das colunas numéricas (média, desvio, mínimo, máximo, quartis, etc)
print(df.describe())

# Converter a coluna Date para datetime
df['Date'] = pd.to_datetime(df['Date'])

# Ordenar o DataFrame pela data (do mais antigo para o mais recente)
df = df.sort_values(by='Date')

print("\nData após conversão e ordenação:")
print(df.head())

# Plotar gráfico de linha do preço de fechamento ajustado ao longo do tempo
plt.figure(figsize=(12, 6))  # Tamanho do gráfico
plt.plot(df['Date'], df['Adj Close**'], label='Preço Fechamento Ajustado')
plt.title('Evolução do Preço de Fechamento Ajustado')
plt.xlabel('Data')
plt.ylabel('Preço')
plt.legend()
plt.grid(True)
plt.savefig('grafico_1.png')  # ✅ Salvando o primeiro gráfico
# plt.show()

# Gráfico com Open, High, Low, Close
plt.figure(figsize=(14, 7))
plt.plot(df['Date'], df['Open'], label='Abertura (Open)', alpha=0.7)
plt.plot(df['Date'], df['High'], label='Máximo (High)', alpha=0.7)
plt.plot(df['Date'], df['Low'], label='Mínimo (Low)', alpha=0.7)
plt.plot(df['Date'], df['Close*'], label='Fechamento (Close)', alpha=0.7)
plt.title('Preços Open, High, Low e Close ao Longo do Tempo')
plt.xlabel('Data')
plt.ylabel('Preço')
plt.legend()
plt.grid(True)
plt.savefig('grafico_2.png')  # ✅ Salvando o segundo gráfico
# plt.show()

# Gráfico de Volume
plt.figure(figsize=(14, 5))
plt.bar(df['Date'], df['Volume'], color='purple', alpha=0.6)
plt.title('Volume de Negociações ao Longo do Tempo')
plt.xlabel('Data')
plt.ylabel('Volume')
plt.grid(True, axis='y')
plt.savefig('grafico_3.png')  # ✅ Salvando o terceiro gráfico
# plt.show()

# Média móvel simples de 20 dias
df['SMA_20'] = df['Adj Close**'].rolling(window=20).mean()

plt.figure(figsize=(12,6))
plt.plot(df['Date'], df['Close*'], label='Preço de Fechamento')
plt.title('Preço de Fechamento ao Longo do Tempo')
plt.xlabel('Data')
plt.ylabel('Preço de Fechamento')
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()
plt.savefig('grafico_4.png')  # ✅ Salvando o quarto gráfico
# plt.show()

# Cálculo de médias móveis de 7 e 30 dias
df['Date'] = pd.to_datetime(df['Date'])
print(df.isnull().sum())

df['MA7'] = df['Close*'].rolling(window=7).mean()
df['MA30'] = df['Close*'].rolling(window=30).mean()

plt.figure(figsize=(12,6))
plt.plot(df['Date'], df['Close*'], label='Preço de Fechamento')
plt.plot(df['Date'], df['MA7'], label='Média Móvel 7 dias')
plt.plot(df['Date'], df['MA30'], label='Média Móvel 30 dias')
plt.title('Preço de Fechamento com Médias Móveis')
plt.xlabel('Data')
plt.ylabel('Preço')
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()
plt.savefig('grafico_5.png')  # ✅ Salvando o quinto gráfico
# plt.show()

print(df['Close*'].describe())