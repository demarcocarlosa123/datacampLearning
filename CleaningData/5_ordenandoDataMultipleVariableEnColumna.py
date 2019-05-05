import pandas as pd

tuberculosis = pd.read_csv('files/tb.csv', sep=',')

print(tuberculosis.head())
# El problema con este archivo es que mezcla en diferentes campos el sexo y los rangos de edades.



meltedTb = tuberculosis.melt(id_vars=['country', 'year'])
print('Melted:')
print(meltedTb.head())


meltedTb['sex'] = meltedTb.variable.str[0]
meltedTb['ageRange'] = meltedTb.variable.str[1:]

print('Descomponiendo sex de rangoFechas:')
print(meltedTb.head())

print('------------------1')
### El archivo tiene columnas que mezcla en una misma columna la cantidad de casos o muertes con el pais.
ebola = pd.read_csv('files/ebola.csv')
print('Ebola')
print(ebola.head())

meltedEbola = pd.melt(ebola,id_vars=['Date', 'Day'], var_name='tipo_pais', value_name='cantidad')
print('Melted Ebola:')
print(meltedEbola.head())

meltedEbola['str_split'] = meltedEbola.tipo_pais.str.split('-')
print('Melted regenerado:')

meltedEbola['tipo'] = meltedEbola.str_split.str.get(0)
meltedEbola['pais'] = meltedEbola.str_split.str.get(1)

print(meltedEbola.head())
