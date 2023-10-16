def insercion_bbdd(x):

   import clickhouse_connect
    
   # Creaciòn de la lista a insertar
   
   list_insert = list(x)
   list_insert_1 = [list_insert]
   
   # Credenciales cliente clickhouse
   client = clickhouse_connect.get_client(host='h4ht169yky.us-central1.gcp.clickhouse.cloud', port=8443, username='default', password='_J8EZmEnKUcq0')

   # Inserciòn en la BBDD 
   client.insert('dolar_act', list_insert_1, column_names=['fecha', 'hora', 'am_pm', 'blue_compra', 'oficial_compra', 'bolsa_compra', 'contado_liqui_compra', 'crypto_compra', 'blue_venta', 'oficial_venta', 'bolsa_venta', 'contado_liqui_venta', 'crypto_venta', 'solidario_venta'])