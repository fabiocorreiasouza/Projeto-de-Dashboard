import streamlit as st
import mysql.connector
import pandas as pd
import plotly.express as px

# Conexão ao MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="dudu2004",
    database="Oasis"
)

st.title("Dashboard dos Projetos de Lei da Câmara dos Deputados - OASIS")

query = """
SELECT YEAR(datadeapresentacao) AS ano, COUNT(*) AS quantidade
FROM Projetos
WHERE datadeapresentacao IS NOT NULL
GROUP BY YEAR(datadeapresentacao)
ORDER BY ano;
"""

df = pd.read_sql(query, conn)
#print(df)
fig = px.line(df, x="ano", y="quantidade", title="Número de Projetos Apresentados por Ano")
fig.update_xaxes(dtick=1)
st.plotly_chart(fig)

query = """
SELECT partido, COUNT(*) AS quantidade
FROM Projetos
WHERE partido IS NOT NULL AND partido <> ''
GROUP BY partido
ORDER BY quantidade DESC;
"""

df = pd.read_sql(query, conn)
#print(df)

fig = px.pie(
    df,
    names="partido",
    values="quantidade",
    title="Distribuição de Projetos por Partido"
)
st.plotly_chart(fig)

query = """
SELECT descricao, COUNT(*) AS quantidade
FROM Projetos
WHERE descricao IS NOT NULL AND descricao <> ''
GROUP BY descricao
ORDER BY quantidade DESC;
"""

df = pd.read_sql(query, conn)
fig = px.bar(df, x="descricao", y="quantidade", title="Número de Projetos por Descrição da Sigla")
st.plotly_chart(fig)

# Nuvem de palavras da indexacao
# Quantos projetos tem em cada situacao (em porcentagem?)
# Quantos projetos possuem aquele ultimo estado
# Quantos projetos por autor