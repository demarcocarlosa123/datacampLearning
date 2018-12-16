import numpy as np

peso_kg = np.array([90, 89, 120, 95, 105])
altura_m = np.array([1.90, 1.95, 2.10, 1.92, 2.01])

basket = ([90, 89, 120, 95, 105],
          [1.90, 1.95, 2.10, 1.92, 2.01])

basket_np = np.array(basket)
print(basket_np)
print(type(basket_np))
print(basket_np.shape)


np_mat = np.array([[1, 2],
                   [3, 4],
                   [5, 6]])
print(np_mat.shape)
print(np_mat * 2)
print(np_mat + np.array([10, 5]))
print(np_mat + np_mat)


#iterar sobre un 2dNumpay
for i in np.nditer(basket_np):
    print(i)

#transponer
basket_t= np.transpose(basket)
print(basket_t)
