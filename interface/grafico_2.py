import plotly_express as px
import pandas as pd

def grafico_linea(data):
    # Para el gráfico 2, el de líneas
    revenues_monthly = data.set_index('fecha_compra').groupby(pd.Grouper(freq = 'ME'))['valor_total'].sum().reset_index()
    revenues_monthly['Year'] = revenues_monthly['fecha_compra'].dt.year
    revenues_monthly['Month'] = revenues_monthly['fecha_compra'].dt.month
    month = {	
            1:'January',
            2:'February',
            3:'March',
            4:'April',
            5:'May',
            6:'June',
            7:'July',
            8:'August',
            9:'September',
            10:'October',
            11:'November',
            12:'December'}
    revenues_monthly['Month'] = revenues_monthly['Month'].map(month)
    # Ordenar los datos usando el diccionario
    month_order = {
            'January': 1, 'February': 2, 'March': 3, 'April': 4, 
            'May': 5, 'June': 6, 'July': 7, 'August': 8, 
            'September': 9, 'October': 10, 'November': 11, 'December': 12
        }
    revenues_monthly['Month'] = pd.Categorical(revenues_monthly['Month'], categories=month_order.keys(), ordered=True)
    revenues_monthly = revenues_monthly.sort_values(by=['Month'])
        
    fig_grafico_lineas = px.line(revenues_monthly,
    x = 'Month',
    y = 'valor_total',
    markers = True,
    range_y = (0, revenues_monthly.max()),
    color = 'Year')
    
    return fig_grafico_lineas