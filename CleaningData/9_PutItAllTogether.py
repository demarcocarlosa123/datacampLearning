import pandas as pd

gap = pd.read_csv('files/gapminder.csv')
print('Head:')
print(gap.head())

print('Tail:')
print(gap.tail())


print('Info:')
print(gap.info())

# Para ver la calidad de los datos, vamos a comparar los dos años mas extremos.
# Como podremos ver, hay muchos paises para los cuales la data no cambia entre un extremo y otro.
# En este contexto es raro pensar que no hubo cambios en la población, asi que pueden ser datos copiados a mano.
import matplotlib.pyplot as plt

# Create the scatter plot
gap.plot(kind='scatter', x='1800', y='1899')

# Specify axis labels
plt.xlabel('Life Expectancy in 1800')
plt.ylabel('Life Expectancy in 1899')

# Specify axis limits
plt.xlim(20, 55)
plt.ylim(20, 55)

# Display the plot
#plt.show()


### Antes de seguir es importante verificar las siguientes cosas sobre la data:
### - 'Life Expectancy' es la ultima columna del DF.
### - las otras columnas contienen null o numeric values
### - Todos hay valores numericos negativos
### - Los paises aparecen solo una vez

def check_null_or_valid(row_data):
    """Function that takes a row of data,
    drops all missing values,
    and checks if all remaining values are greater than or equal to 0
    """
    no_na = row_data.dropna()
    numeric = pd.to_numeric(no_na)
    ge0 = numeric >= 0
    return ge0

# Chequeo que la ultima columna es 'Life expectancy'. Recordar que no vale ver el excel para analizar eso.
assert gap.columns[-1] == 'Life expectancy'


# Check whether the values in the row are valid
# Recordar que el primer parametro de iloc sobre una matriz hace refencia al rango de las filas (Y),
# y el segundo parametro representa el rango de columnas. En este caso no queremos ni la primera columna, ni la ultima que tiene valores String.
dfNumerico = gap.iloc[:, 1:-1]
assert dfNumerico.apply(check_null_or_valid, axis=1).all().all()



#print(gap['Life expectancy'])
### El data frame original tiene el problema que los paises aparecen 3 veces. Porque?
### Porque para un mismo pais se cargaron los datos de siglos difentes en diferentes filas, y donde no hay dato hay NA
### Entonces hay procesar la data para desduplicar este DF.
gapW = gap.iloc[:, 1:101]
gapZ = gap.iloc[:, -1:]
gapA = pd.concat([gapW, gapZ], axis=1)
gapA = gapA.dropna()

gapX = gap.iloc[:, 101:201]
gapZ = gap.iloc[:, -1:]
gapB = pd.concat([gapX, gapZ], axis=1)
gapB = gapB.dropna()

gapC = gap.iloc[:, 201:]
gapC = gapC.dropna()

temp = pd.merge(left=gapA, right=gapB, left_on='Life expectancy', right_on='Life expectancy')
gap = pd.merge(left=temp, right=gapC, left_on='Life expectancy', right_on='Life expectancy')

print(gap['Life expectancy'].value_counts())




# Check that there is only one instance of each country
#index 0 of .value_counts() will contain the most frequently occuring value.
assert gap['Life expectancy'].value_counts()[0] == 1
