import pandas as pd
from prettytable import PrettyTable

import id_f as id_f
import email_f as email_f
import primary_f as primary_f

#This function is the main one, it takes the fuctions primary_f, email_f, id_f and combines them in a data frame 
def dataprofile_fuction (x):

    profile_date =                     pd.DataFrame(columns=['columns'])
    profile_date['columns'] =          pd.Series(primary_f.column_list(x))
    profile_date['count'] =            pd.Series(primary_f.r_count(x))
    profile_date['unique'] =           pd.Series(primary_f.r_count_distinct(x))
    profile_date['unique_%'] =         pd.Series(primary_f.r_count_distinct_percent(x))
    profile_date['id_probabilty'] =    pd.Series(id_f.id_probability(x))
    profile_date['email_probabilty'] = pd.Series(email_f.email_probability(x))
    profile_date['duplicate'] =        profile_date['count'] - profile_date['unique']
    profile_date['numeric'] =          pd.Series(primary_f.is_numeric(x))
    profile_date['letter'] =           pd.Series(primary_f.is_letter(x))
    profile_date['bool'] =             pd.Series(primary_f.is_bool(x))
    profile_date['empty'] =            pd.Series(primary_f.r_empty(x))
    profile_date['empty_%'] =          pd.Series(primary_f.empty_percent(x))
    profile_date['cero'] =             pd.Series(primary_f.r_cero(x))
    profile_date['cero_%'] =           pd.Series(primary_f.r_cero_percent(x))
    profile_date['null'] =             pd.Series(primary_f.is_null(x))
    profile_date['null_%'] =           pd.Series(primary_f.is_null_percent(x))

    x = PrettyTable()
    x.field_names = profile_date.columns.tolist()
    for row in profile_date.itertuples(index=False):
        x.add_row(row)

    return x

#With this fuction first validate if the input source is a Dataframe, then execute the dataprofile_fuction
def dataprofile (x):
    try:
        # Verificar si es un DataFrame
        if isinstance(x, pd.DataFrame):
            return dataprofile_fuction (x)
        else:
            return "The file is not a DataFrame."
    except Exception as e:
       
        return f"Error: {e}. The file is not a DataFrame."