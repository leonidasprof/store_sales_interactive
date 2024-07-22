import plotly.graph_objects as go
import pandas as pd 
import requests

# Función para obtener el archivo GeoJSON de los estados de Brasil
def obtener_geojson_brasil():
    url = 'https://raw.githubusercontent.com/codeforamerica/click_that_hood/master/public/data/brazil-states.geojson'
    response = requests.get(url)
    return response.json()


def grafico_mapa(df):
    df=df.rename(columns={'abbrev_state':'sigla'})
    df_mapa = df.groupby('sigla').agg({
        'valor_total': 'sum',
    }).reset_index()

    geojson_brasil = obtener_geojson_brasil()

    fig = go.Figure(data=go.Choropleth(
        geojson=geojson_brasil,
        locations=df_mapa['sigla'],  # Coordenadas espaciales
        z=df_mapa['valor_total'].astype(float),  # Datos a codificar por color
        featureidkey="properties.sigla",  # Clave para acceder a las siglas en el archivo GeoJSON
        colorscale="Blues",  # Escala de colores
        #colorbar_title ="Ingresos ($)",
        marker_line_color='black',
           colorbar=dict(
            title='Ingresos ($)',
            len=0.8,  # Proporción de la longitud de la barra de colores
            y=0.5,  # Posición vertical de la barra de colores
            thickness=20,  # Grosor de la barra de colores
        )# Color de las líneas de los bordes
    ))
    
    fig.update_geos(
        fitbounds="locations",  # Ajustar el rango del mapa a los estados presentes en el DataFrame
        visible=False  # No mostrar elementos de geografía adicionales
    )

    fig.update_layout(
        title='Valores por estado en Brasil',
       # plot_bgcolor='rgba(0, 0, 0, 0)',  # Hacer el fondo del gráfico transparente
        #paper_bgcolor='rgba(0, 0, 0, 0)',  # Hacer el fondo del papel transparente
        geo=dict(
            bgcolor='rgba(0, 0, 0, 0)',
            
        ),
        width=2000,  # Ancho del gráfico
        height=500 # Altura del gráfico
    )  # Cambiar el fondo del gráfico a azul
      
    

    return fig



    



