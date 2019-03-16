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