# Para devolver multiples valores de las funciones se usa una estructura llamada tupla
tupla1 = ("unaValor", "OtroValor", "Otro valor mas")
print(tupla1)

val1, val2, val3 = tupla1
print(val2)
print(tupla1[1])




def gritar(palabra1, palabra2):
    """Le agrega a palabra pasada tres exclamaciones"""
    tupla = (palabra1 + "!!!", palabra2 + "!!!")
    return tupla
grito1, grito2 = gritar("puto", " el que lee")
print(grito1)
print(grito2)


