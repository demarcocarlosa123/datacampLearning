gritar = (lambda palabra, veces: palabra * veces)
print(gritar("Hola ", 5))


#Lambda functions sirven para aplicar una simple funcion sobre un array
spells = ["protego", "accio", "expecto patronum", "legilimens"]
spellsRepetidos = map(lambda s: (s + " ") * 3, spells)
print(type(spellsRepetidos))
print(spellsRepetidos)
spellsRepetidosLista = list(spellsRepetidos)

#Otro uso comun es para filtrar arrays
fellowship = ['frodo', 'samwise', 'merry', 'aragorn', 'legolas', 'boromir', 'gimli']
cortos = filter(lambda member: len(member)>6 , fellowship)
print(cortos)

#La otra utilidad que tiene lambda es aplicarlos sobre reduce.
# Import reduce from functools
from functools import reduce

# Create a list of strings: stark
stark = ['robb', 'sansa', 'arya', 'eddard', 'jon']

# Use reduce() to apply a lambda function over stark: result
result = reduce(lambda item1, item2: item1 + item2, stark)

# Print the result
print(result)