import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import MultipleLocator

# Configurar Matplotlib para usar LaTeX en los textos
plt.rcParams['text.usetex'] = True

# Definir la función a trozos
def h(t):
    # Primer trozo: 0 < t <= 0.5, la función es 0.5 - t
    # Segundo trozo: -0.5 < t < 0, la función es -0.5 - t
    # Usamos np.nan en las discontinuidades para que matplotlib no conecte esos puntos
    y = np.where((t > 0) & (t <= 0.5), 0.5 - t, 
                 np.where((t > -0.5) & (t < 0), -0.5 - t, np.nan))
    return y

# Asegurarse de incluir el punto (0,0) en los datos
t_extra = np.array([0])  # El punto adicional en t = 0
y_extra = np.array([0])  # El valor de la función en t = 0

# Definir el rango de valores para t
t = np.linspace(-0.5, 0.5, 400)

# Evaluar la función para cada valor de t
y = h(t)

# Concatenar el punto (0,0) en las listas de t y y
t = np.concatenate((t, t_extra))
y = np.concatenate((y, y_extra))

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
plt.gca().xaxis.set_minor_locator(MultipleLocator(0.2))
plt.gca().yaxis.set_minor_locator(MultipleLocator(0.2))

# Cuadrícula principal y menor
plt.grid(True, which='major', linestyle='--', color='gray', linewidth=0.5)
plt.grid(True, which='minor', linestyle=':', color='lightgray', linewidth=0.5)

# Graficar
plt.plot(t, y, label=r"Función $h(t)$", marker='o', linestyle='None')  # Solo puntos, sin línea

# Añadir título y etiquetas a los ejes con LaTeX
plt.xlabel(r"$t$", fontsize=12)
plt.ylabel(r"$h(t)$", fontsize=12)

# Mostrar la leyenda con LaTeX
plt.legend()

# Guardar la gráfica en un archivo con LaTeX
plt.savefig('grafica_h_tiks.png', dpi=300, bbox_inches='tight')

# Mostrar la gráfica
plt.show()

