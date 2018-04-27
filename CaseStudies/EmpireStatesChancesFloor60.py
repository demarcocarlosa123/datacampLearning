import numpy as np
import matplotlib.pyplot as plt

#Una persona le apuesta a otra que va a llegar por encima del piso 59. Cuantas chances tiene de ganar?

#Una tirada de lanzamiento de dado del juego propiamente dicho
def lanzarDado():
    return np.random.randint(1, 7)

def jugarASubirOBajar():
    dado = lanzarDado()
    if dado <= 2:
        return -1
    elif dado <= 5:
        return 1
    else:
        dado = lanzarDado()
        return dado

def torpe():
    return np.random.rand() <= 0.001


#Un random walk de 100 pasos

np.random.seed(123)
corridas = []
cant_simulaciones = 1000
for i in range(cant_simulaciones):
    pisos = [0]
    for x in range(100):
        pisoActual = pisos[-1]
        nuevoPiso = max(0, pisoActual + jugarASubirOBajar())
        if not torpe():
            pisos.append(nuevoPiso)
        else:
            pisos.append(0)
    corridas.append(pisos)

corridas_traspuesta = np.transpose(corridas)
plt.plot(corridas_traspuesta)
xLabel = "Tiros de dados"
yLabel = "Pisos alcanzados"
titulo = "Evolucion pisos alcanzados"
plt.title(titulo)
plt.xlabel(xLabel)
plt.ylabel(yLabel)
plt.show()

terminales = corridas_traspuesta[-1, :]

plt.clf()
plt.hist(terminales, bins=20)
xLabel = "Piso alcanzado"
yLabel = "Veces alcanzado"
titulo = "Histograma piso mas alto alcanzado"
plt.title(titulo)
plt.xlabel(xLabel)
plt.ylabel(yLabel)
plt.show()

probabilidad = np.sum(terminales >= 60) / float(cant_simulaciones)
print("P() de lograr llegar por encima del piso 59 en 100 tiros es " + str(probabilidad))
