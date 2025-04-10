import numpy as np
import matplotlib.pyplot as plt

def funcion_a_trozos(x, a):
    f = np.where((0 <= x) & (x <= 1 - (1 / (2 * a))), 0, np.nan)
    g = np.where((1 + (1 / (2 * a)) <= x) & (x <= 2), 0, np.nan)
    h = np.where((1 - (1 / (2 * a)) <= x) & (x <= 1), 2 * a**2 * x - 2 * a**2 + a, np.nan)
    p = np.where((1 <= x) & (x <= 1 + (1 / (2 * a))), -2 * a**2 * x + 2 * a**2 + a, np.nan)
    
    return np.nan_to_num(f, nan=0) + np.nan_to_num(g, nan=0) + np.nan_to_num(h, nan=0) + np.nan_to_num(p, nan=0)

# Rango de valores x
x = np.linspace(0, 2, 1000)

# Valores de a
valores_de_a = [1, 2, 5, 10]

# Crear la gráfica
plt.figure(figsize=(10, 6))
for a in valores_de_a:
    y = funcion_a_trozos(x, a)
    plt.plot(x, y, label=f'k = {a}')

plt.title('$f_{k}(x)$')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid(True)
plt.legend()
plt.show()

