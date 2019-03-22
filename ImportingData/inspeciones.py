import numpy as np
import matplotlib.pyplot as plt
archivo = 'files/inspeciones.csv'
inspections = np.loadtxt(archivo, delimiter=',', dtype=int, skiprows=1)
print(np.shape(inspections))

listaInspections = list(inspections)
print(listaInspections)

plt.hist(listaInspections, bins=6)
plt.show()