# código de geração do gráfico 
import pandas as pd

# Carregar o arquivo CSV em um DataFrame
df_galosina = pd.read_csv('gasolina.csv')

import seaborn as sns

with sns.axes_style('whitegrid'):

  grafico = sns.lineplot(data= df_galosina, x = 'dia', y = 'venda', palette='pastel')
  grafico.set(title = 'preço médio de venda da gasolina na cidade de São Paulo', xlabel = 'dia', ylabel = 'venda');

grafico.figure.savefig("gasolina.png")