def potencia(n):
    """Devuelve la funcion potenciaInterna seteada con la potencia n"""

    def potenciaInterna(x):
        """Devuelve la potencia n-esima de un valor x"""
        return (x ** n)

    return potenciaInterna

alCubo = potencia(3)
print(alCubo(4))

alaQuinta = potencia(5)
print(alaQuinta(2))



def echo(veces):
    def repetir(texto):
        nuevoTexto = texto * veces
        return nuevoTexto
    return repetir

cuatroVeces = echo(4)
dosVeces = echo(2)
print(cuatroVeces("alma "), dosVeces("mora "))