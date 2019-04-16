my_kitchen = 18.0
your_kitchen = 14.0

print('Is the double of my kitchen smaller than the triple of your kitchen?: ', 2 * my_kitchen < 3 * your_kitchen)


import numpy as np
array_my_house = [18.0, 20.0, 10.75, 9.50]
array_your_house = [4.0, 24.0, 14.25, 9.0]

my_house = np.array(array_my_house)
your_house = np.array(array_your_house)

# my_house greater than 18.5 or smaller than 10
print(np.logical_or(my_house > 18.5, my_house < 10))

# Both my_house and your_house smaller than 11
print(np.logical_and(my_house < 11, your_house < 11))

# Both my_house greater than 10 and your_house smaller than 15
print(np.logical_and(my_house > 10, your_house < 15))