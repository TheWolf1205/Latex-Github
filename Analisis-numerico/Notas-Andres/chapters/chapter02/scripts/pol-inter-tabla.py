import matplotlib.pyplot as plt
import numpy as np

# Datos de ejemplo
x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
y = np.array([1.3, 3.5, 4.2, 5.0, 7.0, 8.8, 10.1, 12.5, 13.0, 15.6])

# Obtener el polinomio de interpolación de grado 9
coeficientes = np.polyfit(x, y, 9)  # Ajuste polinómico de grado 9
polinomio = np.poly1d(coeficientes)  # Crear el polinomio

# Puntos para graficar el polinomio de interpolación
x_fit = np.linspace(min(x), max(x), 100)  # Valores suaves para la curva
y_fit = polinomio(x_fit)

# Crear la figura y ejes
fig, ax = plt.subplots(figsize=(5, 5))

# Graficar los puntos
ax.scatter(x, y, color='blue', s=20, label="Datos")

# Graficar el polinomio de interpolación
ax.plot(x_fit, y_fit, 'r-', label="Interpolación de grado 9")

# Configurar límites y ticks
ax.set_xlim(-1, 12)
ax.set_ylim(-1, 22)
ax.set_xticks(np.arange(2, 12, 2))
ax.set_yticks(np.arange(2, 22, 2))

# Estilo de los ejes
ax.spines['left'].set_position(('data', 0))
ax.spines['bottom'].set_position(('data', 0))
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

# Flechas en los ejes
ax.plot(1.0, 0, ">k", transform=ax.get_yaxis_transform(), clip_on=False)
ax.plot(0, 1.0, "^k", transform=ax.get_xaxis_transform(), clip_on=False)

# Etiquetas de los ejes
ax.text(12.5, -0.5, r'$x$', fontsize=14)
ax.text(-0.5, 22, r'$y$', fontsize=14)

# Quitar la cuadrícula
ax.grid(False)

# Agregar leyenda
ax.legend()

plt.savefig("tabla-interpolacion")
plt.show()

