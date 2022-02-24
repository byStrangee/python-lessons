import numpy as np
import matplotlib.colors as col
from mpl_toolkits.mplot3d import Axes3D 
import matplotlib.pyplot as plt
#Data for a three dimensional line
def f(x, y):
    return np.sin(np.sqrt(x ** 2 + y ** 2))
x = np.linspace(-6, 6, 30)
y = np.linspace(-6, 6, 30)
x, y = np.meshgrid(x, y)
z = f(x, y)
ax = plt.axes(projection='3d')
ax.plot_surface(x, y, z, rstride=1,
                cstride=1, cmap='viridis',
                edgecolor='none')
ax.set_title('surface')
plt.show()