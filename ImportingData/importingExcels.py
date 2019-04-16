# Import pandas
import pandas as pd
import xlrd
# Assign spreadsheet filename: file
file = 'files/battledeath.xlsx'

# Load spreadsheet: xl
xl = pd.ExcelFile(file, mode='r')

# Print sheet names
print(xl.sheet_names)


# cargar una hoja por nombre
s1 = xl.parse('2004')
print(s1.head())

#cargar una hoja por indice
s2 = xl.parse(0)
print(s2.head())


#Al mismo momento que se parsea una hoja se puede, saltear una cantidad de filas,
# renombrar columnas, y seleccionar un subconjunto de columnas
s3 = xl.parse(0, skiprows=1, names=['nombre1', 'nombre2'])
print(s3.head())
print('----------------')
s4 = xl.parse(1, skiprows=1, parse_col=[0])
print(s4.head())