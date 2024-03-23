import plotly.express as px # importa nossa biblioteca gráfica
from dataset import  df  # importa o df do nosso arquivo dataset.py


barra_quant = px.bar(df, x='Quantidade', y='Valor', color='Tipo Titulo', title='Valor por Quantidade')

linha_quant = px.line(df, x='Quantidade', y='Valor', color='Tipo Titulo', title='Valor por Quantidade')

area_quant = px.area(df, x='Quantidade', y='Valor', color='Tipo Titulo', title='Valor por Quantidade')

barra_temp = px.bar(df, x='Data Venda', y='Valor', color='Tipo Titulo', title='Valor ao longo do Tempo')

linha_temp = px.line(df, x='Data Venda', y='Valor', color='Tipo Titulo', title='Valor ao longo do Tempo')

area_temp =px.area(df, x='Data Venda', y='Valor', color='Tipo Titulo', title='Valor ao longo do Tempo')