
import os, sys
sys.path.append(os.getcwd())
# Lee los datos de ventas
import pandas as pd 

#df = pd.read_csv('')

# Módulo para almacenar las variables calculadas
#class DataStorage:
 #   df_ventas = None


df_itens_pedidos = pd.read_csv('base/data/df_itens_pedidos.csv')
df_itens_pedidos.head()

df_pedidos = pd.read_csv('base/data/df_pedidos.csv')
df_pedidos.head()

df_productos = pd.read_csv('base/data/df_productos.csv')
df_productos.head()

df_vendedores = pd.read_csv('base/data/df_vendedores.csv')
df_vendedores.head()



def preprocesamiento(df_itens_pedidos,df_pedidos,df_productos,df_vendedores):


    return df_itens_pedidos,df_pedidos,df_productos,df_vendedores

