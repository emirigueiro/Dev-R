import main as dp
import pandas as pd

def profile_date(x):
    """
    Valida si la entrada es un DataFrame.
    
    Parámetros:
    input_data: cualquier tipo de entrada que se desee validar.
    
    Retorna:
    True si la entrada es un DataFrame.
    
    Lanza:
    TypeError si la entrada no es un DataFrame.
    """
    if isinstance(x, pd.DataFrame):
        return dp.profile_date(x)
    else:
        raise TypeError("La entrada no es un DataFrame. Por favor, proporciona un DataFrame de pandas.")