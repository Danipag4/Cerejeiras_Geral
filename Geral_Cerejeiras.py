import streamlit as st 
import pandas as pd 
import plotly_express as px 
#import matplotlib.pyplot as plt

st.set_page_config(layout="wide")

df = pd.read_csv("Geral_Cerejeiras.csv", sep=",")


df=df.sort_values("Setor")

df["Colab"] = df["Nome"]
df["Compet"] = df["Competencia"]
df["Setor"] = df["Setor"]
df["Setorial"] = df["Setor"]

st.write("""
# Cerejeiras - Análise de Competências
""" )
aval = ["Autoavaliação","Gestor","Pares","Liderados"]
Nome = st.selectbox("Setor",df["Setor"].unique())
df_filtered = df[df["Setor"] == Nome]
#df_filtered
df_Média = df_filtered.groupby("Compet")[["Autoavaliação","Gestor","Pares","Liderados"]].mean().round(decimals=2).reset_index()
#df_Média
aval = ["Autoavaliação","Gestor","Pares","Liderados"]

#----------------------------------------------------------------------

st.write("""
## Setor
""" ), Nome
fig_comp = px.bar(df_Média, y=aval, x="Compet", barmode='group', color_discrete_map = {"Autoavaliação":"#281BD2", "Gestor":"#764D29","Pares":"#EDEC7C", "Liderados":"#F0A652"})
fig_comp.update_layout(xaxis_title="Competências", yaxis_title="Médias")

fig_comp

#df_filtered

#-------------------------------------------------------------------------------------------

st.write("""
## Desempenho Geral por Colaborador
""" ), Nome

Compet_Desemp = Nome
#Compet_Desemp = st.selectbox("Defina o Setor",df["Setor"].unique(),index=1)
df_filtered5 = df[df["Setor"] == Compet_Desemp]
df_MédiaGeral = df_filtered5.groupby("Nome")[["Autoavaliação","Gestor","Pares","Liderados"]].mean().round(decimals=2).reset_index()
#df_MédiaGeral = df_filtered5.groupby("Nome")[["Autoavaliação","Gestor"]].mean().round(decimals=2).sort_values('Gestor').reset_index()
#df_MédiaGeral

if Nome == "CAMPO":
    fig_DesenvGeral = px.bar(df_MédiaGeral, x=aval, y="Nome", orientation="h", height=1200, barmode='group',color_discrete_map = {"Autoavaliação":"#281BD2", "Gestor":"#764D29","Pares":"#EDEC7C", "Liderados":"#F0A652"})
    fig_DesenvGeral.update_layout(xaxis_title="Média", yaxis_title="Colaborador")
    fig_DesenvGeral    

else:
    
    fig_DesenvGeral = px.bar(df_MédiaGeral, x=aval, y="Nome", orientation="h", height=600, barmode='group',color_discrete_map = {"Autoavaliação":"#281BD2", "Gestor":"#764D29","Pares":"#EDEC7C", "Liderados":"#F0A652"})
    fig_DesenvGeral.update_layout(xaxis_title="Média", yaxis_title="Colaborador")
    fig_DesenvGeral



