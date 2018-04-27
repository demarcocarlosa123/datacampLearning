# coding=utf-8
x = True

print(x)
print(type(x))
print(int(x))

listOfList = [["a", "b", "c"], ["d", "f"], ["g", "h", "i", "j"]]
print("lengh of the list is: ", len(listOfList))
print("lengh of the second list of the list", len(listOfList[1]))


x = [8.3, 3.1, 7, 5, 1]
y = [2.2, 4.6, 9.1]

print("Max element", max(x))
print("Max element of two lists", max(x, y))

w = x + y
print("lista W: ",w)
sorted_w = sorted(w, reverse=True)
print("Lista ordenada:", sorted_w)

print("possition of 7", x.index(7))
