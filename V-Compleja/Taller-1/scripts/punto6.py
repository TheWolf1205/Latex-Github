import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import MultipleLocator

# Definir las raíces cuartas de i
k_values = range(4)
roots = [np.sqrt(2)*np.exp(1j * (-np.pi + 2 * k * np.pi) / 6) for k in k_values]

# Extraer partes reales e imaginarias para graficar
real_parts = [z.real for z in roots]
imag_parts = [z.imag for z in roots]

# Etiquetas con fracciones en formato LaTeX
labels = [f'$\\sqrt{{2}}e^{{i\\frac{{-\\pi + 2 \\times {k} \\pi}}{{6}}}}$' for k in k_values]

# Crear la figura y el gráfico
fig, ax = plt.subplots(figsize=(8, 8))

# Configurar los ejes para que crucen en el origen
ax.axhline(0, color='black', linewidth=1.5)
ax.axvline(0, color='black', linewidth=1.5)

# Graficar los puntos en el plano complejo
ax.scatter(real_parts, imag_parts, color='blue')

# Etiquetas para los puntos con fondo negro y texto blanco
for i, txt in enumerate(labels):
    ax.annotate(
        txt, 
        (real_parts[i], imag_parts[i]), 
        textcoords="offset points",
        xytext=(10,10), 
        ha='center', 
        color='white',
        bbox=dict(facecolor='black', edgecolor='none', boxstyle='round,pad=0.3')
    )

# Configurar los límites de los ejes
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)

# Colocar los números en los ejes de 0.5 en 0.5
ax.set_xticks(np.arange(-1.5, 1.6, 0.5))
ax.set_yticks(np.arange(-1.5, 1.6, 0.5))

# Configurar las líneas de cuadrícula menor cada 0.1
ax.xaxis.set_minor_locator(MultipleLocator(0.1))
ax.yaxis.set_minor_locator(MultipleLocator(0.1))

# Cuadrícula principal y menor
ax.grid(True, which='major', linestyle='--', color='gray', linewidth=0.5)
ax.grid(True, which='minor', linestyle=':', color='lightgray', linewidth=0.5)

# Etiquetas para los ejes
ax.set_xlabel('Parte Real')
ax.set_ylabel('Parte Imaginaria')

# Título
ax.set_title('Raíces cuartas de $-2+2i\\sqrt{{3}}$ en el plano complejo')

# Guardar la figura
fig.savefig('grafico_raices_cuartas_-2+2isqrt3.png', dpi=300, bbox_inches='tight')  # Guardar la imagen con calidad

plt.show()
