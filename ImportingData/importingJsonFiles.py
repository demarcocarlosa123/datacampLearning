import json

with open('files/a_movie.json') as file:
    json_data = json.load(file)

print(json_data)

for k in json_data.keys():
    print(k, ': ', json_data[k])