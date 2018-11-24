import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

productosPD = pd.read_csv('data_lake_redshift_producto.csv')
fechasVentas = productosPD[["transaction_code", "fecha_emision", "fecha_checkin"]]
fechasVentas["transaction_code"] = fechasVentas.transaction_code.astype(int)
fechasVentas["fecha_emision"] = fechasVentas.fecha_emision.astype()
fechasVentas.set_index("transaction_code")
print(fechasVentas.dtypes)

encuestasPD = pd.read_csv("sherman_survey_20180623.csv", low_memory=False)

fechaEncuestas = encuestasPD[["transaction_id", "review_type", "product_code", "date_long"]]
fechaEncuestas = fechaEncuestas[fechaEncuestas["review_type"] == "CHANGE_FLIGHT"]
fechaEncuestas["transaction_id"] = fechaEncuestas.transaction_id.astype(int)
fechaEncuestas.set_index("transaction_id")
print(fechaEncuestas.dtypes)