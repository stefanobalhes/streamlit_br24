import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Carregar o DataFrame
df = pd.read_csv("merged_df.csv")  # Corrigido: Removido o ponto extra no nome do arquivo
df_squadless = df.drop(columns=["Squad"])

# Configuração do título e instruções
st.title("Brasileirão 2024")
st.subheader("Escolha duas estatísticas para plotar o gráfico por equipes")
st.write("Para plotar o gráfico por equipes, escolha uma das estatísticas abaixo:")

# Selecionar estatísticas com chaves exclusivas
estatistica_1 = st.selectbox("Escolha o eixo x", df_squadless.columns, key="estatistica_1")
estatistica_2 = st.selectbox("Escolha o eixo y", df_squadless.columns, key="estatistica_2")

# Defina as cores desejadas para cada Squad (se necessário)
color_map = {
    'ATP': 'red',
    'ATG': 'red',
    'ATM': 'black',
    'BAH': 'blue',
    'BOT': 'black',
    'COR': 'black',
    'CRI': '#D8A300',
    'CRU': 'blue',
    'CUI': 'green',
    'FLA': 'red',
    'FLU': '#7C0A2A',
    'FOR': 'blue',
    'GRE': 'blue',
    'INT': 'red',
    'JUV': 'green',
    'PAL': 'green',
    'RBR': 'black',
    'SÃO': 'red',
    'VDG': 'black',
    'VIT': 'red',
}

# Botão para gerar o gráfico
if st.button("Gerar Gráfico"):
    plt.figure(figsize=(10, 6))

    # Garantir que todos os Squads no seu DataFrame tenham uma cor no dicionário
    unique_squads = df['Squad'].unique()
    markers = ['s']

    # Plotar cada Squad com a cor e o marcador definidos
    for i, squad in enumerate(unique_squads):
        squad_data = df[df['Squad'] == squad]
        plt.scatter(squad_data[estatistica_1], squad_data[estatistica_2],
                    color=color_map.get(squad, '#333333'),
                    marker=markers[i % len(markers)], label=squad)

        # Adicionar o nome do Squad ao gráfico
        for j in range(len(squad_data)):
            plt.text(squad_data[estatistica_1].iloc[j],
                     squad_data[estatistica_2].iloc[j] + 0.025,  # Ajuste da posição do texto
                     squad_data['Squad'].iloc[j], fontsize=8, ha='center', va='center',
                     color='white', fontweight='bold',
                     bbox=dict(facecolor=color_map.get(squad, '#333333'), edgecolor='none', pad=1.5))

    # Título e rótulos dos eixos
    plt.title(f'Scatter Plot: {estatistica_1} vs {estatistica_2}')
    plt.xlabel(estatistica_1)
    plt.ylabel(estatistica_2)

    # Mostrar o gráfico
    st.pyplot(plt)

    # Limpar a figura após o plot
    plt.clf()  # Limpa a figura para não sobrepor os plots
