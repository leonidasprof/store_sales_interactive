import pandas as pd
import plotly_express as px


def grafico_pizza(df):
    
    color_sequence = ['#003f5c', '#2f4b7c', '#4361a0', '#5a73c7', '#90baf7']

    vendedores = (
        df.groupby('nombre_vendedor')[['cantidad']].sum()
        .sort_values('cantidad',ascending=False)
        .reset_index()
        .iloc[:5]
    )
    
    vendedores = vendedores.rename(columns={
        'cantidad': 'total_ventas',
        'nombre_vendedor': 'vendedor_name'})
    
    fig = px.pie(vendedores,
        values = 'total_ventas',
        names = 'vendedor_name',
        title = 'Ventas por vendedores',
        color_discrete_sequence = color_sequence
    )
    
    fig.update_traces(
        textposition='inside',
        textinfo='percent+label',
        texttemplate='%{label}<br>%{percent:,.2%}',
        hovertemplate='<b>%{label}</b><br>Ventas Totales: %{value:,.0f}<extra></extra>'
    )
    
    fig.update_layout(showlegend=False,
                      title_x=0.4)  # Centra el título
    
    return fig