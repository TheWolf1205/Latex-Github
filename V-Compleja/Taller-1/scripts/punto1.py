import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import MultipleLocator

# Definir los números complejos
z1 = -2 - 1j
z2 = -4 + 3j
z3 = (-7/5) - (1j/5)

# Extraer partes reales e imaginarias para graficar
real_parts = [z1.real, z2.real, z3.real]
imag_parts = [z1.imag, z2.imag, z3.imag]
labels = ['-2-i', '-4+3i', '$-\\frac{{7}}{{5}}-\\frac{{i}}{{5}}$']

# Crear la figura y el gráfico
plt.figure(figsize=(8, 8))

# Configurar los ejes para que crucen en el origen
plt.axhline(0, color='black',linewidth=1.5)
plt.axvline(0, color='black',linewidth=1.5)

# Graficar los puntos en el plano complejo
plt.scatter(real_parts, imag_parts, color='red')

# Etiquetas para los puntos con fondo negro y texto blanco
for i, txt in enumerate(labels):
    plt.annotate(
        txt, 
        (real_parts[i], imag_parts[i]), 
        textcoords="offset points",
        xytext=(15,15), 
        ha='center', 
        color='white',
        bbox=dict(facecolor='black', edgecolor='none', boxstyle='round,pad=0.3')
    )

# Configurar los límites de los ejes
plt.xlim(-5, 5)
plt.ylim(-5, 5)

# Colocar los números en los ejes de 1 en 1
plt.xticks(range(-5, 6, 1))
plt.yticks(range(-5, 6, 1))

# Configurar las líneas de cuadrícula menor cada 0.2
plt.gca().xaxis.set_minor_locator(MultipleLocator(0.2))
plt.gca().yaxis.set_minor_locator(MultipleLocator(0.2))

# Cuadrícula principal y menor
plt.grid(True, which='major', linestyle='--', color='gray', linewidth=0.5)
plt.grid(True, which='minor', linestyle=':', color='lightgray', linewidth=0.5)

# Etiquetas para los ejes
plt.xlabel('x (Parte Real)')
plt.ylabel('y (Parte Imaginaria)')

# Cuadrícula
plt.grid(True, which='both', linestyle='--', color='gray', linewidth=0.5)

# Título
plt.title('Representación en el plano complejo')

# Guardar
plt.savefig('grafico_punto_1.png', dpi=300, bbox_inches='tight')  # dpi ajusta la calidad


plt.show()
