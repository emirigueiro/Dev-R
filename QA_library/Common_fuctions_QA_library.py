import pandas as pd

def volumen (x):
    volumn = pd.DataFrame(columns=['Count'])
    volumn.loc['Filas'] = x.shape[0]
    volumn.loc['Columnas'] = x.shape[1]
    return volumn

def column_list (x):
    columns_list = []
    columns_list = x.columns
    return columns_list

def count_list (x):
    column_list = x.columns
    count_list = []
    for y in column_list:
        column_data = x[y]
        if column_data is not None:
            count_list.append(column_data.count())

    return count_list

def unique_list (x):
    column_list = x.columns
    unique_list = []
    for y in column_list:
        column_data = x[y]
        if column_data is not None:
            unique_list.append(column_data.nunique())

    return unique_list

def empty_list (x):
    column_list = x.columns
    empty_list = []
    for y in column_list:
        column_data = x[y]
        if column_data is not None:
            empty_list.append(column_data.eq(' ').sum())

    return empty_list

def cero_list (x):
    column_list = x.columns
    cero_list = []
    for y in column_list:
        column_data = x[y]
        if column_data is not None:
            cero_list.append(column_data.eq('0').sum())

    return cero_list

def unique_values_list (x):
    column_list = x.columns
    unique_values = []
    for y in column_list:
        column_data = x[y]
        if column_data is not None:
            unique_values.append(column_data.unique().tolist())

    return unique_values

def numeric_list(x):
    column_list = x.columns
    result_list = []

    for y in column_list:
        try:
            is_numeric = pd.to_numeric(x[y], errors='coerce')  # Utiliza 'coerce' para convertir a NaN si no es numérico
            is_numeric = is_numeric.notnull().all()  # Verifica si todos los valores de la columna son numéricos
            result_list.append(is_numeric)  # Agrega el resultado a la lista
        except ValueError:
            result_list.append(False)  # Si hay un error, marca la columna como no numérica

    return result_list  # Devuelve la lista con valores True o False por columna

def letter_list (x):
    column_list = x.columns
    letter_list = []
    for y in column_list:
        column_data = x[y]
        if column_data is not None:
            letter_list.append(column_data.astype(str).apply(lambda x: x.replace(" ", "").isalpha()).all())

    return letter_list

def null_list (x):
    column_list = x.columns
    null_list = []
    for y in column_list:
        column_data = x[y]
        if column_data is not None:
            null_list.append(column_data.isnull().sum())

    return null_list