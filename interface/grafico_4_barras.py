import plotly_express as px
import pandas as pd

def grafico_barras_producto(data):
    revenues_productos = (
        data.groupby("tipo_producto")["valor_total"].sum()
        .sort_values(ascending = False)
        .reset_index()
    )
    
    # Creando el gráfico
    fig = px.bar(revenues_productos.head(10),
        x = 'tipo_producto',
        y = 'valor_total',
        text = 'valor_total',
        title = "Top ingresos por Producto ($)"
    )
    fig.update_layout(
        yaxis_title='Ingresos ($)',
        xaxis_title='Tipo de Producto',
        showlegend=False
    )
    fig.update_xaxes(tickangle=45)
    fig.update_traces(
        texttemplate = '%{text:.3s}',
        hovertemplate = '<b>%{x}</b><br>Ingresos totales: $%{y:,.0f}<extra></extra>'
    )
    return fig