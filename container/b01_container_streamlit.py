import os, sys
sys.path.append(os.getcwd())
import streamlit as st 
import pandas as pd 
from controller.a01_preproceso import DataStorage 
from functions.function_format_num import formato_numero
from functions.function_delta import delta
from interface.grafico1 import grafico_mapa
from interface.grafico_2 import grafico_linea
from interface.grafico_3_barras import grafico_barras_ciudades
from interface.grafico_4_barras import grafico_barras_producto
br_final=DataStorage.br_final



#Configuracion
st.set_page_config(layout='wide')

#Configuramos los filtros-------------------------------------------------------
st.sidebar.image('https://i.postimg.cc/8kvVTRJp/brazil.png')
st.sidebar.title('Filtros')

estados=sorted(list(br_final['state_name'].unique()))
ciudades = st.sidebar.multiselect('Estados', estados)

if ciudades:
    br_final=br_final[br_final['state_name'].isin(ciudades)]


# Interacción de filtros--------------------------------------------------------
graf_mapa=grafico_mapa(br_final)
graf_linea = grafico_linea(br_final)
graf_barras_ciudades = grafico_barras_ciudades(br_final)
graf_barras_producto = grafico_barras_producto(br_final)
#-------------------------- Se calcula el delta cuando este el filtro del año ------------------
delta_revenue,delta_ventas=delta(br_final,'2020')

st.title('Dashboard de Ventas :shopping_trolley:')
col1,col2=st.columns(2)



with col1:
    st.metric('**Total de Revenues**',formato_numero( br_final['valor_total'].sum()),delta=delta_revenue)
    st.plotly_chart(graf_mapa)
    st.plotly_chart(graf_barras_ciudades,use_container_width=True)
with col2:
    st.metric('**Total de Ventas**', formato_numero(br_final['cantidad'].sum()),delta=delta_ventas)
    st.plotly_chart(graf_linea,use_container_width=True)
    st.plotly_chart(graf_barras_producto,use_container_width=True)




# Mostrando filtros-------------------------------------------------
dataframe_toggle = st.toggle("Hide/Show Dataframe", value=False)
if dataframe_toggle:
    st.dataframe(br_final.head(15))
