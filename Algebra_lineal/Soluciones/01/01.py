#<---------Solucion a los problemas propuestos en el notebook--------------->
#<------------------01 escalares vectores matrices tensores.ipynb-------------->
import numpy as np
#<--------------Crear un escalar 42-------------->
a=42
print("Esto es un escalar con valor 42\n",a)
#<------------Crear el vector con los elementos 2,3,5,7---------------->
a=np.array([2,3,5,7])
print("Esto es un vector con elementos 2,3,5,7\n",a)
#<Crear una matriz de 2x2 con los elementos 2,3 en la primera fila y 5,7 en la segunda fila>
a=np.array([[2,3],[5,7]])
print("Esto una matriz de 2x2 con los elementos 2,3 en la primera fila y 5,7 en la segunda fila\n",a)
#<Crear un tensor que al graficarlo veamos Blanco, Negro, Gris, desde arriba hacia abajo.>
#<-----------Nota------------>
#<-----La funcion imshow de matplot realiza el "plot" de pixeles, este normalmente tiene valores en rgb--------->
#<-------Blaco en rgb (255,255,255)---------->
#<--------Gris en rgb (128,128,128)----------->
#<----------Negro en rgb (0,0,0)--------------->
#<----------- el tensor que formaremos tendra dimensiones de 3x3------------->
a=np.array([
    [[255,255,255],[255,255,255],[255,255,255]], #Blanco
    [[128,128,128],[128,128,128],[128,128,128]], # Gris
    [[0,0,0],[0,0,0],[0,0,0]] # Negro
]
)
#<--------------Libreria para plotear------------>
import matplotlib.pyplot as plt
#<-------------Deshabilito los ejes---------->
plt.yticks([]);plt.xticks([])
plt.imshow(a)
plt.show()