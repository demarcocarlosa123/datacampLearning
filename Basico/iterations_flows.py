# Un while basico
offset = -6
while offset != 0 :
    print('entro')
    if offset > 0 :
        offset = offset - 1
    else :
        offset = offset + 1

# Un for basico sobre lista
areas = [11.25, 18.0, 20.0, 10.75, 9.50]
for elemento in areas:
    print(elemento)

# Un for con info del indice
for index, element in enumerate(areas):
    print("Room " + str(index) + ": " + str(element) )

# Un for sobre lista de lista
house = [["hallway", 11.25],
         ["kitchen", 18.0],
         ["living room", 20.0],
         ["bedroom", 10.75],
         ["bathroom", 9.50]]

for elemento in house:
    print(elemento[0] + " tiene: " + str(elemento[1]) + "m2")

# Un for sobre Diccionarios
europe = {'spain':'madrid',
          'france':'paris',
          'germany':'bonn',
          'norway':'oslo',
          'italy':'rome',
          'poland':'warsaw',
          'australia':'vienna'
          }
for key, value in europe.items():
    print("La capital de " + key + " es " + value)


# Un for sobre numpy
import numpy as np

peso_kg = np.array([90, 89, 120, 95, 105])
altura_m = np.array([1.90, 1.95, 2.10, 1.92, 2.01])

basket = ([90, 89, 120, 95, 105],
          [1.90, 1.95, 2.10, 1.92, 2.01])

for peso in peso_kg:
    print (peso)

#Un for sobre un numpay array 2D
for element in np.nditer(basket):
    print(str(element))

#Un for sobre un panda
import pandas as pd

#Un for sobre un pandas basico
import pandas as pd
cars = pd.read_csv('cars.csv', index_col=0)

for primary_key, fila in cars.iterrows():
    print(primary_key)
    print(fila)

#Un for sobre un panda con un campo filtrado
for pk, fila in cars.iterrows():
    print(pk + ": " + str(fila['cars_per_cap']) )

#Un for sobre un DataFame y agregado de una columna.
#loc[] agrega un campo nuevo en el objeto Series, cuando matchea el indice.
for pk, fila in cars.iterrows():
    pais_minuscula = fila["country"]
    cars.loc[pk, "COUNTRY"] = pais_minuscula.upper()

#Una forma eficiente de agregar campos calculados al DataFrame
def porMil(x):
    return x*1000
cars["COUNTRY2"] = cars["country"].apply(str.upper)
cars["CPC_in_miles"] = cars["cars_per_cap"].apply(porMil)
print(cars)