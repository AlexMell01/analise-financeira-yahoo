import pandas as pd
import matplotlib.pyplot as plt
arquivo = "archive/yahoo_data.xlsx"
df = pd.read_excel (arquivo)
print("Primeiras linhas da Planilha:")
print(df.head())
print("\nColunas disponíveis:")
print(df.columns)
print(df.info())
print(df.describe())

df['Date'] = pd.to_datetime(df['Date'])
df = df.sort_values(by= 'Date')
print("\nData após conversão e ordenação")
print(df.head())

plt.figure(figsize=(12,6))
plt.plot(df['Date'], df['Adj Close**'], label ='Preço de Fechamento Ajustado')

plt.title('Evolução do Preço de Fechamento Ajustado')
plt.xlabel('Data')
plt.ylabel('Preço')
plt.legend()
plt.grid(True)
plt.savefig('grafico_1.png')

plt.figure(figsize=(14,7))

plt.plot(df['Date'], df['Open'], label ='Abertura (Open)', alpha= 0.7)
plt.plot(df['Date'], df['High'], label= 'Maximo (High)', alpha= 0.7)
plt.plot(df['Date'], df['Low'], label = 'Mínimo (Low)', alpha= 0.7)
plt.plot(df['Date'], df['Close*'], label='Fechamento (Close)', alpha= 0.7)

plt.title('Preços Open, High, Low e Close ao Longo do Tempo ')
plt.xlabel('Data')
plt.ylabel('Preço')
plt.legend()
plt.grid(True)

plt.savefig("grafico_2.png")

plt.figure(figsize=(14, 5))  

plt.bar(df['Date'], df['Volume'], color='purple', alpha=0.6)

plt.title('Volume de Negociações ao Longo do Tempo')
plt.xlabel('Data')
plt.ylabel('Volume')
plt.grid(True, axis='y')  

plt.savefig('grafico_3.png')

df['SMA_20'] = df['Adj Close**'].rolling(window=20).mean()
plt.figure(figsize=(12, 6))
plt.plot(df['Date'], df['Close*'], label='Preço de Fechamento')
plt.plot(df['Date'], df['SMA_20'], label='Média Móvel 20 dias', linestyle='--')
plt.title('Preço de Fechamento e Média Móvel de 20 dias')
plt.xlabel('Data')
plt.ylabel('Preço')
plt.legend()
plt.grid(True)
plt.savefig('grafico_4.png')


df['MA7'] = df['Close*'].rolling(window=7).mean()
df['MA30'] = df['Close*'].rolling(window=30).mean()
plt.figure(figsize=(12, 6))
plt.plot(df['Date'], df['Close*'], label='Preço de Fechamento')
plt.plot(df['Date'], df['MA7'], label='Média Móvel 7 dias', linestyle='--')
plt.plot(df['Date'], df['MA30'], label='Média Móvel 30 dias', linestyle='--')
plt.title('Preço de Fechamento com Médias Móveis de 7 e 30 dias')
plt.xlabel('Data')
plt.ylabel('Preço')
plt.legend()
plt.grid(True)
plt.savefig('grafico_5.png')

print("\nEstatísticas do Preço de Fechamento:")
print(df['Close*'].describe())




