import clickhouse_connect

# Conecciòn con la BBDD clickhouse
client = clickhouse_connect.get_client(host='h4ht169yky.us-central1.gcp.clickhouse.cloud', port=8443, username='default', password='_J8EZmEnKUcq0')

# Creaciòn de la estructura de la BBDD en clickhouse
client.command('CREATE TABLE dolar_act (fecha String, hora String, am_pm String, blue_compra Float64, oficial_compra Float64, bolsa_compra Float64, contado_liqui_compra Float64, crypto_compra Float64, blue_venta Float64, oficial_venta Float64, bolsa_venta Float64, contado_liqui_venta Float64, crypto_venta Float64, solidario_venta Float64) ENGINE MergeTree order by fecha')
               