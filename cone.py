from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np


fig = plt.figure()
ax = fig.add_subplot(111,projection='3d')

# Set up the grid in polar
theta = np.linspace(0,2*np.pi,90)
r = np.linspace(0,3,50)
T, R = np.meshgrid(theta, r)

# Then calculate X, Y, and Z
X = R * np.cos(T)
Y = R * np.sin(T)
Z = (np.sqrt(X**2 + Y**2) - 1)*-1
print("z1:"+repr(Z)+"\nz2"+repr(np.sqrt(X**2 + Y**2) - 1))
# Set the Z values outside your range to NaNs so they aren't plotted
Z[Z < 0] = np.nan
Z[Z > 2.1] = np.nan
ax.plot_surface(X, Y, Z,  rstride=4, cstride=4, color='b')

ax.set_zlim(0,2)

ax.set_xlabel('Eje X')
ax.set_ylabel('Eje Y')
ax.set_zlabel('Eje Z')

plt.show()
