import pandas as pd
import numpy as np
import re
import primary_f as primary_f 

#Indentify of the column name cotain this regular expresion: "ID"
def id_list(x):
    column_list = x.columns
    patron = re.compile(r"id", re.IGNORECASE)
    resultados = []   
    
    for y in column_list:
        if re.search(patron, str(y)): 
           resultados.append(True)
        else:
            resultados.append(False)
            
    return(resultados)

#In this fuction creates the ID probability for each column
def id_probability(x):
    # Replace True for 1, and False for 0. This is necessary for the posterior probability calculation
    id_re = [0 if is_id else 1 for is_id in id_list(x)]
    
    # Initialize lists
    unique_and_distincts = []
    count_rows = primary_f.r_count(x)
    count_distinct_rows = primary_f.r_count_distinct(x)
       
    for x1, x2 in zip(count_rows, count_distinct_rows):
        unique_and_distincts.append(1 if x1 != x2 else 0)

    # Reemplazar True por 1 y False por 0
    empty_rows = [1 if count > 0 else 0 for count in primary_f.r_empty(x)]
    null_rows = [1 if count > 0 else 0 for count in primary_f.is_null(x)]
    
    # Asignar números a cada columna
    percent_unique_1 = [(x2 / x1 * 100) if x1 > 0 else 0 for x1, x2 in zip(count_rows, count_distinct_rows)]
    
    percent_unique_2 = []
    for x in percent_unique_1:
        if 90.1 <= x <= 100.0:
            percent_unique_2.append(0)
        elif 50.1 <= x <= 90.0:
            percent_unique_2.append(1)
        elif 20.1 <= x <= 50.0:
            percent_unique_2.append(2)
        else:
            percent_unique_2.append(3)

    # Crear DataFrame
    final = pd.DataFrame({
        'id_re': id_re,
        'unique_and_distincts': unique_and_distincts,
        'empty_rows': empty_rows,
        'null_rows': null_rows,
        'percent_unique': percent_unique_2
    })

    # Sumarización
    final_2 = final.sum(axis=1)  # Suma por fila
    id_quality = ['100%' if x == 0 else '75%' if x == 1 else '50%' if x == 2 else '0%' for x in final_2]

    return id_quality
