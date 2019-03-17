from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np


fig = plt.figure()
ax = fig.add_subplot(111,projection='3d')

# Set up the grid in polar
u = np.linspace(0,2*np.pi,50)
v = np.linspace(-5,5,30)
U,V = np.meshgrid(u, v)



a = 3
b = 3
c = 6

# Then calculate X, Y, and Z
X = a * V*np.cos(U)
Y = b * V*np.sin(U)
Z = c * V


ax.plot_surface(X, Y, Z,  rstride=1, cstride=1, color='b')


ax.set_xlabel('Eje X')
ax.set_ylabel('Eje Y')
ax.set_zlabel('Eje Z')

plt.show()
