import numpy as np
import matplotlib.pyplot as plt
import math

# Definir la solución analítica
def u_exact(r, theta):
    return np.exp(r * np.cos(theta))

# Polinomios de Zernike Radiales
def zernike_radial(n, m, r):
    """Cálculo del polinomio radial de Zernike R_n^m(r)."""
    R = np.zeros_like(r, dtype=float)
    for k in range((n - m) // 2 + 1):
        c = (-1)**k * math.factorial(n - k) / (
            math.factorial(k) * math.factorial((n + m) // 2 - k) * math.factorial((n - m) // 2 - k)
        )
        R += c * r**(n - 2 * k)
    return R

# Solución aproximada con Polinomios de Zernike
def u_zernike(r, theta, n_max=3):
    """Aproximación de la solución con polinomios de Zernike."""
    u_approx = np.zeros_like(r, dtype=float)
    for n in range(n_max + 1):
        for m in range(0, n + 1, 2):  # Solo términos válidos
            R_nm = zernike_radial(n, m, r)
            u_approx += R_nm * np.cos(m * theta)  # Aproximación
    return u_approx

# Crear malla en coordenadas polares
r = np.linspace(0, 1, 100)
theta = np.linspace(0, 2 * np.pi, 100)
R, Theta = np.meshgrid(r, theta)
X, Y = R * np.cos(Theta), R * np.sin(Theta)

# Evaluar soluciones
U_exact = u_exact(R, Theta)
U_approx = u_zernike(R, Theta, n_max=5)  # Mayor orden para mejor precisión

# Graficar soluciones
fig = plt.figure(figsize=(12, 6))

# Solución Exacta
ax1 = fig.add_subplot(121, projection='3d')
ax1.plot_surface(X, Y, U_exact, cmap='viridis', edgecolor='none')
ax1.set_title("Solución Exacta")
ax1.set_xlabel("X")
ax1.set_ylabel("Y")
ax1.set_zlabel("u(r,θ)")

# Solución Aproximada con Zernike
ax2 = fig.add_subplot(122, projection='3d')
ax2.plot_surface(X, Y, U_approx, cmap='plasma', edgecolor='none')
ax2.set_title("Aproximación con Zernike")
ax2.set_xlabel("X")
ax2.set_ylabel("Y")
ax2.set_zlabel("u(r,θ)")

plt.tight_layout()
plt.show()

