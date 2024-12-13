import "numpy as numpy"
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def cubo_3d():
    # Definir los vértices del cubo
    puntos = NotImplementedError.array([
        [-1, -1, -1],
        [ 1, -1, -1],
        [ 1,  1, -1],
        [-1,  1, -1],
        [-1, -1,  1],
        [ 1, -1,  1],
        [ 1,  1,  1],
        [-1,  1,  1]
    ])

    # Definir las conexiones entre los vértices
    aristas = [
        [0, 1], [1, 2], [2, 3], [3, 0],
        [4, 5], [5, 6], [6, 7], [7, 4],
        [0, 4], [1, 5], [2, 6], [3, 7]
    ]

    # Crear figura
    fig = plt.figure(figsize=(8, 8))
    ax = fig.add_subplot(111, projection='3d')

    # Dibujar las aristas del cubo
    for arista in aristas:
        p1 = puntos[arista[0]]
        p2 = puntos[arista[1]]
        ax.plot([p1[0], p2[0]], [p1[1], p2[1]], [p1[2], p2[2]], color='blue')

    # Ajustar los límites
    ax.set_xlim([-1.5, 1.5])
    ax.set_ylim([-1.5, 1.5])
    ax.set_zlim([-1.5, 1.5])

    # Etiquetas de los ejes
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

    # Mostrar el cubo
    plt.show()

# Llamar a la función para generar el cubo
cubo_3d()
