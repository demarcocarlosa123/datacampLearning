def gritar(palabra, veces=1):
    try:
        return palabra * veces
    except:
        print("Palabra tiene que ser un string y veces un integer")

print(gritar("Hello", 4))
print(gritar("Hello", "muchas veces"))



def gritar2(palabra, veces=1):
    if veces <= 0:
        raise ValueError("Veces tiene que ser mayor a cero")
    return palabra * veces

print(gritar2("Hola", 3))
print(gritar2("Hola", -5))