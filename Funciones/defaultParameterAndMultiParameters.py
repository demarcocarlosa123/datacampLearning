def gritar(palabra, veces = 1, intensidad = False):
    """devuelve la palabra gritada concatenada * veces, y lo pone en mayuscula a pedido"""
    grito = (palabra + " ") * veces
    grito = grito + "!!!"
    if intensidad is True:
        grito = grito.upper()
    return grito

print(gritar("Hola"))
print(gritar("Hola", 7))
print(gritar("Hola", 3, True))
print(gritar("Hola", intensidad=True))



def concatenar(*palabras):
    """concatena todas las palabras que se le pasan como argumento"""
    output = ""
    for elemento in palabras:
        output = output + elemento + " "
    return output

print(concatenar("luke"))
print(concatenar("luke", "leia", "Han", "chuwy"))



# Define report_status, con Diccionarios como parametros
def report_status(**kwargs):
    """Print out the status of a movie character."""

    print("\nBEGIN: REPORT\n")

    # Iterate over the key-value pairs of kwargs
    for key, value in kwargs.items():
        # Print out the keys and values, separated by a colon ':'
        print(key + ": " + value)

    print("\nEND REPORT")

# First call to report_status()
report_status(name="luke", affiliation="jedi", status="missing")



def soloCelulares(**diccionario):
    for key, value in diccionario.items():
        if value[0:2] == '11':
            print(key + " " + value)

soloCelulares(jesica='1157470808', ernesto='47558241', carlos='1133798241')