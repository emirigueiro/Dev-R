def df_validator(input_data):
    """
    Valida si la entrada es un DataFrame.
    
    Parámetros:
    input_data: cualquier tipo de entrada que se desee validar.
    
    Retorna:
    True si la entrada es un DataFrame.
    
    Lanza:
    TypeError si la entrada no es un DataFrame.
    """
    if isinstance(input_data, pd.DataFrame):
        return True
    else:
        raise TypeError("La entrada no es un DataFrame. Por favor, proporciona un DataFrame de pandas.")