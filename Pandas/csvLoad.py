import pandas as pd

cars = pd.read_csv('cars.csv', index_col=0)
print(cars)

##Selecciona columnas
print (cars[['cars_per_cap', 'drives_right']])

##Selecciona filas
print('First 3')
print(cars[0:3])

print('3 in the middle')
print(cars[2:5])

print('Select row Japon')
print(cars.loc[['JP']])

print('Select Australia and Egypto')
print(cars.loc[['AU', 'IC']])

print('Select de algunas filas y algunas columnas')
subSelect = cars.loc[['AU', 'IC'],['country', 'drives_right']]
print(subSelect)

print('Select all the rows of for country and dives_right')
subSelect = cars.loc[:, ['country', 'drives_right']]