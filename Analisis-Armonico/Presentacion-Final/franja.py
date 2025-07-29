import matplotlib.pyplot as plt
import numpy as np

# Crear los datos para los ejes
x = np.linspace(-2, 2, 400)
y = np.linspace(-2, 2, 400)
X, Y = np.meshgrid(x, y)

# Crear la figura y el eje
fig, ax = plt.subplots()

# Dibujar las líneas de los ejes x e y
ax.axhline(0, color='black', linewidth=1)
ax.axvline(0, color='black', linewidth=1)

# Rellenar la franja 0 ≤ x ≤ 1 en el gráfico
ax.fill_betweenx(y, 0, 1, color='skyblue', alpha=0.5)

# Agregar un borde en x = 1
ax.plot([1, 1], [-2, 2], color='blue', linewidth=2)
ax.plot([0, 0], [-2, 2], color='blue', linewidth=2)

# Establecer límites de los ejes
ax.set_xlim([-2, 2])
ax.set_ylim([-2, 2])

# Añadir nombres a los ejes
ax.set_xlabel('x', rotation=0, fontsize=12)
ax.set_ylabel('y', rotation=0, fontsize=12)

# Mover los números indicadores sobre los ejes (estilo gráfico matemático)
ax.spines['left'].set_position('zero')
ax.spines['bottom'].set_position('zero')
ax.spines['top'].set_color('none')
ax.spines['right'].set_color('none')

ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')

ax.xaxis.set_label_coords(1.05, 0.5)
ax.yaxis.set_label_coords(0.5, 1.05)

# Guardar la imagen
plt.savefig('grafica_con_nombres_y_borde.png')

# Mostrar la gráfica
plt.show()

