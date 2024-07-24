import plotly_express as px
import pandas as pd

def grafico_barras_producto(data):
    data["tipo_productos"] = data["tipo_producto"].str.split(" ").str[0]
    revenues_productos = data.groupby("tipo_productos")["valor_total"].sum().sort_values(ascending = False).reset_index()
    
    # Creando el gráfico
    fig = px.bar(revenues_productos.head(10),
        x = 'tipo_productos',
        y = 'valor_total',
        text = 'valor_total'
    )
    fig.update_layout(yaxis_title='Ingresos ($)',
                              xaxis_title='Tipo de Producto',
                              showlegend=False)
    fig.update_xaxes(tickangle=45)
    return fig