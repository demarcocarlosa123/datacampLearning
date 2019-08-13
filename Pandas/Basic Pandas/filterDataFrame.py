import pandas as pd

cars = pd.read_csv('files/cars.csv', index_col=0)
print(cars)


#Paises que manejen por la derecha
dr = cars['drives_right']
print(type(dr))
print(dr)
print(cars[dr])

#Paises que tienen una cantidad de autos per capita mayor a 500
isCarsPerCapitaGrande = cars['cars_per_cap'] > 500
print(cars[isCarsPerCapitaGrande])
print(cars[cars['cars_per_cap'] > 500])

#Paises que tienen cantidad de autos per capita entre 100 y 500
import numpy as np
filtroBetween = np.logical_and(cars['cars_per_cap']>100, cars['cars_per_cap'] < 500)
print(cars[filtroBetween])
