import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Criando dados fictícios
dados = {
    'Dia': ['Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado', 'Domingo'],
    'Vendas': [1200, 1500, 1700, 1600, 2000, 2500, 2200],
    'Clientes': [100, 130, 140, 135, 180, 220, 200],
    'Lucro': [300, 400, 450, 420, 600, 800, 700]
}

# Criando um DataFrame
df = pd.DataFrame(dados)

# Gráfico de barras - Total de vendas por dia
plt.figure(figsize=(10, 5))
sns.barplot(x='Dia', y='Vendas', data=df, palette='Blues')
plt.title('Total de Vendas por Dia')
plt.xlabel('Dia da Semana')
plt.ylabel('Total de Vendas')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()

# Gráfico de dispersão - Número de clientes vs. Total de vendas
plt.figure(figsize=(8, 5))
sns.scatterplot(x='Clientes', y='Vendas', data=df, color='red', s=100)
plt.title('Relação entre Número de Clientes e Vendas')
plt.xlabel('Número de Clientes')
plt.ylabel('Total de Vendas')
plt.grid(True, linestyle='--', alpha=0.7)
plt.show()

# Heatmap - Correlação entre Vendas, Clientes e Lucro
plt.figure(figsize=(6, 4))
sns.heatmap(df[['Vendas', 'Clientes', 'Lucro']].corr(), annot=True, cmap='coolwarm', linewidths=0.5)
plt.title('Correlação entre Vendas, Clientes e Lucro')
plt.show()

# Explicação breve:
# 1. O gráfico de barras mostra a variação das vendas ao longo da semana, ajudando a identificar os dias mais lucrativos.
# 2. O gráfico de dispersão revela a relação entre o número de clientes e o total de vendas, evidenciando se há uma correlação forte.
# 3. O heatmap exibe a correlação entre as variáveis, indicando quais fatores estão mais associados ao desempenho de vendas.
