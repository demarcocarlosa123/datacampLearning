import pandas as pd

### A partir de tener listas, con series de datos. Se arma una lista de listas, los zipeamos con otra lista de
### Headers, usamos ese objeto zipeado para crear un Diccionario, y el Diccionario para crear un DataFrame.
labels = ['pais', 'poblacion']
pais = ['argentina', 'uruguay', 'chile']
poblacion = [40, 5, 10]

lista_values = [pais, poblacion]

## Armo una lista de tupas
zipped = list(zip(labels, lista_values))

## armo dicionario a partir del zipperd
dic = dict(zipped)
print(dic)
## finalmente armo el dataframe.

frame = pd.DataFrame(dic)

print(frame)

print('----------------------------------------------1')

### Tambien podemos cambiar el nombre a un DataFrame
nuevosLabels = ['country', 'population']
frame.columns = nuevosLabels
print(frame)


print('----------------------------------------------2')
### En la contrucción de DF podemos usar la función broadcasting,
# para evitar armar una lista con datos repetidos.
# Para eso en la uno de las claves en vez de poner una lista como valor,
# ponemos solo un dato. Este se va broadcastear
# para todos las filas del dataFrame.
partidosDic = {'partido': ['San Martin', 'Vicente  Lopez', 'La matanza'], 'provincia': 'BUE'}
partidosFG = pd.DataFrame(partidosDic)
print(partidosFG.head())