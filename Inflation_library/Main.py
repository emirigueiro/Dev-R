# Ejecuciòn final
import ETL_Dolar as etl
import Insercion_BBDD as ins

ins.insercion_bbdd(etl.carga_inicial())