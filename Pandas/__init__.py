import pandas as pd

countries = ['United States', 'Australia', 'Japan', 'India', 'Russia', 'Morocco', 'Egypt']
drive_right = [True, False, False, False, True, True, True]
cars_per_country = [809, 731, 588, 18, 200, 70, 45]
primary_key = ['US', 'AU', 'JP', 'IN', 'RU', 'MO', 'EG']

my_dictionary = {
    'pais': countries,
    'maneja_derecha': drive_right,
    'cars_per_1000': cars_per_country
}

cars = pd.DataFrame(my_dictionary)
print(cars)

cars.index = primary_key
print(cars)
print(type(cars))