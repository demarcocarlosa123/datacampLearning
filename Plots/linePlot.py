import matplotlib.pyplot as plt

year = [1950, 1970, 1990, 2010, 2030, 2050, 2070, 2090, 2110]
pop = [2.51, 3.69, 5.26, 6.97, 8.43, 12.34, 17.34, 24.87, 34.73]
print("Cant anos:", len(year))
plt.plot(year, pop)

plt.clf()

plt.scatter(year, pop)
xLabel = "Ano"
yLabel = "Poblacion"
titulo = "Ano vs Poblacion"
plt.title(titulo)
plt.xlabel(xLabel)
plt.ylabel(yLabel)
plt.xticks([1900, 1950, 2000, 2050, 2100], ['A0', 'A1', 'A2', 'A3', 'A4'])
plt.show()

