flash = ['jay garrick', 'barry allen', 'wally west', 'bart allen']
mutants = ['charles xavier', 'bobby drake', 'kurt wagner', 'max eisenhardt', 'kitty pride']

it = iter(flash)
print(next(it))
print(next(it))


#la funcion enumarate() arma un objeto del tipo (Enumerate) a partir de un iterable con el primer elto siendo el indice
flashEnumerado = enumerate(flash)
print(flashEnumerado)

#La funcion list recibe como parametro un objeti enumerate y lo transforma en una lista.
listaFlashEnumerado = list(enumerate(flash))
print("listaEnumerada:")
print(listaFlashEnumerado)

print("For sentence:")
for index, value in enumerate(flash):
    print(index, value)

#La funcion zip() une los elementos de diferentes listas con mismo indice en un gran objeto Zip.
mutante = ['charles xavier', 'bobby drake', 'kurt wagner', 'max eisenhardt', 'kitty pride']
alias = ["porfesor X", "iceman", "nightcrawler", "magneto", "shadowcat"]
poder = ["telekinesis", "thermokinesis", "teletrasportacion", "magnetismo", "intangiability"]

x = zip(mutante, alias, poder)
print(x)
print("Lista de zips:")
print(list(x))

print("Sentencia For sobre objeto ZIP:")
x = zip(mutante, alias, poder)
for mut, ali, pod in x:
    print(mut, ali, pod)

print("Unzip:")
x = zip(mutante, alias, poder)
print(zip(*x))

#A partir de dos listas de igual largo se puede armar un diccionario de clave valor. 
nombre_alias = zip(mutante, alias)
nombre_alias_dic = dict(nombre_alias)
print("Diccionario creado a partir de un ZIP:")
print(nombre_alias_dic)