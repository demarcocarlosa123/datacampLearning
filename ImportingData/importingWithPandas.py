# Import pandas as pd
import pandas as pd


# Assign the filename: file
file = 'files/titanic_sub.csv'

# Read the file into a DataFrame: df
df = pd.read_csv(file)

# View the head of the DataFrame
print(df.head(4))





# Assign the filename: file
file = 'files/mnist_kaggle_some_rows.csv'

# Read the first 5 rows of the file into a DataFrame: data
data = pd.read_csv(file, nrows=5, header=None)

# Build a numpy array from the DataFrame: data_array
data_array = data.values

# Print the datatype of data_array to the shell
print(type(data_array))
print(data_array)




###Pandas tiene la posibilidad de trabajar con archivos mal formados, con comentarios, delimitadores determinados.
import matplotlib.pyplot as plt

# Assign filename: file
file = 'files/titanic_corrupt.txt'

# Import file: data
data = pd.read_csv(file, sep='\t', comment='#', na_values=['Nothing', 'NA'])

# Print the head of the DataFrame
print(data.head())

# Plot 'Age' variable in a histogram
pd.DataFrame.hist(data[['Age']], bins=15)
plt.xlabel('Age (years)')
plt.ylabel('count')
plt.show()
