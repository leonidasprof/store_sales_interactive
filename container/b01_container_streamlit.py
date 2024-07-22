import os, sys
sys.path.append(os.getcwd())
import streamlit as st 
import pandas as pd 
from controller.a01_preproceso import DataStorage
from interface.grafico_2 import crear_grafico_linea


#Configuracion
st.set_page_config(layout='wide')

df_final = DataStorage.df_final

st.sidebar.title('Filtros')

graf_linea= crear_grafico_linea(df_final)

# Contenedor de la visualizacion
st.title('Dashboard de Ventas :shopping_trolley:')
col1,col2=st.columns(2)

with col1:
 #Agregando grafico de linea 
    st.plotly_chart(graf_linea, use_container_width = True)
