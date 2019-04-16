from urllib.request import urlretrieve
import pandas as pd
import matplotlib.pyplot as plt


####Lo que vamos a hacer es descargar desde un sitio de internet al disco local, para despues usarlo
url = 'https://s3.amazonaws.com/assets.datacamp.com/production/course_1606/datasets/winequality-red.csv'
filename = '../files/winequality-red.csv'
urlretrieve(url, filename)

#Ahora lo uso
df = pd.read_csv(filename, sep=';')
print(df.head())


print('----------------------')

#####Procesar un csv de la web pero sin descargarlo, usando la funcion nativa read_csv
df = pd.read_csv(url, sep=';')
print(df.head())

print('doble[[]]', type(df[['fixed acidity']]))
print('simple []', type(df['fixed acidity']))

pd.DataFrame.hist(df[['fixed acidity']])
plt.xlabel('fixed acidity (g(tartaric acid)/dm$^3$)')
plt.ylabel('count')
plt.show()

print('----------------------')
##### Procesamos un XLS desde la web.
url = 'http://s3.amazonaws.com/assets.datacamp.com/course/importing_data_into_r/latitude.xls'
df = pd.read_excel(url, None) #El None es para traer todas las hojas del excel

#Emprimir los nobres de las hojas
print(df.keys())

#Imprimer head() de la primera hoja, usando el nombre de la primera hoja.
print(df['1700'].head())
