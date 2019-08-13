import pandas as pd

cars = pd.read_csv('files/cars.csv', index_col=0)
print(cars)


###Selección de una única dimension. Devuelve un tipo Series.
per_cap = cars['drives_right']
print(per_cap)

###De ahora en mas se seleccionan filas y columnas
##Selecciona columnas. En este caso al ser mar de una columna devueve un SubDataFame.
x1 = cars[['cars_per_cap', 'drives_right']]
print(x1)

##Selecciona filas
print('First 3')
x2 = cars[0:3]
print(x2)

print('3 in the middle')
print(cars[2:5])

print('Select row Japon')
x3 = cars.loc[['JP']]
print(x3)

print('Select Australia and Egypto')
print(cars.loc[['AU', 'IC']])

print('Select de algunas filas y algunas columnas')
subSelect = cars.loc[['AU', 'IC'],['country', 'drives_right']]
print(subSelect)

print('Select all the rows just for country and dives_right')
subSelect = cars.loc[:, ['country', 'drives_right']]


#seleccionar fila por indice
print(cars.iloc[2:3])