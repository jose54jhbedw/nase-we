import turtle
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def flor_3d():
    # Crear datos para los pétalos
    u = np.linspace(0, 2 * np.pi, 100)
    v = np.linspace(0, np.pi, 100)
    u, v = np.meshgrid(u, v)

    # Ecuaciones paramétricas para los pétalos
    x = (1 + 0.5 * np.sin(6 * u)) * np.sin(v) * np.cos(u)
    y = (1 + 0.5 * np.sin(6 * u)) * np.sin(v) * np.sin(u)
    z = (1 + 0.5 * np.sin(6 * u)) * np.cos(v)

    # Crear figura
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='3d')

    # Dibujar los pétalos
    ax.plot_surface(x, y, z, cmap='autumn', edgecolor='none', alpha=0.8)

    # Crear el tallo
    z_tallo = np.linspace(-2, 0, 100)
    x_tallo = 0.1 * np.sin(10 * z_tallo)
    y_tallo = 0.1 * np.cos(10 * z_tallo)
    ax.plot(x_tallo, y_tallo, z_tallo, color='green', linewidth=3)

    # Ajustar los límites
    ax.set_xlim([-2, 2])
    ax.set_ylim([-2, 2])
    ax.set_zlim([-2, 2])

    # Ocultar ejes
    ax.axis('on')

    # Mostrar la flor
    plt.show()

# Llamar a la función para generar la flor
flor_3d()
