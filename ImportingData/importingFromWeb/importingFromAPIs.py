import requests

#quiero la info solo de una pelicula
url = 'http://www.omdbapi.com/?apikey=72bc447a&t=the+social+network'

resp = requests.get(url)

#imprimir la respusta plana
#print(resp.text)

#implimir las claves y valores
peliculaDic = resp.json()

for k in peliculaDic:
    print(k, ': ', peliculaDic[k])


print('-----------------------------')
#le pido a wikipedia que me de info de la pizza
url = 'https://en.wikipedia.org/w/api.php?action=query&prop=extracts&format=json&exintro=&titles=pizza'

resp = requests.get(url)

jsonDic = resp.json()

#imprimir el json resultante plano
print(jsonDic)

#imprimir un determinado nodo del json que ya se que es un html, porque lei con los ojos el Json completo
html = jsonDic['query']['pages']['24768']['extract']
print(html)