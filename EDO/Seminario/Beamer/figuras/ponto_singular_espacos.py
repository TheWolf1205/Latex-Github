
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter

# ============================================================
# Sistema:
#       x' = x
#       y' = -y
#
# E^u = span{(1,0)}: eje horizontal
# E^s = span{(0,1)}: eje vertical
# ============================================================

T = 3.0
dt = 0.03
times = np.arange(0, T + dt, dt)

# Condiciones iniciales
initial_conditions = np.array([
    [0.12, 1.35],
    [0, 1.5],
    [0, -1.5],
    [0.1, 0],
    [-0.1, 0],
    [0.25, -1.15],
    [-0.18, 1.05],
    [-0.30, -1.30],
    [0.45, 0.75],
    [-0.45, -0.75],
])

# Soluciones exactas:
# x(t) = x_0 exp(t)
# y(t) = y_0 exp(-t)

trajectories = []

for x0, y0 in initial_conditions:
    x = x0 * np.exp(times)
    y = y0 * np.exp(-times)
    trajectories.append(np.column_stack((x, y)))


# ============================================================
# Figura y campo vectorial
# ============================================================

xx = np.linspace(-1.6, 1.6, 25)
yy = np.linspace(-1.7, 1.7, 25)
X, Y = np.meshgrid(xx, yy)

fig, ax = plt.subplots(figsize=(8, 6))

ax.streamplot(
    X, Y,
    X, -Y,
    density=1.0,
    linewidth=0.8,
    arrowsize=0.9
)

# Subespacios estable e inestable
ax.axhline(
    0,
    linewidth=2,
    linestyle="--",
    label=r"$E^u=\operatorname{span}\{(1,0)\}$"
)

ax.axvline(
    0,
    linewidth=2,
    linestyle="--",
    label=r"$E^s=\operatorname{span}\{(0,1)\}$"
)

# Equilibrio
ax.plot(0, 0, "ko", markersize=5)

ax.set_xlim(-1.6, 1.6)
ax.set_ylim(-1.7, 1.7)
ax.set_aspect("equal", adjustable="box")

ax.set_xlabel(r"$x$")
ax.set_ylabel(r"$y$")

ax.set_title(
    r"Fluxo de $x'=x,\quad y'=-y$" "\n"
    r"$E^u$: direção instável;  $E^s$: direção estável"
)

ax.legend(loc="upper right", framealpha=0.95)

ax.grid(False)
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)


# ============================================================
# Partículas y trayectorias
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
# Actualización de la animación
# ============================================================

def update(i):
    for traj, line, particle in zip(
        trajectories, lines, particles
    ):
        line.set_data(
            traj[:i+1, 0],
            traj[:i+1, 1]
        )

        particle.set_data(
            [traj[i, 0]],
            [traj[i, 1]]
        )

    return lines + particles


# ============================================================
# Crear y guardar GIF
# ============================================================

ani = FuncAnimation(
    fig,
    update,
    frames=len(times),
    init_func=init,
    interval=35,
    blit=True
)

gif_path = "ponto_singular_espacos.gif"

ani.save(
    gif_path,
    writer=PillowWriter(fps=28)
)

plt.close(fig)

print(f"GIF guardado en: {gif_path}")
