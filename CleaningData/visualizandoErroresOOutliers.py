import matplotlib.pyplot as plt
import pandas as pd

file = 'files/dob_job_application_filings_subset.csv'
fileNum = 'files/dob_job_application_filings_subset_num.csv'

df = pd.read_csv(file)
dfNum = pd.read_csv(fileNum, sep=';')



# Al DF original le agrego dos columnas con valores motenarios
# que con el excel le saque el signo pesos.
print(df.shape)
df['initialCost'] = dfNum['initialCost']
df['totalEstFee'] = dfNum['totalEstFee']
print(df.shape)



### Primero vemos los valores estadisticos
print(df['Existing Zoning Sqft'].describe())

### Ahora vamos a comparar los datos estadisticos contra un histograma
### Los histogramas son barbaros para entender variables unicas.
### En este ejemplo se usa una escala logaritmica.
### Estadisticamente vemos que casi todos los valores son cero, y hay pocos mas grandes. Extrañamente hay un grupo de outlayer a la derecha
df['Existing Zoning Sqft'].plot(kind='hist', rot=45, logx=False, logy=True, bins=10)
plt.show()

print('-------------------------')

### Para visualizar multiples cortes de una misma variable son utiles los BoxPlots
# Great work! You can see the 2 extreme outliers are in the borough of Manhattan.
# An initial guess could be that since land in Manhattan is extremely expensive,
# these outliers may be valid data points. Again, further investigation is needed
df.boxplot(column='initialCost', by='Borough', rot=45)
plt.show()



### When you want to visualize two numeric columns, scatter plots are ideal.
# Create and display the first scatter plot
# It is difficult to infer any trends from the first plot because it is dominated by the outliers.
df.plot(kind='scatter', x='initialCost', y='totalEstFee', rot=70)
plt.show()

# Despues de ver mucho el grafico hago unos recortes a los datos que parecen outliners
df_subset = df[df['initialCost'] < 1000000]
df_subset = df[df['totalEstFee'] < 10000]

# Create and display the second scatter plot
# it seems like there is a strong correlation between 'initial_cost' and 'total_est_fee'.
# In addition, take note of the large number of points that have an 'initial_cost' of
df_subset.plot(kind='scatter', x='initialCost', y='totalEstFee', rot=70)
plt.show()