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