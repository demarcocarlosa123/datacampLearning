from urllib.request import urlopen, Request
import requests

url = "http://www.datacamp.com/teach/documentation"

#creo un objeto Request
req = Request(url)

#obtengo el response
res = urlopen(req)

print('Tipo clase:', type(res))
print('Id objeto:', res)
print(res.read())
res.close()

print('--------------------------------')
###Otra manera para ahorrar algunas lineas
###Usando un objeto requests
res = requests.get(url)

print('Tipo clase:', type(res))
print('Id objeto:', res)
print(res.text)

