import numpy as np
import numpy.random
import matplotlib.pyplot as plt

#create data
x = np.random.rand(4096)
y = np.random.rand(4096)

#create heatmap
heatmap, xedges, yedges = np.histogram2d(x, y , bins=(64, 64))
extent = [xedges[0], xedges[-1],yedges[0], yedges[-1]]

#plot heatmap
plt.clf()
plt.title("heatmap example")
plt.xlabel("x")
plt.ylabel("y")
plt.imshow(heatmap, extent= extent)
plt.show()
