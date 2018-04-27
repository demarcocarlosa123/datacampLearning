import matplotlib.pyplot as plt
import numpy as np
from random import randint

peso_kg = [90, 95, 98, 95, 100, 103, 105, 90, 105, 110, 115, 117, 120, 115, 120, 123, 127, 128, 130, 125, 128, 132, 115, 125, 134, 130, 137, 130, 138, 140, 141, 138, 139, 140, 142, 143, 148, 149, 150]
altura_m = [1.8, 1.8, 1.8, 1.85, 1.85, 1.85, 1.85, 1.9, 1.9, 1.9, 1.95, 1.95, 1.95, 2, 2, 2.05, 2.05, 2.05, 2.05, 2.1, 2.1, 2.1, 2.15, 2.15, 2.15, 2.2, 2.2, 2.25, 2.25, 2.25, 2.25, 2.3, 2.3, 2.3, 2.35, 2.35, 2.4, 2.4, 2.4]
cantidad = [900, 1500, 1800, 1500, 900, 1500, 600, 900, 300, 900, 1500, 1800, 600, 1500, 1800, 900, 300, 600, 1500, 600, 900, 600, 1200, 1500, 1800, 600, 900, 600, 900, 600, 1500, 300, 900, 900, 900, 600, 300, 300, 300]
color = ['blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'green', 'green', 'green', 'green', 'green', 'green', 'green', 'green', 'green', 'green', 'green', 'green', 'yellow', 'yellow', 'yellow', 'yellow', 'yellow', 'yellow', 'yellow', 'yellow', 'yellow', 'yellow', 'yellow', 'yellow', 'yellow', 'red', 'red']
print(len(cantidad))

peso_np = np.array(peso_kg)
altura_np = np.array(altura_m)
cantidad_np = np.array(cantidad)
autogenerado = np.random.random((1, 39)) * 1
print(autogenerado)

cantidad_np = cantidad_np * autogenerado * autogenerado

plt.scatter(peso_np, altura_np, s=cantidad_np, c=color, alpha=0.8)
plt.xlabel('peso en kilos')
plt.ylabel('Altura en metros')
plt.title('Tamano poblacion segun peso y altura')
plt.text(100, 1.85, 'Charly')
plt.text(120, 1.95, 'Denis Rodman')
plt.text(130, 2.1, 'Shakil Oneil')
plt.grid(True)
plt.show()
