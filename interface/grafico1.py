import plotly.graph_objects as go
import pandas as pd 
import requests
from functions.function_format_num import formato_numero


def grafico_mapa(df):

    # Función para obtener el archivo GeoJSON de los estados de Brasil
    def obtener_geojson_brasil():
        url = 'https://raw.githubusercontent.com/codeforamerica/click_that_hood/master/public/data/brazil-states.geojson'
        response = requests.get(url)
        return response.json()
    
    df_mapa = df.groupby('state_name').agg({
        'valor_total': 'sum',
    }).reset_index()
    #df_mapa['valor_total'] = (df_mapa['valor_total'] / 1000000).apply(lambda x: round(x, 2))
    geojson_brasil = obtener_geojson_brasil()
    fig = go.Figure(data=go.Choropleth(
        geojson=geojson_brasil,
        locations=df_mapa['state_name'],  # Coordenadas espaciales
        z=df_mapa['valor_total'],  # Datos a codificar por color
        featureidkey="properties.name",  # Clave para acceder a las siglas en el archivo GeoJSON
        colorscale="Blues",  # Escala de colores
        colorbar_tickprefix='$',
        customdata=df[['state_name','valor_total']],
        colorbar_title="Ingresos ($)",
        marker_line_color='black',
        colorbar={
            'tickformat':'.3s',
            'x': 0.88,  # Ajusta la posición x de la barra de colores
            'xpad': 10  # Ajusta la separación horizontal
            }
        ))
    
    fig.update_geos(
        fitbounds="locations",  # Ajustar el rango del mapa a los estados presentes en el DataFrame
        visible=False  # No mostrar elementos de geografía adicionales
    )

    fig.update_layout(
        title='Ingresos por Estado ($)',
        geo=dict(
            bgcolor='rgba(0, 0, 0, 0)',
        ),
        width=2000,  # Ancho del gráfico
        height=500  # Altura del gráfico
    )
    
    fig.update_traces(
        hovertemplate='<b>%{location}</b><br>Valor Total: $%{z:,.0f}<extra></extra>',
    )

    return fig




