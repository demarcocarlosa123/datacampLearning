file = open('files/seaslug.txt', 'r')

print(file)
print(file.read())

print(file.closed)
file.close()
print(file.closed)


#Para olvidarse de tener que cerrar el archivos, se pone una clausula with. cuando termine la clausula se
with open('files/seaslug.txt', 'r') as file:
    print(file.readline())
    print(file.readline())


print('-------------------------')
#Practicas diarias:
#Buscando un output None

filename = 'files/seaslug.txt'
file = open(filename, mode='r')
text = file.read()
print(text)
file.close()

#Devuelve none porque ese el el resulsado del metodo Close()
filename = 'files/seaslug.txt'
file = open(filename, mode='r')
text = file.close()
print(text)

