def carga_inicial(): 
  
  from bs4 import BeautifulSoup
  import pandas as pd
  import requests
  import re
  import lxml
  
   
  web = 'https://dolarhoy.com/'
  response = requests.get(web)
  content = response.text
    
  soup = BeautifulSoup(content, 'html.parser')
    
  dolares = soup.find('div', class_="tile is-parent is-7 is-vertical")
  dolares = (dolares).get_text()
    
  fecha = soup.find('div', class_="tile update")
  fecha = (fecha).get_text()
    
  dolares_split = dolares.split(" ")
  dolares_list = dolares_split
    
     
  def captura_compra(tipo_dolar):
      result = re.search("compra(.*?)venta", tipo_dolar, re.DOTALL | re.IGNORECASE)
      tipo_dolar = result.group(1)
      tipo_dolar = float(tipo_dolar.replace('$', "")) 
      return tipo_dolar
    
  def captura_venta(tipo_dolar):
      result = re.search("Venta(.*?)Dólar", tipo_dolar, re.DOTALL | re.IGNORECASE)
      tipo_dolar= result.group(1)
      tipo_dolar = float(tipo_dolar.replace('$', "")) 
      return tipo_dolar
    
  def captura_venta_1(tipo_dolar):
      result = re.search("Venta(.*?)Contado", tipo_dolar, re.DOTALL | re.IGNORECASE)
      tipo_dolar= result.group(1)
      tipo_dolar = float(tipo_dolar.replace('$', "")) 
      return tipo_dolar
    
  def captura_venta_2(tipo_dolar):
      result = re.search("Venta(.*?)Publicá", tipo_dolar, re.DOTALL | re.IGNORECASE)
      tipo_dolar= result.group(1)
      tipo_dolar = float(tipo_dolar.replace('$', "")) 
      return tipo_dolar
   
  def captura_fecha(tipo_dolar):
      result = re.search("el(.*?)m", tipo_dolar, re.DOTALL | re.IGNORECASE)
      tipo_dolar= result.group(1)
      return tipo_dolar
      
  # Creacion de valores de venta
  blue_compra = captura_compra(dolares_list[1])
  oficial_compra = captura_compra(dolares_list[3])
  bolsa_compra = captura_compra(dolares_list[4])
  contado_liqui_compra = captura_compra(dolares_list[6])
  crypto_compra = captura_compra(dolares_list[7])

  # Creacion de valores de venta
  blue_venta = captura_venta(dolares_list[1])
  oficial_venta = captura_venta(dolares_list[3])
  bolsa_venta = captura_venta_1(dolares_list[4])
  contado_liqui_venta = captura_venta(dolares_list[6])
  crypto_venta = captura_venta(dolares_list[7])
  solidario_venta = captura_venta_2(dolares_list[8])
  
  # Limpieza fecha
  fecha = captura_fecha(fecha)
  fecha_split = fecha.split( )
  fecha = fecha_split[0]
  hora = fecha_split[1]
  am_pm = fecha_split[2]

  return fecha, hora, am_pm, blue_compra, oficial_compra, bolsa_compra, contado_liqui_compra, crypto_compra, blue_venta, oficial_venta, bolsa_venta, contado_liqui_venta, crypto_venta, solidario_venta
