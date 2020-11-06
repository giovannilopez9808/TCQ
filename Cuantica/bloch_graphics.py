from qiskit.visualization import plot_bloch_vector
import matplotlib.pyplot as plt
import numpy as np
up=np.array([0,0,1])
down=np.array([0,0,-1])
#Compuerta de Hadamard
H=1/np.sqrt(0.5)*np.array([[0,0,0],[0,1,1],[0,1,-1]])
n=np.dot(H,down)/2
plot_bloch_vector(n)
plt.show()