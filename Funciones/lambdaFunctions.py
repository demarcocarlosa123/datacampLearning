#Lamda funcions es una forma simple de escribir una breve funcion en una sola linea.
gritar = (lambda palabra, veces: palabra * veces)
print(gritar("Hola ", 5))


#map() sirven para aplicar una funcion lambda sobre un array
#map() recibe dos parametros, una funcion y una lista. La funcion puede ser tanto un lambda como una funcion comun
spells = ["protego", "accio", "expecto patronum", "legilimens"]
spellsRepetidos = map(lambda s: (s + " ") * 3, spells)
print(type(spellsRepetidos))
print(spellsRepetidos)
spellsRepetidosLista = list(spellsRepetidos)
print(spellsRepetidosLista)

def multiplicarPalabra(cantidadVeces):
    """A la palabra pasada por parametro se le agrega un espacio y a eso se lo multiplique por 3"""
    def multiplicar(palabra):
        return (palabra + " ") * cantidadVeces
    return multiplicar

porTres = multiplicarPalabra(3)
spellsRepetidos = map(porTres, spells)
print(list(spellsRepetidos))




#Otro uso comun es para filtrar arrays
fellowship = ['frodo', 'samwise', 'merry', 'aragorn', 'legolas', 'boromir', 'gimli']
miembrosLargos = filter(lambda member: len(member)>6 , fellowship)
print(miembrosLargos)
print(list(miembrosLargos))

isCorto = (lambda elemento: len(elemento)<=6)
miembrosCortos = filter(lambda elemento: len(elemento)<=6, fellowship)
print(list(miembrosCortos))

#La otra utilidad que tiene lambda es aplicarlos sobre reduce.
# Import reduce from functools
from functools import reduce

# Create a list of strings: stark
stark = ['robb', 'sansa', 'arya', 'eddard', 'jon']

# Use reduce() to apply a lambda function over stark: result
result = reduce(lambda item1, item2: item1 + item2, stark)

# Print the result
print(result)