# Import the numpy package as np
import numpy as np

# Create list baseball
baseball = [180, 215, 210, 210, 188, 176, 209, 200]


# Create a numpy array from baseball: np_baseball
np_baseball = np.array(baseball)

# Print out type of np_baseball
print(np_baseball, type(np_baseball))
print(baseball, type(baseball))

np_baseball_en_pulgadas = np_baseball / 100 / 0.0254
print("npArray con operacion aritimetica aplicada:", np_baseball_en_pulgadas)

baseball_weight = [90, 89, 120, 95, 105]
np_bb_weight_gramos = np.array(baseball_weight) * 1000
print(np_bb_weight_gramos)

bb_weight = np.array(baseball_weight)
##Aplicando una operacion logica
bb_gordos = bb_weight > 100
print(bb_gordos)
##Aplica un filtro. Solo se queda con los elementos "True", los otros no los incluye en el resultado.
print(bb_weight[bb_gordos])
print(bb_gordos.__len__())

##Filtro en una sola linea con numpy
bb_gordos = bb_weight[bb_weight > 100]
print(list(bb_gordos))

##Filtro con lambda
bb_gordos_lambda = filter(lambda persona: persona>100, baseball_weight)
print(list(bb_gordos_lambda))

a1 = np.array([True, 1, 2])
print(a1)

a2 = np.array([3, 4, False])
print(a2)

print(a1 + a2)
