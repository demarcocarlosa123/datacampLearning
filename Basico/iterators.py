flash = ['jay garrick', 'barry allen', 'wally west', 'bart allen']
mutants = ['charles xavier', 'bobby drake', 'kurt wagner', 'max eisenhardt', 'kitty pride']

it = iter(flash)
print(next(it))
print(next(it))


#la funcion enumarate() arma tuplas a partir de un iterable con el primer elto siendo el indice
flashEnumerado = enumerate(flash)
print(flashEnumerado)
listaFlashEnumerado = list(enumerate(flash))
print("listaEnumerada:")
print(listaFlashEnumerado)

print("For sentence:")
for index, value in enumerate(flash):
    print(index, value)

#La funcion zip() una en un objeto zip tuplas con los elementos de cada iterable pasado por cada indice.
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