import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator

# Definir la función (h * D_N)(t) usando la forma compleja
def h_DN(t, N):
    sumatoria = np.zeros_like(t, dtype=complex)
    for m in range(-N, N + 1):
        if m != 0:
            sumatoria += np.exp(2j * np.pi * m * t) / m
    return -1j / (2 * np.pi) * sumatoria

# Pedir al usuario el grado de la serie de Fourier
N = int(input("Grado de la serie de Fourier: "))

# Valores de t para graficar
t = np.linspace(-0.5, 0.5, 1000)

# Evaluar la aproximación de Fourier
fourier_values = h_DN(t, N).real  # Tomamos solo la parte real

# Crear la figura
plt.figure(figsize=(8, 5))

# Configurar los ejes para que crucen en el origen
plt.axhline(0, color='black', linewidth=1.5)
plt.axvline(0, color='black', linewidth=1.5)

# Configurar los límites de los ejes
plt.xlim(-0.6, 0.6)
plt.ylim(-0.6, 0.6)

# Colocar los números en los ejes de 0.2 en 0.2
plt.xticks(np.arange(-0.6, 0.7, 0.2))
plt.yticks(np.arange(-0.6, 0.7, 0.2))

# Configurar las líneas de cuadrícula menor cada 0.2
plt.gca().xaxis.set_minor_locator(MultipleLocator(0.02))
plt.gca().yaxis.set_minor_locator(MultipleLocator(0.02))

# Cuadrícula principal y menor
plt.grid(True, which='major', linestyle='--', color='gray', linewidth=0.5)
plt.grid(True, which='minor', linestyle=':', color='lightgray', linewidth=0.5)

# Graficar la aproximación de Fourier
plt.plot(t, fourier_values, label=rf"$(h * D_{{{N}}})(t)$", linestyle='dashed', color='red')

# Configurar los ejes
plt.xlabel(r"$t$")
plt.ylabel(r"$(h * D_N)(t)$")
plt.legend()

# Mostrar la gráfica
plt.show()
