europa = {
    'spain': 'madrid',
    'france': 'paris',
    'germany': 'berlin',
    'norway': 'oslo'
}

print(type(europa))
print(europa)
print(europa.keys())
print("Type of dictionary.keys(): ", type(europa.keys()))
print("Capital de Francia:", europa['france'])

print("Esta Germany in Europe?: ",'germany' in europa)

## Agregando un elemneto a un diccionario:
europa['argentina'] = 'buenos aires'
print("Diccionario con elemento agregado: ",europa)
