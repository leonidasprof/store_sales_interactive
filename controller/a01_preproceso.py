
import os, sys
sys.path.append(os.getcwd())
# Lee los datos de ventas
import pandas as pd 

df_itens_pedidos = pd.read_csv("base/data/df_itens_pedidos.csv", sep = ",")

df_pedidos = pd.read_csv("base/data/df_pedidos.csv", sep = ",")

df_productos = pd.read_csv("base/data/df_productos.csv", sep = ",")

df_vendedores = pd.read_csv("base/data/df_vendedores.csv", sep = ",")



# Módulo para almacenar las variables calculadas
class DataStorage:
    df_itens_pedidos = None
    df_pedidos = None
    df_productos = None
    df_vendedores = None
    df_final = None

# Tratando los datos nulos

def eliminando_nulos(df):
    nulos = df.isnull().sum().sum()
    if nulos > 0:
        df = df.dropna().reset_index()
    else:
        df = df
    return df
   
# Eliminando nulos de df_itens_pedidos
df_itens_pedidos = eliminando_nulos(df_itens_pedidos)

# Eliminando nulos de df_pedidos
df_pedidos = eliminando_nulos(df_pedidos)

# Eliminando nulos de df_productos
df_productos = eliminando_nulos(df_productos)

# Eliminando nulos de df_vendedores
df_vendedores = eliminando_nulos(df_vendedores)



#  Eliminand los datos duplicados

def eliminando_duplicados(df):
    nulos = df.duplicated().sum()
    if nulos > 0:
        df = df.drop_duplicates().reset_index()
    else:
        df = df
    return df
   
# Eliminando nulos de df_itens_pedidos
df_itens_pedidos = eliminando_duplicados(df_itens_pedidos)

# Eliminando nulos de df_pedidos
df_pedidos = eliminando_duplicados(df_pedidos)

# Eliminando nulos de df_productos
df_productos = eliminando_duplicados(df_productos)

# Eliminando nulos de df_vendedores
df_vendedores = eliminando_duplicados(df_vendedores)



# Valores Unicos
columnas_itens = df_itens_pedidos.columns
for columna in columnas_itens:
    print(columna, df_itens_pedidos[columna].unique())
    print("#----------------------------------------#")
    

columnas_pedidos = df_pedidos.columns
for columna in columnas_pedidos:
    print(columna, df_pedidos[columna].unique())
    print("#----------------------------------------#")


columnas_producto = df_productos.columns
for columna in columnas_producto:
    print(columna, df_productos[columna].unique())
    print("#----------------------------------------#")


columnas_vendedores = df_vendedores.columns
for columna in columnas_vendedores:
    print(columna, df_vendedores[columna].unique())
    print("#----------------------------------------#")

# Seleccionando los registros con vendedores conocidos, los que marcan Unknown serán descartadas
df_vendedores = df_vendedores[df_vendedores['nombre_vendedor'] != 'Unknown']
print(df_vendedores["nombre_vendedor"].unique())

states = {
    'AC': 'Acre', 'AL': 'Alagoas', 'AP': 'Amapá', 'AM': 'Amazonas', 'BA': 'Bahia',
    'CE': 'Ceará', 'DF': 'Distrito Federal', 'ES': 'Espírito Santo', 'GO': 'Goiás',
    'MA': 'Maranhão', 'MT': 'Mato Grosso', 'MS': 'Mato Grosso do Sul', 'MG': 'Minas Gerais',
    'PA': 'Pará', 'PB': 'Paraíba', 'PR': 'Paraná', 'PE': 'Pernambuco', 'PI': 'Piauí',
    'RJ': 'Rio de Janeiro', 'RN': 'Rio Grande do Norte', 'RS': 'Rio Grande do Sul',
    'RO': 'Rondônia', 'RR': 'Roraima', 'SC': 'Santa Catarina', 'SP': 'São Paulo',
    'SE': 'Sergipe', 'TO': 'Tocantins'
}

df_pedidos["fecha_compra"] = pd.to_datetime(df_pedidos["fecha_compra"])

# Dividiendo con split la incial del estado y creando nueva columna states
df_itens_pedidos['ciudad'] = df_itens_pedidos['ciudad'].str.split("-").str[1]
df_itens_pedidos['state_name'] = df_itens_pedidos['ciudad'].map(states)

print(df_itens_pedidos)


merged1 = pd.merge(df_itens_pedidos, df_pedidos, on=['producto_id', 'pedido_id'])
merged2 = pd.merge(merged1, df_productos, on='producto_id')
df_final = pd.merge(merged2, df_vendedores, on='vendedor_id')

print(df_final)

DataStorage.df_itens_pedidos=(df_itens_pedidos)
df_itens_pedidos=df_itens_pedidos.copy()

DataStorage.df_pedidos=(df_pedidos)
df_pedidos=df_pedidos.copy()

DataStorage.df_productos=(df_productos)
df_productos=df_productos.copy()

DataStorage.df_productos=(df_productos)
df_productos=df_productos.copy()

DataStorage.df_final=(df_final)
df_final=df_final.copy()