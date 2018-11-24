nombres = ["carlos", "Jesica", "Azul", "Bauti"]
anios = [35, 37, 3, 0.7]


def list2Dict(list1, list2):
    """Lista1 se convertira en las claves, lista 2 en los valores"""
    zipped = zip(list1, list2)
    return dict(zipped)

d = list2Dict(nombres, anios)
print(d)




import numpy as np
headers = ['NombrePais', 'Codigo', 'Desidad', 'Superficie', 'Capital', 'poblacion']
paises = [['Argentina', 'AR', 16, 2792573, 'Buenos Aires'],
         ['Brasil', 'BR', 24, 8514877, 'Brasilia'],
         ['Paraguay', 'PY', 17, 406752, 'Asuncion']]

def calcularPoblacion(densidad, superficie):
    return densidad * superficie

for pais in paises:
    poblacion = calcularPoblacion(pais[2], pais[3])
    pais.append(poblacion)

###Ejercicio: contruir una lista de diccionarios, con los datos de las dos listas anteriores
###usando list comprenhension

listaDeDiccionarios = [list2Dict(headers, pais) for pais in paises]
print(listaDeDiccionarios)