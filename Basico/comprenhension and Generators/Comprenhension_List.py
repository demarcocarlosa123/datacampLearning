###List comprenhension es una forma concisa de crear LISTAS.

flash = ['jay garrick', 'barry allen', 'wally west', 'bart allen']
mutants = ['charles xavier', 'bobby drake', 'kurt wagner', 'max eisenhardt', 'kitty pride']

flashTooneada = []
for x in mutants:
    flashTooneada.append(x + "!")
print(flashTooneada)

flashTooneada = [x + "!" for x in mutants]
print(flashTooneada)

indice = [i for i in range(11)]
print(indice)

#listComprenhension que devuelva solo la primera letra de cada palabra
doctor = ['house', 'cuddy', 'chase', 'thirteen', 'wilson']
doctor_inicial = [l[0:1] for l in doctor]
print(doctor_inicial)

# Create list comprehension: squares
squares = [i ** 2 for i in range(10)]
print(squares)

#Crear una matriz de 5x5 desde 0 a 4 con list comprenhensions
matris = [[elemento for elemento in range(0,5)] for columna in range(0,5)]
print(matris)

#Ahora quiero una lista pero solo si se cumple alguna condicion
cuadradosPares = [numero ** 2    for numero in range(10) if numero % 2 == 0]
print(cuadradosPares)

fellowship = ['frodo', 'samwise', 'merry', 'aragorn', 'legolas', 'boromir', 'gimli']
fellowLargos = [miembro for miembro in fellowship if len(miembro)>=7]
print(fellowLargos)

new_fellowship = [member  if len(member)>=7 else "" for member in fellowship]
# Print the new list
print(new_fellowship)


cuadradosSoloCuandoBaseEsPar = [numero**2  if numero%2==0 else 0 for numero in range(10)]
print(cuadradosSoloCuandoBaseEsPar)