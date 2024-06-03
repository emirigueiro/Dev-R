import pandas as pd
import QA_library.primary_f as primary_f 

import pandas as pd

def date_count(df):
    column_list = df.columns
    resultados = []
    
    for col in column_list:
        valid_count = 0
        column_data = df[col]
        for value in column_data:
            try:
                pd.to_datetime(value)
                valid_count += 1
            except ValueError:
                continue
        resultados.append(valid_count)
    
    return resultados