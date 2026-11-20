import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Arc

fig, axes = plt.subplots(1, 2, figsize=(10, 5))

casos = [
    (axes[0], 0, r"Equilíbrio: $(0,0)$"),
    (axes[1], np.pi, r"Equilíbrio: $(\pi,0)$")
]

for ax, theta, titulo in casos:

    # Pivote y posición de la masa (radio = 1)
    pivote = np.array([0, 0])
    massa = np.array([np.sin(theta), -np.cos(theta)])

    # Ejes cartesianos centrados
    ax.axhline(0, color="black", linewidth=1.8, zorder=1)
    ax.axvline(0, color="black", linewidth=1.8, zorder=1)

    # Soporte del péndulo
    ax.plot([-0.35, 0.35], [0, 0], color="black",
            linewidth=4, solid_capstyle="round", zorder=2)

    # Varilla
    ax.plot(
        [pivote[0], massa[0]],
        [pivote[1], massa[1]],
        color="royalblue",
        linewidth=3,
        zorder=3
    )

    # Masa
    ax.add_patch(
        Circle(massa, radius=0.09,
               facecolor="darkorange",
               edgecolor="black",
               linewidth=1.2,
               zorder=4)
    )

    # Pivote
    ax.scatter(0, 0, color="black", s=25, zorder=5)

    # Etiquetas
    ax.text(
        massa[0] + 0.13,
        massa[1],
        r"$m$",
        fontsize=13,
        va="center"
    )

    ax.text(0.12, -0.55 if theta == 0 else 0.55,
            r"$r=1$", color="royalblue", fontsize=12)

    if theta == 0:
        ax.text(0.12, -0.22, r"$\theta=0$", fontsize=12)
    else:
        ax.add_patch(
            Arc((0, 0), 0.5, 0.5,
                theta1=-90, theta2=90,
                color="seagreen", linewidth=1.8)
        )
        ax.text(0.32, 0, r"$\theta=\pi$",
                color="seagreen", fontsize=12)

    ax.set_title(titulo, fontsize=13)

    # Configuración de los ejes
    ax.set_xlim(-0.8, 0.8)
    ax.set_ylim(-1.3, 1.3)
    ax.set_aspect("equal")

    ax.set_xticks([])
    ax.set_yticks([])

    # Quitar el marco exterior
    for spine in ax.spines.values():
        spine.set_visible(False)

fig.suptitle("Pêndulo", fontsize=15)

plt.tight_layout()
plt.savefig("pendulo.png", dpi=300, bbox_inches="tight")
plt.show()
