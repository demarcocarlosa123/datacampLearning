pos = {num:-num for num in range(10)}
print(pos)

### A partir de una lista creo un diccionario.
fellowship = ['frodo', 'samwise', 'merry', 'aragorn', 'legolas', 'boromir', 'gimli']
dicFellowship = {elemento:len(elemento) for elemento in fellowship}
print(dicFellowship)