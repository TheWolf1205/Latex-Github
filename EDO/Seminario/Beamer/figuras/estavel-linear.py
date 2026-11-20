import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter

# ============================================================
# Sistema linealizado del péndulo amortiguado en (0,0)
#
#     theta' = omega
#     omega' = -theta - c*omega
#
# Elegimos 0 < c < 2 para obtener un sumidero tipo foco.
# ============================================================

c = 1

def campo(z):
    theta, omega = z
    return np.array([
        omega,
        -theta - c*omega
    ])


# ============================================================
# Parámetros de la animación
# ============================================================

dt = 0.03
T = 8
times = np.arange(0, T, dt)


# ============================================================
# Campo vectorial
# ============================================================

theta = np.linspace(-2, 2, 25)
omega = np.linspace(-2, 2, 25)

TH, OM = np.meshgrid(theta, omega)


# ============================================================
# Condiciones iniciales de las partículas
# ============================================================

initial_conditions = np.array([
    [1.7, 0.0],
    [1.2, 1.0],
    [0.3, 1.7],
    [-1.4, 0.5],
    [-1.6, -0.7],
    [-0.5, -1.5],
])


# ============================================================
# Integración mediante Runge-Kutta de orden 4
# ============================================================

trajectories = []

for z0 in initial_conditions:

    z = np.zeros((len(times), 2))
    z[0] = z0

    for n in range(len(times) - 1):

        x = z[n]

        k1 = campo(x)
        k2 = campo(x + dt*k1/2)
        k3 = campo(x + dt*k2/2)
        k4 = campo(x + dt*k3)

        z[n+1] = x + dt*(k1 + 2*k2 + 2*k3 + k4)/6

    trajectories.append(z)


# ============================================================
# Figura
# ============================================================

fig, ax = plt.subplots(figsize=(7, 7))

ax.streamplot(
    TH,
    OM,
    OM,
    -TH - c*OM,
    density=1.15,
    linewidth=0.8,
    arrowsize=1.0
)

# Equilibrio
ax.plot(
    0,
    0,
    "o",
    markersize=9,
    label=r"Equilibrio $(0,0)$"
)

ax.grid(False)

ax.axhline(0, linewidth=1)
ax.axvline(0, linewidth=1)

ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.spines["bottom"].set_visible(False)
ax.spines["left"].set_visible(False)

ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)

ax.set_xlabel(r"$\theta$")
ax.set_ylabel(r"$\omega$")

ax.set_title(
    r"Fluxo do sistema linearizado" "\n"
    r"$\theta'=\omega$"
    r" $\omega'=-\theta-c\omega$"
    + f"\n$c={c}$"
)

ax.set_aspect("equal")
ax.grid(True, alpha=0.25)


# ============================================================
# Objetos animados
# ============================================================

lines = []
particles = []

for _ in trajectories:
    line, = ax.plot([], [], linewidth=1.8)

    particle, = ax.plot(
        [], [],
        "o",
        markersize=6,
        color=line.get_color()
    )

    lines.append(line)
    particles.append(particle)

# ============================================================
# Inicialización
# ============================================================

def init():

    for line, particle in zip(lines, particles):

        line.set_data([], [])

        particle.set_data([], [])

    return lines + particles


# ============================================================
# Actualización de cada frame
# ============================================================

def update(frame):

    for trajectory, line, particle in zip(
        trajectories,
        lines,
        particles
    ):

        # Trayectoria recorrida hasta este instante
        line.set_data(
            trajectory[:frame+1, 0],
            trajectory[:frame+1, 1]
        )

        # Posición actual de la partícula
        particle.set_data(
            [trajectory[frame, 0]],
            [trajectory[frame, 1]]
        )

    return lines + particles


# ============================================================
# Crear animación
# ============================================================

animation = FuncAnimation(
    fig,
    update,
    frames=len(times),
    init_func=init,
    interval=30,
    blit=True
)


# ============================================================
# Guardar GIF
# ============================================================

gif_path = "pendulo_linearizado_estavel.gif"

animation.save(
    gif_path,
    writer=PillowWriter(fps=30)
)

plt.close(fig)

print(f"GIF guardado en: {gif_path}")
