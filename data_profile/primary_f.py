#This section contain all the common fuction in order to create a final profile date analysis. 
#Exist other specificts sections for: email and id. 

import pandas as pd

#Creates a list with the columns names
def column_list (x):
    columns_list = []
    columns_list = x.columns
    return columns_list

#---------------------------------------------------------------------------------------------------------------------------

#Creates a list with the records count for each column
def r_count(x):
    return [x[y].count() for y in x.columns if x[y].notna().any()]

#---------------------------------------------------------------------------------------------------------------------------

#Creates a list with the distinct records count for each column
def get_valid_columns(x):
    # Obtener las columnas donde al menos un valor no es NaN
    return [col for col in x.columns if x[col].notna().any()]

def r_count(x):
    return [x[y].shape[0] for y in x.columns]

def r_count_distinct(x):
    valid_columns = get_valid_columns(x)
    return [x[col].nunique() for col in valid_columns]

def r_count_distinct_percent(x):
    count_rows = r_count(x)
    count_distinct_rows = r_count_distinct(x)

    unique_percent = []
    for x1, x2 in zip(count_rows, count_distinct_rows):
        if x1 != 0:  # Evitar división por cero
            unique_percent.append(f"{int((x2 / x1) * 100)}%")
        else:
            unique_percent.append("0%")
    return unique_percent

#---------------------------------------------------------------------------------------------------------------------------

#Creates a list with the empty record count for each column 
def r_empty(x):
    return [x[y].eq(' ').sum() for y in x.columns if x[y] is not None]

def empty_percent (x):
    empty_percent = []
    [empty_percent.append(f"{int((x2 / x1)*100)}%") for x1, x2 in zip(r_count(x), r_empty(x))]
    return empty_percent

#---------------------------------------------------------------------------------------------------------------------------

#Creates a list with the count of records that contains value 0 for each column
def r_cero(x):
    return [x[y].eq(' ').eq('0').sum() for y in x.columns]

def r_cero_percent (x):
    cero_percent = []
    [cero_percent.append(f"{int((x2 / x1)*100)}%") for x1, x2 in zip(r_count(x), r_cero(x))]
    return cero_percent

#---------------------------------------------------------------------------------------------------------------------------

#Validates whether all records in the columns are numeric and returns a list with all the results
def is_numeric(x):
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

#---------------------------------------------------------------------------------------------------------------------------

#Validates whether all records in the columns are letter and returns a list with all the results
def is_letter(x):
    return [x[y].astype(str).apply(lambda x: x.replace(" ", "").isalpha()).all() for y in x.columns if x[y] is not None]

#---------------------------------------------------------------------------------------------------------------------------

#Creates a list with the count of null recors for each column
def is_null(x):
    return [x[y].isnull().sum() for y in x.columns if x[y] is not None]

def is_null_percent (x):
    null_percent = []
    [null_percent.append(f"{int((x2 / x1)*100)}%") for x1, x2 in zip(r_count(x), is_null(x))]
    return null_percent

#---------------------------------------------------------------------------------------------------------------------------

#Identified if the column date type is bool.There may be empty or null records.

def is_bool(x):
    column_list = x.columns
    unique_list = []
    boolean_list = []    
    for y in column_list:
        column_data = x[y]
        if column_data is not None:
            unique_list.append(column_data.nunique())

    for x in unique_list:
        if x == 2:
           boolean_list.append(True)         
        else: 
           boolean_list.append(False)

    return boolean_list

#---------------------------------------------------------------------------------------------------------------------------