import pandas as pd

file='files/messy_stock_data.tsv.txt'
stockDataDF = pd.read_csv(file)
print(stockDataDF)


### El anterior archivo tiene 3 desafios.
# a. esta separado por TABs
# b. Tiene  comentarios intercalados entre la data
# c. Recien la tercera fila tiene los titulos de los campos.
# El ejercicio leer el archivo y al mismo tiempo saltear los 3 obstaculos.


stockDataDF = pd.read_csv(file, comment='#', header=3, delimiter=' ')
print(stockDataDF)



