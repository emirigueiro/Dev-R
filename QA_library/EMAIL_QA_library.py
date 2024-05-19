import pandas as pd
import numpy as np
import re
import Common_fuctions_QA_library 

#Identifica si el nombre de la columna contiene la expresión regular "email|mail|correo"
def email_re(x):
    column_list = x.columns
    patron = re.compile(r"@", re.IGNORECASE)
    resultados = []   
    
    for y in column_list:
        if re.search(patron, str(y)): 
           resultados.append(True)
        else:
            resultados.append(False)
            
    return(resultados)

#Se cuentan cuantos "@" hay en cada columna
def email_count_arroba(x):
    column_list = x.columns
    patron = re.compile(r"@")
    resultados = []

    for y in column_list:
        column_data = x[y]
        count = sum(1 for value in column_data if re.search(patron, str(value)))
        resultados.append(count)
          
    return resultados


#Se divide la cantidad de "@" por la cantidad de registros para obtener el % de registros con @ por fila
def email_percent_arroba(x):
    email_percent_arroba_1 = []
    email_percent_arroba_2 = [] 
    [email_percent_arroba_1.append((x2 / x1)*100) for x1, x2 in zip(Common_fuctions_QA_library.count_list(x), email_count_arroba(x))]

    for x in email_percent_arroba_1:
       if x <= 100.0 and x >= 90.1:
           email_percent_arroba_2.append(0)
       elif x <= 90.0 and x >= 50.1:
           email_percent_arroba_2.append(1)
       elif x <= 50.0 and x >= 20.1:
           email_percent_arroba_2.append(2)
       elif x <= 20.0:
           email_percent_arroba_2.append(3)
       
    return email_percent_arroba_2


#Recorro todas las filas de todas las columnas y si encuentra alguno de los dominios (Hotmail, Gmail, Yahoo, etc.) en al menos una fila, marca esa columna con True.


def email_domain (x):
    column_list = x.columns
    patron = re.compile(r"Hotmail|Gmail|Yahoo|Outlook|Live|Icloud|Fastemail", re.IGNORECASE)
    resultados = []
    for y in column_list:
        column_data = x[y]
        if re.search(patron, str(column_data)): 
           resultados.append(True)
        else:
            resultados.append(False)
    return resultados

def email_probability(x):
   
   #Sumarizaciòn:
   final = pd.DataFrame()
   final['email_re'] = email_re(x) 
   final['email_percent_arroba'] = email_percent_arroba(x)
   final['email_domain'] = email_domain(x) 

   final_2 = []
   final_2 = final['email_re'] + final['email_percent_arroba'] + final['email_domain']

   #Construcciòn del calcuo de probabilidad
   email_probability = []
   for x in final_2:
       if x == 0:
           email_probability.append('100%')
       elif x == 1:
           email_probability.append('75%')
       elif x == 2:
           email_probability.append('50%')
       elif x >= 3:
           email_probability.append('0%')

   return email_probability