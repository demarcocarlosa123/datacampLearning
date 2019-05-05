import re

### Verificar que un String cumple un patron determinado
### se verifica si matchea con una expresión regular

regularExpresion = re.compile('\d{3}-\d{3}-\d{4}')
print(type(regularExpresion))

result = regularExpresion.match('123-566-7895')
print('tipo:', type(result))
print('123-566-7895:', bool(result))

result = regularExpresion.match('456-89-4569')
print('456-89-4569:', bool(result))

# Write the second pattern
# $ es una letra especial en re, entonces se debe scapear
# d* sirve para idicar cualquier numero de digitos
# . se escapea por ser paralabra
texto = 'U$D123.45'
pattern2 = bool(re.match(pattern='\$\d*\.\d{2}', string=texto))
print(texto, pattern2)
pattern2 = bool(re.match(pattern='U\$D\d*\.\d{2}', string=texto))
print(texto, pattern2)

# Write the third pattern
# corchetes sirve para indicar cualquier letra del abecedario
# w* sirve para indicar cualquier numero de letras en minuscula
texto = 'AUstralia'
pattern3 = bool(re.match(pattern='[A-Z]\w*', string='Australia'))
print(texto, pattern3)

print('----------------------1')
### Como extraer números de un parrafo.
### se usa usa la función findall()
### El + luego de la d sirve para que tome al 26 como un numero solo.
matcheos = re.findall('\d+', 'Azul tiene 4 años y el 26/6 va a cumplir 5 añitos')
print(type(matcheos))
print(matcheos)

print('------------------------2')
### Ahora para limpiar información de un data frame,
### se usa la funcion apply() de un pandas y se le pasa como parametro una función que haga la limpieza.
import pandas as pd
import numpy as np
df = pd.read_csv('files/demarcoFirus.csv', sep=';')
print(df)

dfNumerico = df[['altura', 'peso']]
print(dfNumerico)
a = dfNumerico.apply(np.mean, axis=0)
print(type(a))
print(a)


print('---------------------------3')
### Ejmplo de limpieza de columnas usando funciones definidas por mi, y usando apply() sobre el DataFrame

tips = pd.read_csv('files/tips2.csv', sep=';')
print(tips.head())

def acomodarSexo(generoString):
    """ Convierte a booleano el sexo"""
    if generoString == 'Male':
        return 1
    elif generoString == 'Female':
        return 0
    else:
        return np.nan


tips['sexoAcomodado'] = tips.sex.apply(acomodarSexo)
tips.sexoAcomodado = tips.sexoAcomodado.astype('category')
print(tips.head())
print(tips.info())


print('---------------------------4')
### Ahora limpieza con lamda usando replace y Regular expresion

tips['total_bill3'] = tips.total_bill2.apply(lambda x: x.replace('$', ""))
tips['tip3'] = tips.tip2.apply(lambda x: re.findall('\d+\.\d+', x)[0])

print(tips.head())