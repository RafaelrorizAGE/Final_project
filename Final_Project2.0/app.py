import streamlit as st
import pandas as pd
from dataset import df  
from graficos import barra_quant, linha_quant, area_quant, barra_temp, linha_temp, area_temp  # Importa os gráficos

def homepage():
    st.title('Análise de Vendas sobre o Tesouro Direto')
    st.header('Projeto de Análise de Dados')
    st.write('Este projeto tem como fim avaliar as fases de uma pipeline ETL.')
    st.header('Sobre o Projeto')
    st.write('')
    st.write('')
    col1, col2 = st.columns([2, 4])
    with col1:
        st.header("IMAGEM")
        # st.image('arquivos/ror.jpeg', caption='Rafael R M Pereira', width=250)

    with col2:
        st.header('Rafael Roriz de Menezes Pereira')
        st.markdown('''Linkedin: https://www.linkedin.com/in/rafael-roriz-de-menezes-5300161b1 \n\n Github: https://github.com/RafaelrorizAGE''')

def mainpage():
    n_samples = st.sidebar.number_input("Escolha o número de amostras (por tipo de título)", min_value=1, value=10, step=1)

    def select_balanced_samples(df, n_samples):
        samples_per_group = n_samples
        grouped = df.groupby('Tipo Titulo')
        balanced_samples = pd.DataFrame()
        for _, group in grouped:
            samples = group.sample(min(len(group), samples_per_group), random_state=1)
            balanced_samples = pd.concat([balanced_samples, samples], ignore_index=True)
        return balanced_samples

    # Seleção de amostras equitativas antes de gerar gráficos
    df_samples = select_balanced_samples(df, n_samples)

    chart_data = st.sidebar.selectbox("Selecione o dado analisado", ['Valor por Quantidade' , 'Valor ao longo do Tempo'])

    # Seleção de tipo de gráfico
    chart_type = st.sidebar.selectbox("Selecione o tipo de gráfico", ['Barra', 'Linha', 'Scatter', 'Área'])
    # Renderização do gráfico selecionado
    if chart_data == 'Valor por Quantidade':

        if chart_type == 'Barra':
            st.plotly_chart(barra_quant)
        elif chart_type == 'Linha':
            st.plotly_chart(linha_quant)
        elif chart_type == 'Área':
            st.plotly_chart(area_quant)
    elif chart_data == 'Valor ao longo do Tempo':
        if chart_type == 'Barra':
            st.plotly_chart(barra_temp)
        elif chart_type == 'Linha':
            st.plotly_chart(linha_temp)
        elif chart_type == 'Área':
            st.plotly_chart(area_temp) 

    # Mostrar tabela de dados das amostras
    show_table = st.sidebar.checkbox("Mostrar Tabela de Dados", value=True)

    # Mostrar tabela de dados se selecionado
    if show_table:
        st.write("Tabela de Dados das Amostras:")
        st.table(df_samples)

# Configuração do app para utilizar páginas
st.set_page_config(page_title="Análise de Vendas do Tesouro Direto", layout="wide")

# Sidebar para navegação
st.sidebar.title('Navegação')
selection = st.sidebar.radio("Ir para", ["Home", "Análise de Dados"])

# Renderiza a página selecionada
if selection == "Home":
    homepage()
elif selection == "Análise de Dados":
    mainpage()
