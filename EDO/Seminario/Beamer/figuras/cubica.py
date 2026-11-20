
import numpy as np
import matplotlib.pyplot as plt

# ============================================================
# Función raíz cúbica
# ============================================================

x = np.linspace(-5, 5, 1000)
y = np.cbrt(x)

# ============================================================
# Figura
# ============================================================

fig, ax = plt.subplots(figsize=(10, 4.5))

ax.plot(x, y, linewidth=2, color="royalblue")

# Límites de los ejes
ax.set_xlim(-5, 5)
ax.set_ylim(-2, 2)

ax.set_box_aspect(0.4)

# Ejes cruzados en el origen
ax.spines["left"].set_position("zero")
ax.spines["bottom"].set_position("zero")

# Ocultar los bordes superior y derecho
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)

# Marcas cada unidad
ax.set_xticks(np.arange(-5, 6, 1))
ax.set_yticks(np.arange(-2, 3, 1))

# Cuadrícula
ax.grid(True, linestyle="-", linewidth=0.6, alpha=0.4)

# Etiquetas
ax.set_xlabel(r"$x$", loc="right")

ax.set_title(r"$f(x)=\sqrt[3]{x}$")

plt.tight_layout()

plt.savefig(
    "cubica.png",
    bbox_inches="tight",
    pad_inches=0.1,
    dpi=300
)
plt.show()

