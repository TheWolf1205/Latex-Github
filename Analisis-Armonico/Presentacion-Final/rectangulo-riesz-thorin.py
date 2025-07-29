import matplotlib.pyplot as plt
import numpy as np

# Crear la figura y ajustar el tamaño para que sea cuadrada
fig, ax = plt.subplots(figsize=(6, 6))

# Dibujar el rectángulo
rect = plt.Rectangle((0, 0), 1, 1, edgecolor='black', facecolor='none', linewidth=1)
ax.add_patch(rect)

# Dibujar el segmento de línea diagonal
x_values = [0.2, 0.5, 0.8]  # Ajustados para que se vea mejor
y_values = [0.8, 0.5, 0.2]
ax.plot(x_values, y_values, color='black', marker='o', markersize=5)

# Etiquetas de los puntos
ax.text(0.2, 0.8, r'$\left(\frac{1}{p_0}, \frac{1}{q_0}\right)$', fontsize=14, ha='left', va='bottom')
ax.text(0.5, 0.5, r'$\left(\frac{1}{p_{\theta}}, \frac{1}{q_{\theta}}\right)$', fontsize=14, ha='left', va='bottom')
ax.text(0.8, 0.2, r'$\left(\frac{1}{p_1}, \frac{1}{q_1}\right)$', fontsize=14, ha='right', va='top')

# Configurar límites y etiquetas de los ejes
ax.set_xlim(-0.1, 1.1)
ax.set_ylim(-0.1, 1.1)
ax.set_xlabel(r'$\frac{1}{p}$', fontsize=16, rotation=0)
ax.set_ylabel(r'$\frac{1}{q}$', fontsize=16, rotation=0)

ax.set_xticks([0, 1])
ax.set_yticks([0, 1])

# Personalizar los ejes
ax.spines['left'].set_position('zero')
ax.spines['bottom'].set_position('zero')
ax.spines['top'].set_color('none')
ax.spines['right'].set_color('none')

ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')

ax.xaxis.set_label_coords(1.05, 0.1)
ax.yaxis.set_label_coords(0.1, 1.05)


# Ajustar la relación de aspecto para que sea igual en ambos ejes
ax.set_aspect('equal')

# Mostrar la gráfica
plt.show()

