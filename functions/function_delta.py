# docstring

def delta(df, año):
    """
    Calcula el cambio porcentual en ingresos y cantidad de ventas entre dos años consecutivos en un DataFrame.

    Parámetros:
    df (pd.DataFrame): DataFrame que contiene los datos de ventas, incluyendo las columnas 'fecha_compra' (datetime) y 'valor_total' (numérico) y 'cantidad' (numérico).
    año (int): El año para el cual se desea calcular el delta en ingresos y ventas respecto al año anterior.

    Retorna:
    tuple: Una tupla que contiene dos strings:
        - delta_revenue (str): El cambio porcentual en ingresos entre el año dado y el año anterior. 
          Formateado con un decimal seguido del símbolo de porcentaje, por ejemplo, '10.0%'. 
          Devuelve '0%' si el valor del año anterior es cero o si el año proporcionado no es válido.
        - delta_ventas (str): El cambio porcentual en cantidad de ventas entre el año dado y el año anterior. 
          Formateado con un decimal seguido del símbolo de porcentaje, por ejemplo, '10.0%'. 
          Devuelve '0%' si el valor del año anterior es cero o si el año proporcionado no es válido.

    Excepciones:
    - ValueError: Se lanza si el año proporcionado no puede convertirse a entero.
    """
    try:
        año = int(año)
    except ValueError:
        return '0%', '0%'

    # Calcular el delta de ingresos
    valor_actual = df[df['fecha_compra'].dt.year == año]['valor_total'].sum()
    valor_anterior = df[df['fecha_compra'].dt.year == (año - 1)]['valor_total'].sum()

    if valor_anterior == 0:
        delta_revenue = '0%'
    else:
        delta_revenue = f'{round(((valor_actual - valor_anterior) / valor_anterior) * 100, 1)}%'

    # Calcular el delta de ventas
    valor_actual = df[df['fecha_compra'].dt.year == año]['cantidad'].sum()
    valor_anterior = df[df['fecha_compra'].dt.year == (año - 1)]['cantidad'].sum()

    if valor_anterior == 0:
        delta_ventas = '0%'
    else:
        delta_ventas = f'{round(((valor_actual - valor_anterior) / valor_anterior) * 100, 1)}%'

    return delta_revenue, delta_ventas