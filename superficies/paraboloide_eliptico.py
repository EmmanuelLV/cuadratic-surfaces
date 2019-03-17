from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

fig = fig = plt.figure() # Square figure
ax = fig.add_subplot(111, projection='3d')

r=1;
u=np.linspace(-10,10, 100)
v=np.linspace(-np.pi,np.pi, 100)
[u,v]=np.meshgrid(u,v);

a = 1
b = 1
c = 1

x = a*u*np.cos(v)
y = b*u**2
z = 5*u*np.sin(v)

ax.plot_surface(z, x, y,  rstride=4, cstride=4, color='b')

ax.set_xlabel('Eje X')
ax.set_ylabel('Eje Y')
ax.set_zlabel('Eje Z')

plt.show()
