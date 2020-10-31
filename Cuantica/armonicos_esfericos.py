import scipy as sci
import scipy.special as sp
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm, colors
l = 1    #grado del armónico esférico
m_n = 1    # orden
phi, theta = np.mgrid[0:2*np.pi:200j, 0:np.pi:100j]
#R = np.abs(sp.sph_harm(m, l, phi, theta))
R = sp.sph_harm(m_n, l, phi, theta).real
X = R * np.sin(theta) * np.cos(phi)
Y = R * np.sin(theta) * np.sin(phi)
Z = R * np.cos(theta)
norm = colors.Normalize()
fig, ax = plt.subplots(subplot_kw=dict(projection='3d'))
m = cm.ScalarMappable(cmap=cm.jet)
ax.plot_surface(X, Y, Z, rstride=1, cstride=1, facecolors=cm.jet(norm(R)))
ax.set_title('real$(Y^'+str(m_n)+'_'+str(l)+')$', fontsize=20)
m.set_array(R)
fig.colorbar(m, shrink=0.8)
plt.show()