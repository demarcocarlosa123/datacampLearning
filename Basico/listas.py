
# coding=utf-8
areas = ["distribuidor", 10, "cocina", 15, "living", 20.0, "dormitorio", 10.75, "baño", 0.50]
print(areas)

#slide selection
segundoAQuinto = areas[1:5]
print("segundoAQuinto", segundoAQuinto)

ultimoYanteUltimo = areas[-2:10]
print("ultimoYanteUltimo", ultimoYanteUltimo)

ultimoYanteUltimo = areas[-2:]
print("ultimoYanteUltimo", ultimoYanteUltimo)

print("primeros 5", areas[:5])

print("todos", areas[:])

listOfList = [["a", "b", "c"], ["d", "f"], ["g", "h", "i", "j"]]

print("From the last element, the first two", listOfList[-1][:2])

del(listOfList[0])
print(listOfList)

listOfList = listOfList + [["k", "l", "m"]]
print(listOfList)

print(type(listOfList))