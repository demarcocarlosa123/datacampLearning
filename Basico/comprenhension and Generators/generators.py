# un generador no crea la lista como los comprenhension sino que lo dilata hasta que se necesita usar.
# Sirve para generar indices tan grandes que no entrarian en memoria.


sec = (num for num in range(30))
valor = next(sec)
print(valor)
valor = next(sec)
print(valor)
valor = next(sec)
print(valor)
for valor in sec:
    print(valor)


pares = (num for num in range(10**2) if num % 2 == 0)
print(pares)
print(list(pares))


#Generator funtions son funciones que devuelven generadores.
def secuenciaImparHasta(n):
    i = 0
    while i < n:
        if i%2 == 1:
            yield i
        i += 1

print(list(secuenciaImparHasta(10**2)))
for i in secuenciaImparHasta(10**2):
    print(i)

lannister = ['cersei', 'jaime', 'tywin', 'tyrion', 'joffrey']
largo = (len(persona) for persona in lannister)
print(list(largo))

def get_largo(iterable):
    for persona in iterable:
        yield(len(largo))

for value in get_largo(lannister):
    print(value)