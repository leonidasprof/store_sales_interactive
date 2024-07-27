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
from interface.grafico_5 import grafico_pizza
from interface.grafico_6 import grafico_ingresos_vendedores


br_final=DataStorage.br_final

#Configuracion
st.set_page_config(layout='wide')

#Configuramos los filtros-------------------------------------------------------
st.sidebar.image('https://i.postimg.cc/Hny9LmTT/brazil.png')
st.sidebar.title('Filtros')

estados=sorted(list(br_final['state_name'].unique()))
ciudades = st.sidebar.multiselect('Estados', estados)

if ciudades:
    br_final=br_final[br_final['state_name'].isin(ciudades)]

# Filtro producto --------------------------------------------------------
br_final["tipo_productos"] = br_final["tipo_producto"].str.split(" ").str[0]
productos = sorted(list(br_final["tipo_productos"].dropna().unique()))
productos.insert(0,"Todos")
producto = st.sidebar.selectbox("Productos",productos)

    #-------------------------- Se calcula el delta cuando este el filtro del año ------------------
delta_revenue,delta_ventas=delta(br_final)
if producto != "Todos":
    br_final = br_final[br_final["tipo_productos"] == producto]


años = st.sidebar.checkbox('Todo el periodo', value=True)
if not años:
    año1 = st.sidebar.slider(
        'Año',
        br_final['fecha_compra'].dt.year.min(), 
        br_final['fecha_compra'].dt.year.max()

    )
    #-------------------------- Se calcula el delta cuando este el filtro del año ------------------
    delta_revenue,delta_ventas=delta(br_final,año1)
if not años:
	br_final = br_final[br_final['fecha_compra'].dt.year == año1]


# Interacción de filtros--------------------------------------------------------
graf_mapa=grafico_mapa(br_final)
graf_linea = grafico_linea(br_final)
graf_barras_ciudades = grafico_barras_ciudades(br_final)
graf_barras_producto = grafico_barras_producto(br_final)
graf_pizza = grafico_pizza(br_final)
graf_ingresos = grafico_ingresos_vendedores(br_final)


st.header(':shopping_trolley: DASHBOARD :green[BRASİ-İOPE] :shopping_bags:', divider='rainbow')

col1, col2=st.columns(2)

with col1:
    st.metric(' 💰 **Total de Revenues**',formato_numero(br_final['valor_total'].sum()),delta=delta_revenue)
    st.plotly_chart(graf_mapa, use_container_width=True)
    st.plotly_chart(graf_barras_ciudades, use_container_width=True)
    st.plotly_chart(graf_ingresos, use_container_width=True)
with col2:
    st.metric(' 💲 **Total de Ventas**', formato_numero(br_final['cantidad'].sum()),delta=delta_ventas)
    st.plotly_chart(graf_linea, use_container_width=True)
    st.plotly_chart(graf_barras_producto, use_container_width=True)
    st.plotly_chart(graf_pizza, use_container_width=True)