import pandas as pd
import numpy as np
import re
import Common_fuctions_QA_library 

#Identifica si el nombre de la columna contiene la expresión regular "id/ID"

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

def id_probability(x):
   #Tranforma el True por 1 y False por 0, sobre el return de la funciòn id_list:
   id_re = [0 if x == True else 1 for x in (id_list(x))]
   
   #Identifica aquellas columnas que cuentan con la misma cantidad de registros ùnicos y distinto:
   unique_and_distincts = []

   count_rows = (Common_fuctions_QA_library.count_list(x))
   count_distinct_rows = (Common_fuctions_QA_library.unique_list(x))
   
   for x1, x2 in zip(count_rows, count_distinct_rows):
      if x1 != x2:
         unique_and_distincts.append(1)
      elif x1 == x2:
         unique_and_distincts.append(0)

   #Utiliza la funciòn empty_list para identifica aquellas columnas que cuentan con valores vacios y reemplaza Ture x 1 y False x 0:
   empty_rows = [1 if x > 0 else 0 for x in (Common_fuctions_QA_library.empty_list(x))]

   #Utiliza la funciòn  null_list para identifica aquellas columnas que cuentan con valores nulos y reemplaza Ture x 1 y False x 0:
   null_rows = [1 if x > 0 else 0 for x in (Common_fuctions_QA_library.null_list(x))]

   #Creacion variable % de unicos:
   percent_unique_1 = []
   percent_unique_2 = [] 
   [percent_unique_1.append((x2 / x1)*100) for x1, x2 in zip(count_rows, count_distinct_rows)]
   
   for x in percent_unique_1:
       if x <= 100.0 and x >= 90.1:
           percent_unique_2.append(0)
       elif x <= 90.0 and x >= 50.1:
           percent_unique_2.append(1)
       elif x <= 50.0 and x >= 20.1:
           percent_unique_2.append(2)
       elif x <= 20.0:
           percent_unique_2.append(3)

   #Sumarizaciòn:
   final = pd.DataFrame()
   final['id_re'] = id_re 
   final['unique_and_distincts'] = unique_and_distincts
   final['empty_rows'] = empty_rows
   final['null_rows'] = null_rows
   final['percent_unique'] = percent_unique_2
  
   final_2 = []
   final_2 = final['id_re'] + final['unique_and_distincts'] + final['empty_rows'] + final['null_rows'] + final['percent_unique']
   
   #Construcciòn del calcuo de probabilidad
   id_quality = []
   for x in final_2:
       if x == 0:
           id_quality.append('100%')
       elif x == 1:
           id_quality.append('75%')
       elif x == 2:
           id_quality.append('50%')
       elif x >= 3:
           id_quality.append('0%')

   return id_quality