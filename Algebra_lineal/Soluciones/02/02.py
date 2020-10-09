#Solucion a los ejercicios propuestos en el notebook
# Transposicion Suma Matrices y Escalares.ipynb
import numpy as np
import matplotlib.pyplot as plt

def plot_matrices(axs,matrices,titles):
    for ax,matriz,title in zip(axs,matrices,titles):
        ax.set_title(title)
        ax.imshow(matriz,cmap="binary")
        ax.set_yticks([])
        ax.set_xticks([])

#<---------- Calcula la multiplicacion de dos matrices 5x5
#<---------------Creando la matriz A con valores aleatorios entre 0,255
A=np.random.random([5,5])*255
#<---------------Creando la matriz B con valores aleatorios entre 0,255
B=np.random.random([5,5])*255
#<-------------------C=AB-------------->
C=np.dot(A,B)
#<-----------------D=BA------------------>
D=np.dot(B,A)
fig,axs=plt.subplots(2,3)
plot_matrices(axs[0,:],[A,B,C],["A","B","AB"])
plot_matrices(axs[1,:],[B,A,D],["B","A","BA"])
plt.show()
#<-------------------------Extendi el problema para que pudieran de una manera visual
#<--------------------ver que BA=/=AB
#<----------El problema de umas una matriz y un escalar no se puede realizar la suma