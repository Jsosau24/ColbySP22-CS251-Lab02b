
import numpy as np
import matplotlib.pyplot as plt

Lab02 = np.genfromtxt('data/gauss_3d.csv', delimiter=',')
Lab02 = np.array(Lab02)
 
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

zdata = Lab02[:,2]
xdata = Lab02[:,0]
ydata = Lab02[:,1]

ax.scatter3D(xdata, ydata, zdata, c=zdata);
plt.show()
