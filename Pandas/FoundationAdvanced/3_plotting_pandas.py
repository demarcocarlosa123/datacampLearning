import pandas as pd
import matplotlib.pyplot as plt

austin = pd.read_csv('files/weather_data_austin_2010.csv')
print(austin.info())
print(austin.iloc[20:28, :])

### el ejercicio es plotear la temperatura
# configurando color, y titulos en los ejes

austin.Temperature.plot(color='red')
plt.xlabel('Hours since midnight August 1, 2010')
plt.ylabel('Temperature (degrees F)')
#plt.show()


### A veces conviene ver las variables al mismo tiempo.
# Pero al estar en diferentes escalas convine hacer sub reportes,
# O mostras un sub conjunto de series en el mismo gráfico
plt.close()
austin.plot()
plt.show()


# Mostrar las series como sub plots, para que cada uno este dentro de su escala
austin.plot(subplots = 'True')
plt.show()

# Mostrar solo los dos primeras series en el mismo grafico, ya que tienen escalas comparables.
plt.close()
seriesAComparar = ['Temperature', 'DewPoint']
austin[seriesAComparar].plot
plt.show()

