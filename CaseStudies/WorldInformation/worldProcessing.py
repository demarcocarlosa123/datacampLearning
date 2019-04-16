def list2Dict(lista1, lista2):
    """A partir de dos listas, devuelve un diccionario"""
    zipped = zip(lista1, lista2)
    map = dict(zipped)
    return map


#Abrir una archivo para leerlo linea a linea.
#Para saber cuantas veces si repite cada pais en el archivo en las primeras 1000 lineas
with open('world_ind_pop_data.csv') as file:
    #leo la primera linea de los headears, en este ejercicio quiero loopear sobre las tuplas directamente
    file.readline()

    count_group_by_contry = {}

    for j in range(1000):
        #separo las palablras por coma
        palabras = file.readline().split(',')
        pais = palabras[0]

        if pais in count_group_by_contry.keys():
            count_group_by_contry[pais] += 1
        else:
            count_group_by_contry[pais] = 1
print(count_group_by_contry)



def readLargeFileGen(aFile):
    """read lazy a file line by line. Ojo solo es para propositos educativos, readfile ya es un generator"""
    while True:
        linea = aFile.readline()
        if not linea:
            break
        yield linea

with open('world_ind_pop_data.csv') as archivo:
    gen = readLargeFileGen(archivo)

    print(next(gen))
    print(next(gen))
    print(next(gen))


#Abrir una archivo para leerlo linea a linea.
#Para saber cuantas veces si repite cada pais en el archivo en las primeras 1000 lineas
with open('world_ind_pop_data.csv') as file:
    #leo la primera linea de los headears, en este ejercicio quiero loopear sobre las tuplas directamente

    count_group_by_contry = {}

    for tupla in readLargeFileGen(file):
        #separo las palablras por coma
        palabras = tupla.split(',')
        pais = palabras[0]

        if pais in count_group_by_contry.keys():
            count_group_by_contry[pais] += 1
        else:
            count_group_by_contry[pais] = 1
print(count_group_by_contry)


####### ahora con pandas, el siguiente codigo solo procesa un solo chunck####
import pandas as pd
import matplotlib.pyplot as plt

pandasReader = pd.read_csv('world_ind_pop_data.csv', chunksize=3000)
df_chunck = next(pandasReader)
df_pais = df_chunck[df_chunck['CountryCode'] == 'USA']

zip_urban_pop = zip(df_pais['Total Population'], df_pais['Urban population (% of total)'])
urban_pop_tuple_list = list(zip_urban_pop)

#Agrego una nueva columna al frame compuesta por una multiplicación de otros valores del mismo df.
df_pais['Total Urban Population'] = [int(tupla[0] * tupla[1] / 100) for tupla in urban_pop_tuple_list]

#print(df_pais)


df_pais.plot(kind='scatter', x='Year', y='Total Urban Population')
plt.show()



####### ahora con pandas, el siguiente codigo procesa todos los chuncks####
import pandas as pd
import matplotlib.pyplot as plt


def plotPopulation (fileName, country_code):
    """procesa un archivo en chuncks, le genera un nuevo campo, y plotea"""
    pandasReader = pd.read_csv(fileName, chunksize=3000)
    df_completo = pd.DataFrame()

    for df_chunck in pandasReader:
        df_pais = df_chunck[df_chunck['CountryCode'] == country_code]

        zip_urban_pop = zip(df_pais['Total Population'], df_pais['Urban population (% of total)'])
        urban_pop_tuple_list = list(zip_urban_pop)

        #Agrego una nueva columna al frame compuesta por una multiplicación de otros valores del mismo df.
        df_pais['Total Urban Population'] = [int(tupla[0] * tupla[1] / 100) for tupla in urban_pop_tuple_list]
        df_completo = df_completo.append(df_pais)

    df_completo.plot(kind='scatter', x='Year', y='Total Urban Population')
    plt.title(country_code)
    plt.show()

plotPopulation('world_ind_pop_data.csv', 'USA')
plotPopulation('world_ind_pop_data.csv', 'ARG')
