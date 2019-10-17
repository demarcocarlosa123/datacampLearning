### Duplicate data genera varios problemas:
### - uso innecesario de memerioa
### - Puede modificar el resultado del analisis.
import pandas as pd


dup = pd.read_csv('files/billboardDuplicated.csv', sep=';')
print(dup.head())
print('Info:')
print(dup.info())

tracks = dup['track']
print('Count Tracks:')
y = tracks.value_counts()
print('Hay ', len(y), 'registros distintos')

desdup = dup.drop_duplicates()
print('Info Desdup:')
print(desdup.info())



print('-------------------1')
### Es importante lidear con Datos Faltantes, porque a veces ciertos calculos no se pueden hacer con faltantes
### Por default SALTEAR los missing values.
### Analizar cuanta data faltante hay y de donde proviene es crucial hacer interpretaciones parciales

file = 'files/airquality.csv'
air = pd.read_csv(file)
air2 = pd.read_csv(file)
#vemos que las dos primeras columnas tienen faltantes de datos

print(air.info())

promedioOzono = air['Ozone'].mean()
medianaSolarR = air['Solar.R'].median()

air['Ozone'] = air.Ozone.fillna(promedioOzono)
air['Solar.R'] = air['Solar.R'].fillna(medianaSolarR)
print('Habiendo rellenado:')
print(air.info())
print(air.head(50))


print('------------------------2')
### Se pueden definir test reutilizables para saber por ejemplo si hay información faltante.
### Esto es conveniente porque pueden venir lotes de datos nuevos para procesar.
ebola = pd.read_csv('files/ebola.csv')


assert air2.notnull().all().all()
assert air.notnull().all().all()