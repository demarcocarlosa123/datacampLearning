import pandas as pd

file = 'files/dob_job_application_filings_subset.csv'
df = pd.read_csv(file)

# Mostrar los primeros registros, sirve para tener un vistazo
print('Head: ')
print(df.head())

# Mostrar los último registros, sirve para tener un vistazo general
print('Tail: ')
print(df.tail())

# Mostrar las dimensiones del DF, usando el atributo shape
print('Shape:')
print(df.shape)

# Mostrar la lista de columnas.
# Sirve para revisar si hay algun problema con los encabezados como espacios etc
print('Columnas:')
print(df.columns)

# Genero un sub data set para jugar con el.
# Recordar que el doble corchete devuelve un DataFrame.
sub_df = df[['Job #', 'Doc #', 'Borough', 'Initial Cost', 'Total Est. Fee', 'Existing Zoning Sqft',
            'Proposed Zoning Sqft', 'Enlargement SQ Footage', 'Street Frontage',
            'ExistingNo. of Stories', 'Proposed No. of Stories', 'Existing Height', 'Proposed Height']]


print('-----------------------1')


# Uso el metodo info() para ver informacion general del Df.
# Muestra la cantidad de fila y columnas
# Muestra cantidad de non_missing data para cada columna
# Muestra el tipo de dato de cada columna. Si es object es porque no encontró un número
i = df.info()
print(type(i))
print(i)

print(sub_df.info())

print('-----------------------2')


### Para hacer un rápido analisis estadistico sobre los atributos numericos
### Se una la función describe() sobre un objeto DataFrame
subDFNumerico = df[['Proposed No. of Stories','Existing Height', 'Street Frontage', 'Proposed Height']]
i = subDFNumerico.describe()
print(type(i))
print(i)

print('-----------------------3')

### Para hacer un analisis rapido sobre atributos de texto se puede hacer un conteo por cada palabra diferente
### Para eso se usa el metodo value_counts() sobre un objeto del tipo Series
### Sirve para determinar los valores vacios o valores raros. 

subDFString = df['Borough']
print(type(subDFString))
print(subDFString.value_counts())

subDFString = df['Site Fill']
print(subDFString.value_counts(dropna=False))