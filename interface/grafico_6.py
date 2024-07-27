import plotly_express as px
import pandas as pd


def grafico_ingresos_vendedores(df):
    
    df.loc[:, 'ingresos'] = df['valor_total'] - df['costo_envio']
    
    ingresos = (
        df.groupby('nombre_vendedor')[['ingresos']].sum()
        .sort_values('ingresos')
        .reset_index()
        .iloc[:5]
    )
        
    fig = px.bar(
        ingresos,
        x = 'ingresos',
        y = 'nombre_vendedor',
        text = 'ingresos',
        orientation='h',
        title = "Ingresos por vendedores ($)"
    )
    
    fig.update_layout(
        xaxis_title = 'Ingresos ($)',
        yaxis_title = 'Vendedores',
        showlegend = False
    )
    
    fig.update_traces(
        texttemplate = '%{text:.3s}',
        hovertemplate = '<b>%{y}</b><br>Ingresos Totales: $%{x:,.0f}<extra></extra>'
    )
    
    return fig