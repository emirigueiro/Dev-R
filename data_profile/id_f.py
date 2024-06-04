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
   #Replace True for 1, and Flase for 0. This is necessary for the posterirory probability calculation
   id_re = [0 if x == True else 1 for x in (id_list(x))]
   
   #This part of the process identify the columns that contain the same number of unique and duplicate records
   unique_and_distincts = []

   count_rows = (primary_f.r_count(x))
   count_distinct_rows = (primary_f.r_count_distinct(x))
   
   for x1, x2 in zip(count_rows, count_distinct_rows):
      if x1 != x2:
         unique_and_distincts.append(1)
      elif x1 == x2:
         unique_and_distincts.append(0)

   #Replace True for 1, and Flase for 0. This is necessary for the posterirory probability calculation
   empty_rows = [1 if x > 0 else 0 for x in (primary_f.r_empty(x))]

   #Replace True for 1, and Flase for 0. This is necessary for the posterirory probability calculation
   null_rows = [1 if x > 0 else 0 for x in (primary_f.is_null(x))]

   #Asing a number on each column in order to the subsequent probability calculation
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

   #Sumarization
   final = pd.DataFrame()
   final['id_re'] = id_re 
   final['unique_and_distincts'] = unique_and_distincts
   final['empty_rows'] = empty_rows
   final['null_rows'] = null_rows
   final['percent_unique'] = percent_unique_2
  
   final_2 = []
   final_2 = final['id_re'] + final['unique_and_distincts'] + final['empty_rows'] + final['null_rows'] + final['percent_unique']
   
   #Assign the ID probability for each column 
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