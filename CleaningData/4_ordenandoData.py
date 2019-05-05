### Para que la data este ORDENADA esta debe:
#   - Cada variable tiene que estar representada en una columna diferente
#   - Cada observación tiene que estar representada por una fila diferente

import pandas as pd

tidyInformation = pd.read_csv('files/solarRadiation.csv', sep=';')
notTidyInformation = pd.read_csv('files/ozoneAndTemperature.csv', sep=';')

# Reviso la cabeza y la cola de cada df
# Y a simple vista se concluye que ozono no esta ordenado.
# Para que este ordenada deberia existir una columna Ozono, y otra Temp
print('Tidy:')
print(tidyInformation.head())
print(tidyInformation.tail())
print('notTidy:')
print(notTidyInformation.head())
print(notTidyInformation.tail())



### En el caso que necesite que diferentes variables separadas en diferentes columnas
### terminen en la misma columna se usa pd.melt(id_vars=[], value_vars=[])
### melt() = combina columnas en filas
### id_vars debe ser la lista de las columnas que no queremos fundir.
### value_vars debe ser la lista de columnas que queremos fundir.
print('---------------- 1')
print(tidyInformation.head())
meltedInformation = tidyInformation.melt(id_vars=['Month', 'Day'], value_vars=['Ozone', 'Solar.R', 'Wind', 'Temp'])
print(meltedInformation)
#Notar que python invento el nombre de las dos columnas: "variable" y "value"

### Ahora para mejorar lo anterior yo especifico nombres con sentido para las columnas melteadas
print('---------------- 2')
# Print the head of airquality
print(tidyInformation.head())

# Melt airquality: airquality_melt
airquality_melt = pd.melt(tidyInformation, id_vars=['Month', 'Day'], var_name='measurement', value_name='reading')

# Print the head of airquality_melt
print(airquality_melt.head())



### Se una PIVOT() para transformar valores unicos en columnas separadas.
### Se usa por ejemplo cuando la data viola el principio de ordenamiento:
### - Cada variable tiene que estar representada en una columna diferente
print('---------------- 3')
print('airquality_melt:')
print(airquality_melt.head())

pivoted = airquality_melt.pivot_table(values='reading', index=['Month', 'Day'], columns='measurement')
print('Pivoted:')
print(pivoted.head())

# Ojo que esta forma no reconstruye el indice completo. Month no figura en todas las filas por ser el mismo.
print('index:')
print(pivoted.index)

pivoted_reindexed = pivoted.reset_index()
print('re indexed:')
print(pivoted_reindexed.index)
print('Pivoted re indexed:')
print(pivoted_reindexed.head())


print('---------------- 4')
### Tambien como en cualquier tabla dinamica, para la variable valores se puede usar
### funciones agregadas para desduplicar filas.

import numpy as np

duplicated = pd.read_csv('files/meltedDuplicated2.csv', sep=';')
print(duplicated.head())

pivoted_mean = duplicated.pivot_table(values='reading', index=['Month', 'Day'], columns='measurement', aggfunc=np.mean)
pivoted_mean = pivoted_mean.reset_index()
print(pivoted_mean.head())

