import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Título do app
st.title('📊 Dashboard - Análise Financeira')

# Leitura dos dados
df = pd.read_excel('archive/yahoo_data.xlsx')

# Mostrar as primeiras linhas
st.subheader('Dados - Primeiras Linhas')
st.write(df.head())

st.subheader('Gráfico - Preço de Fechamento Ajustado')

fig, ax = plt.subplots (figsize=(10,5))
ax.plot(df['Date'], df['Adj Close**'], label='Adj Close')
ax.set_xlabel('Data')
ax.set_ylabel('Preço')
ax.set_title('Evolução dp preço de Fechamento Ajustado')
ax.legend()
ax.grid(True)
from matplotlib.dates import AutoDateLocator, AutoDateFormatter

locator = AutoDateLocator()
formatter = AutoDateFormatter(locator)

ax.xaxis.set_major_locator(locator)
ax.xaxis.set_major_formatter(formatter)
fig.autofmt_xdate()

st.pyplot(fig)

st.subheader('Gráfico - Open, High, Low e Close')

fig2, ax2 = plt.subplots(figsize=(10, 5))
ax2.plot(df['Date'], df['Open'], label='Open', alpha=0.7)
ax2.plot(df['Date'], df['High'], label='High', alpha=0.7)
ax2.plot(df['Date'], df['Low'], label='Low', alpha=0.7)
ax2.plot(df['Date'], df['Close*'], label='Close', alpha=0.7)

ax2.set_xlabel('Data')
ax2.set_ylabel('Preço')
ax2.set_title('Preços Open, High, Low e Close ao Longo do Tempo')
ax2.legend()
ax2.grid(True)
locator = AutoDateLocator()
formatter = AutoDateFormatter(locator)

ax2.xaxis.set_major_locator(locator)
ax2.xaxis.set_major_formatter(formatter)
fig2.autofmt_xdate()

st.pyplot(fig2)

st.subheader('Gráfico - Volume de Negociações')

fig3, ax3 = plt.subplots(figsize=(10, 5))
ax3.bar(df['Date'], df['Volume'], color='purple', alpha=0.6)
ax3.set_xlabel('Data')
ax3.set_ylabel('Volume')
ax3.set_title('Volume de Negociações ao Longo do Tempo')
ax3.grid(True, axis='y')

from matplotlib.dates import AutoDateLocator, AutoDateFormatter

locator = AutoDateLocator()
formatter = AutoDateFormatter(locator)

ax3.xaxis.set_major_locator(locator)
ax3.xaxis.set_major_formatter(formatter)
fig3.autofmt_xdate()  

st.pyplot(fig3)

st.subheader('Gráfico - Preço de Fechamento com Média Móvel de 20 dias')

# Calcula a média móvel de 20 dias
df['SMA_20'] = df['Adj Close**'].rolling(window=20).mean()

fig4, ax4 = plt.subplots(figsize=(10, 5))
ax4.plot(df['Date'], df['Close*'], label='Preço de Fechamento')
ax4.plot(df['Date'], df['SMA_20'], label='Média Móvel 20 dias', linestyle='--')

ax4.set_xlabel('Data')
ax4.set_ylabel('Preço')
ax4.set_title('Preço de Fechamento com Média Móvel de 20 dias')
ax4.legend()
ax4.grid(True)

# Ajusta as datas no eixo X
locator = AutoDateLocator()
formatter = AutoDateFormatter(locator)
ax4.xaxis.set_major_locator(locator)
ax4.xaxis.set_major_formatter(formatter)
fig4.autofmt_xdate()

st.pyplot(fig4)

st.subheader('Gráfico - Preço de Fechamento com Médias Móveis de 7 e 30 dias')

# Calcula as médias móveis
df['MA7'] = df['Close*'].rolling(window=7).mean()
df['MA30'] = df['Close*'].rolling(window=30).mean()

fig5, ax5 = plt.subplots(figsize=(10, 5))
ax5.plot(df['Date'], df['Close*'], label='Preço de Fechamento')
ax5.plot(df['Date'], df['MA7'], label='Média Móvel 7 dias', linestyle='--')
ax5.plot(df['Date'], df['MA30'], label='Média Móvel 30 dias', linestyle='--')

ax5.set_xlabel('Data')
ax5.set_ylabel('Preço')
ax5.set_title('Preço de Fechamento com Médias Móveis de 7 e 30 dias')
ax5.legend()
ax5.grid(True)

# Ajusta as datas no eixo X
locator = AutoDateLocator()
formatter = AutoDateFormatter(locator)
ax5.xaxis.set_major_locator(locator)
ax5.xaxis.set_major_formatter(formatter)
fig5.autofmt_xdate()

st.pyplot(fig5)


