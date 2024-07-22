import os, sys
sys.path.append(os.getcwd())
import streamlit as st 
import pandas as pd 
from controller.a01_preproceso import DataStorage 
from functions.function_format_num import formato_numero
from interface.grafico1 import grafico_mapa
from interface.grafico_2 import grafico_linea
br_final=DataStorage.br_final

#Configuracion


st.set_page_config(layout='wide')


st.sidebar.title('Filtros')


graf_mapa=grafico_mapa(br_final)
graf_linea = grafico_linea(br_final)

st.title('Dashboard de Ventas :shopping_trolley:')
col1,col2=st.columns(2)

with col1:
    st.metric('**Total de Revenues**',formato_numero( br_final['valor_total'].sum()))
    st.plotly_chart(graf_mapa,use_container_width=True)
with col2:
    st.metric('**Total de Revenues**', formato_numero(br_final['cantidad'].sum()))
    st.plotly_chart(graf_linea,use_container_width=True)
