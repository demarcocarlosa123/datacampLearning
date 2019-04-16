import numpy as np
import matplotlib.pyplot as plt


###Numpy es muy eficiente para trabajar con numeros. Por eso en general se usa.
###Tiene un par de metodos para cargar datos
file = 'files/seaslug.txt'

data = np.loadtxt(file, delimiter='\t', dtype=str)
#Imprimo la primera fila, o sea el header
print(data[0])

datosFloat = np.loadtxt(file, delimiter='\t', dtype=float, skiprows=1)
#Imprimo por ejemplo la fila 10
print(datosFloat[10])

#Imprimo las 10 primeras filas
print(data[0])
print(datosFloat[0:9])

#Vamos a visualizar la info en un scatter a ver como se realacionan los datos
plt.scatter(datosFloat[:, 0], datosFloat[:, 1])
plt.ylabel('percentage of larvae')
plt.xlabel('time (min.)')
plt.show()



###Ahora vamos a cargar un archivo con multiples tipos de datos, np.genfromtxt
###Como dijimos antes si hay multiples tipos de datos, conviene usar pandas.

#names = True, significa que el csv tiene un header,
#dtype = None, significa que tiene multiple tipos de datos el archivo
file = 'files/titanic_sub.csv'
dataMixta = np.genfromtxt(file, delimiter=',', names=True, dtype=None)
print(np.shape(dataMixta))

#Columna de nombre Fare, larguisima
print(dataMixta['Fare'])

#Fila numero 10
print(dataMixta[9])

###Ahora vamos a cargar un archivo con multiples tipos de datos, np.recfromcsv()
# ya tiene por default delimiter=',', names=True, dtype=None
dataMixta = np.recfromcsv(file)
#Columna de nombre Fare, larguisima
print(dataMixta['Fare'])

#Fila numero 10
print(dataMixta[9])



