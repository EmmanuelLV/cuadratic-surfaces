from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np


fig = plt.figure()
ax = fig.add_subplot(111,projection='3d')
a=1;
b=2;
c=3;
numElements = 30;
constant = 1;

x = np.linspace(-2*a, 2*a, numElements);
y = np.linspace(-2*b, 2*b, numElements);

[X, Y] = np.meshgrid(x, y);

Z1 = c*np.sqrt(1+X**2/a**2+Y**2/b**2);

ax.plot_surface(X, Y, Z1,  rstride=1, cstride=1, color='b')

Z2 = -c*np.sqrt(1+X**2/a**2+Y**2/b**2);


ax.plot_surface(X, Y, Z2,  rstride=1, cstride=1, color='b')


ax.set_xlabel('Eje X')
ax.set_ylabel('Eje Y')
ax.set_zlabel('Eje Z')

plt.show()
