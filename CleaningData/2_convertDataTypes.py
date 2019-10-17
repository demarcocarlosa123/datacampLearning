import pandas as pd

tips = pd.read_csv('files/tips.csv')
print(tips.info())

### Hay columnas que pueden ser convertidas a CATEGORIAS.
### Hacerlo ahorra memoria.
### Se debe aplicar sobre un str la funcion astype('category')

tips.sex = tips.sex.astype('category')
tips.smoker = tips.smoker.astype('category')
print(tips.info())



print('---------------------1')
### Cuando vemos que hay campos que deben figurar como numericos (int o float),
### pero aparecen como object (string en python), sifnifica que hay data corrupta.
### entonces o exploramos la data a ver que onda, o forzamos a que sea numerico.

bad = pd.read_csv('files/tipsBad.csv', sep=';')
print(bad.info())
print(bad.head(10))

bad['total_bill'] = pd.to_numeric(bad['total_bill'], errors='coerce')
bad.tip = pd.to_numeric(bad.tip, errors='coerce')
print(bad.info())
print(bad.head(10))

