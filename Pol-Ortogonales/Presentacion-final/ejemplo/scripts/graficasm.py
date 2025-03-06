import numpy as np
import matplotlib.pyplot as plt

def u_exact(r, phi):
    """Solución exacta (expansión en serie de e^(r*cos(phi)))."""
    return (1 + r * np.cos(phi) +
            (1/2) * r**2 * np.cos(phi)**2 +
            (1/6) * r**3 * np.cos(phi)**3)

def u_approx(r, phi):
    """Aproximación según la ecuación dada en el paper."""
    return (1 + r * np.cos(phi) +
            (1/4) * r**2 * (1 + np.cos(2*phi)) -
            (3/2) * r**3 * np.cos(phi))

# Malla polar
r = np.linspace(0, 1, 200)
phi = np.linspace(0, 2 * np.pi, 200)
R, Phi = np.meshgrid(r, phi)

# Coordenadas cartesianas
X = R * np.cos(Phi)
Y = R * np.sin(Phi)

# Evaluación de las funciones
U_exact = u_exact(R, Phi)

# Crear la figura con dos subgráficos
fig, ax = plt.subplots(1, 2, subplot_kw={'projection': '3d'}, figsize=(12, 6))

# Gráfica de la solución exacta
ax[0].plot_surface(X, Y, U_exact, cmap='viridis')
ax[0].set_title("Solución Exacta (Serie de Taylor)")
ax[0].set_xlabel('x')
ax[0].set_ylabel('y')
ax[0].set_zlabel('u')

plt.show()

