import plotly_express as px
import pandas as pd 
    

def grafico_barras_ciudades(df):
    df = (
        df.groupby('state_name')[['valor_total']].sum()
        .sort_values('valor_total', ascending=False)
        .reset_index()
        .iloc[:10]
    )
    
    fig=px.bar(
        df,
        x='state_name',
        y='valor_total',
        text='valor_total',
        title='Top Ingresos por Estado ($)'
    )
    fig.update_layout(
        yaxis_title='Ingresos ($)',
        xaxis_title='Estados',
        showlegend=False
    )
    fig.update_traces(
        texttemplate='%{text:.3s}',
        hovertemplate='<b>Estado: %{x}</b><br>Valor Total: $%{y:,.0f}<extra></extra>'
    )
    fig.update_xaxes(tickangle=45)
    
    return fig