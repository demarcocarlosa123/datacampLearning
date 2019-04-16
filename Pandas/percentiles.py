import pandas as pd
abandonos = pd.read_csv('abandonoAcumulado6.csv')

###Cuantiles para todos los campos numericos
###
x=abandonos.quantile([0, 0.25, 0.5, 0.75, 1])
print(x)

abandonos.plot.box()

import numpy as np
pd_tp = abandonos['TP-BR-Multi']
lista_tp = list(pd_tp)
np_tp = np.array(lista_tp)

print('TP-BR-Multi')
print(np.percentile(np_tp, np.arange(0, 100, 10)))


import matplotlib.pyplot as plt
#plt.boxplot(lista_tp)
#plt.show()