from sqlalchemy import create_engine
import pandas as pd

#creo un engine que estos locos le dicen Motor
engine = create_engine('sqlite:///files/Chinook.sqlite')

#mostrar las tablas

# Save the table names to a list: table_names
table_names = engine.table_names()

# Print the table names to the shell
print(table_names)

#Creo una conexion
con = engine.connect()

#ejecuto el query
rs = con.execute('select * from Album')
df = pd.DataFrame(rs.fetchall())

#Cierro la conexión
con.close()

print(df.head())



#ahora vamos abrir un conexión en un contexto
with engine.connect() as con:
    rs = con.execute('select LastName, Title from Employee Order by LastName desc')
    df = pd.DataFrame(rs.fetchmany(size=10))
    df.columns = rs.keys()

print('largo:', len(df))
print(df.head())


#Una forma mas corta de cargar un dataFrame desde una consulta SQL, pero ahora usando una funcion de Pandas
df = pd.read_sql_query('SELECT * FROM Album', engine)
print(df.head())

print('--------------------')
df2 = pd.read_sql_query('SELECT al.Title, ar.Name '
                        'FROM Album as al '
                        'INNER JOIN ARTIST as ar ON al.ArtistID = ar.ArtistID', engine)
print(df2.head())