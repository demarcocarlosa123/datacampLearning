import pandas as pd

### Para unir 3 archivos con la misma aridad se usa concat()
### Funciona como un UNION ALL en sql
uber1 = pd.read_csv('files/uber1.csv', sep=';')
uber2 = pd.read_csv('files/uber2.csv', sep=';')
uber3 = pd.read_csv('files/uber3.csv', sep=';')

print('uber1 shape:', uber1.shape)
print('uber2 shape:', uber2.shape)
print('uber3 shape:', uber3.shape)

concatenated = pd.concat([uber1, uber2, uber3])
print('concatenated shape:', concatenated.shape)

print(concatenated.head())


print('--------------------1')
### Para adicionar un DF a la derecha de otro, tambien se usa concat.
### hay que pasarle el parámetro axis=1.

a = pd.read_csv('files/ebola2CombineA.csv', sep=';')
b = pd.read_csv('files/ebola2CombineB.csv', sep=';')
print('a shape:', a.shape)
print('a columns:', a.columns)
print('b shape:', b.shape)
print('b columns:', b.columns)

combined = pd.concat([a, b], axis=1)
print('combined shape:', combined.shape)
print(combined.head())

print('-----------------------2')
### Para buscar archivos en un directorio
import glob

pattern = 'files/uber?.csv'
csvFiles = glob.glob(pattern)
print(type(csvFiles))
print('cantidad encontrada:', len(csvFiles))
print(csvFiles)

uber = pd.read_csv(csvFiles[-1], sep=';')
print(uber.head())


print('-----------------------3')
### Muchas veces pasa que los archivos se generan por ejemplo una vez por dias.
### Entonces para compilarlos en uno es conveniente levantarlos todos desde el
### FileSystem automaticamente y combinarlos.

dfs = []
for filename in csvFiles:
    df = pd.read_csv(filename, sep=';')
    print(filename, 'shape:',  df.shape)
    dfs.append(df)

combinado = pd.concat(dfs)
print('Combinado shape:', combinado.shape)

print('--------------4')

### Para joinear DataFrames se usa merge()
### Es igual al JOIN en sql

site = pd.read_csv('files/site.csv', sep=';')
print('site:')
print(site)
visited = pd.read_csv('files/visited.csv', sep=';')
print('visited:')
print(visited)

joined = pd.merge(left=site, right=visited, left_on='name', right_on='site')
print('joined:')
print(joined)







