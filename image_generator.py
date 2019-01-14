import os

#Installing and testing of dependencies
try:
    import numpy
except ImportError:
	os.system('sudo pip install numpy')
try:
    import scipy
except ImportError:
	os.system('sudo pip install scipy')
try:
    import matplotlib
except ImportError:
	os.system('sudo pip install matplotlib')

#main programs start here
import numpy as np
from scipy import misc
import matplotlib.pyplot as plt
import random

colours = ['flag', 'prism', 'ocean', 'gist_earth', 'terrain', 'gist_stern','gnuplot', 'gnuplot2', 'CMRmap', 'cubehelix', 'brg', 'hsv','gist_rainbow', 'rainbow', 'jet', 'nipy_spectral', 'gist_ncar','PiYG', 'PRGn', 'BrBG', 'PuOr', 'RdGy', 'RdBu','RdYlBu', 'RdYlGn', 'Spectral', 'coolwarm', 'bwr', 'seismic','magma','hot','Greys', 'Purples', 'Blues', 'Greens', 'Oranges', 'Reds','YlOrBr', 'YlOrRd', 'OrRd', 'PuRd', 'RdPu', 'BuPu','GnBu', 'PuBu', 'YlGnBu', 'PuBuGn', 'BuGn', 'YlGn']
h = 320     #for 10cm use 602 #height
w = 480		#for 15cm use 898 #width
h,w=w,h
 
s = 300  # Scale.
x = np.linspace(-h / s, h / s, num=h).reshape((1, h))
y = np.linspace(-w / s, w / s, num=w).reshape((w, 1))
Z = np.tile(x, (w, 1)) + 1j * np.tile(y, (1, h))
 
C = np.full((w, h), -0.43 + 0.6j)
M = np.full((w, h), True, dtype=bool)
N = np.zeros((w, h))
for i in range(256):
    Z[M] = Z[M] * Z[M] + C[M]
    M[np.abs(Z) > 2] = False
    N[M] = i
# Save with Matplotlib using a colormap.
fig = plt.figure()
fig.set_size_inches(h / 100, w / 100)
ax = fig.add_axes([0, 0, 1, 1], frameon=False, aspect=1)
ax.set_xticks([])
ax.set_yticks([])
plt.imshow(np.flipud(N),cmap=random.choice(colours)) 
plt.savefig('mandelbrot_image.png')
plt.close()