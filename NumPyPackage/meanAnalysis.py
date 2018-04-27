import numpy as np

peso_kg = np.array([90, 89, 120, 95, 105, 98, 103, 114, 100, 94])
altura_m = np.array([1.90, 1.95, 2.10, 1.92, 2.01, 1.98, 2.02, 2.16, 1.98, 1.96])

#print("Valor promedio: ", np.mean(peso_kg))
#print("Mediana: ", np.median(peso_kg))

players = np.array([[90, 89, 120, 95, 105, 98, 103, 114, 100, 94],
                    [1.90, 1.95, 2.10, 1.92, 2.01, 1.98, 2.02, 2.16, 1.98, 1.96]])

peso = players[0, :]
altura = players[1, :]
print("Peso - promedio: ", np.mean(peso))
print("Peso - mediana: ", np.median(peso))
print("Peso - desvio standar:", np.std(peso))
print("Altura - promedio: ", np.mean(altura))
print("Altura - mediana: ", np.median(altura))
print("Altura - desvio estandar:", np.std(altura))
print("Altura peso - coef correlacion: ", np.corrcoef(peso, altura))
print("-------------------------------------------------------")

mas100k = peso > 100
alturasMas100k = altura[mas100k]
print(alturasMas100k)
print("Promedio altura jugadores mas de 100k: ", np.mean(alturasMas100k))
print("Promedio altura jugadores mas de 100k: ", np.mean(altura[peso > 100]))
