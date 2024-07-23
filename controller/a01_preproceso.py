import os, sys
sys.path.append(os.getcwd())
# Lee los datos de ventas
import pandas as pd 

#df = pd.read_csv('')

# Módulo para almacenar las variables calculadas
class DataStorage:
    br_final = None


df_itens_pedidos = pd.read_csv('base/data/df_itens_pedidos.csv')
df_itens_pedidos.head()

df_pedidos = pd.read_csv('base/data/df_pedidos.csv')
df_pedidos.head()

df_productos = pd.read_csv('base/data/df_productos.csv')
df_productos.head()

df_vendedores = pd.read_csv('base/data/df_vendedores.csv')
df_vendedores.head()


def preprocesamiento(df_itens_pedidos,df_pedidos,df_productos,df_vendedores):
    #========================================================================================
                            #Preprocesamiento DF_ITENS_PEDIDOS
    #========================================================================================
    states = {
    'AC': 'Acre', 'AL': 'Alagoas', 'AP': 'Amapá', 'AM': 'Amazonas', 'BA': 'Bahia',
    'CE': 'Ceará', 'DF': 'Distrito Federal', 'ES': 'Espírito Santo', 'GO': 'Goiás',
    'MA': 'Maranhão', 'MT': 'Mato Grosso', 'MS': 'Mato Grosso do Sul', 'MG': 'Minas Gerais',
    'PA': 'Pará', 'PB': 'Paraíba', 'PR': 'Paraná', 'PE': 'Pernambuco', 'PI': 'Piauí',
    'RJ': 'Rio de Janeiro', 'RN': 'Rio Grande do Norte', 'RS': 'Rio Grande do Sul',
    'RO': 'Rondônia', 'RR': 'Roraima', 'SC': 'Santa Catarina', 'SP': 'São Paulo',
    'SE': 'Sergipe', 'TO': 'Tocantins'
    }
    
    df_itens_pedidos.drop_duplicates(inplace=True)
    df_itens_pedidos['producto_id'].drop_duplicates(inplace=True)
    df_itens_pedidos=df_itens_pedidos.dropna().reset_index(drop=True)
    df_itens_pedidos['sigla']=df_itens_pedidos['ciudad'].str.split("-").str[1]
    df_itens_pedidos['state_name'] = df_itens_pedidos['sigla'].map(states)
 
   #========================================================================================
                            #Preprocesamiento DF_PEDIDOS
    #========================================================================================
    df_pedidos.drop_duplicates(inplace=True)
    df_pedidos['producto_id'].drop_duplicates(inplace=True)
    df_pedidos['fecha_compra']=pd.to_datetime(df_pedidos['fecha_compra'])
    df_pedidos=df_pedidos.dropna().reset_index(drop=True)
    #========================================================================================
                            #Preprocesamiento DF_PRODUCTOS
    #========================================================================================
    df_productos.drop_duplicates(inplace=True)
    df_productos['producto_id'].drop_duplicates(inplace=True)
    df_productos=df_productos.dropna().reset_index(drop=True)
    df_productos['tipo_producto']=df_productos['producto'].str.split("_").str[0]
  #========================================================================================
                            #Preprocesamiento DF_VENDEDORES
    #========================================================================================
    df_vendedores.drop_duplicates(inplace=True)
    df_vendedores=df_vendedores.dropna().reset_index(drop=True)
    df_vendedores = df_vendedores[df_vendedores['nombre_vendedor'] != 'Unknown']


    return df_itens_pedidos,df_pedidos,df_productos,df_vendedores

df_itens_pedidos,df_pedidos,df_productos,df_vendedores=preprocesamiento(df_itens_pedidos,df_pedidos,df_productos,df_vendedores)

print(df_itens_pedidos.info())
print('-------------')
print(df_pedidos.info())
print('-------------')
print(df_productos.info())
print('-------------')
print(df_vendedores.info())

merged1 = pd.merge(df_itens_pedidos, df_pedidos, on=['producto_id', 'pedido_id'])
merged2 = pd.merge(merged1, df_productos, on='producto_id')
br_final = pd.merge(merged2, df_vendedores, on='vendedor_id')


DataStorage.br_final=(br_final)


