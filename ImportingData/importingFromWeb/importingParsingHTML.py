import requests
from bs4 import BeautifulSoup

url = 'https://www.python.org/~guido/'

#obtengo un response
resp = requests.get(url)

#creo un obteto Beauti
soup = BeautifulSoup(resp.text)

#Busco el titulo de la pagina
titulo = soup.title
print('Titulo:', titulo)

#Busco los tags html con hiperlinks
a_tags = soup.find_all('a')
for link in a_tags:
    print(link.get('href'))


#1ra funcion: identa el html
htmlIdentado = soup.prettify()
#print(htmlIdentado)