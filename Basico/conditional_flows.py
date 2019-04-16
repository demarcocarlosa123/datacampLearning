area = 14.3

if area > 15 :
    print('Big area!')
    print('Otra cosa')
    print('Medidas grandes')
elif area > 10 :
    print('Medida media')
    print('Intermedio')
else :
    print('Es chiquito')
    print('Casi infimo')
print('-----------------')

area = 8
if area > 30 :
    print('Enorme')
else :
    if area > 20 :
        print('Grande')
    else :
        if area >10 :
            print('Intermedio')
        else:
            print('chico')
print('-----------------')

area = 25
if area > 30: print('Enorme')
elif area > 20: print('Grande')
elif area > 10: print('Intermedio')
else: print('chico')