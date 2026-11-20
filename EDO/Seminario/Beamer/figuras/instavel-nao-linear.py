
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter

# ============================================================
# Sistema nao linear do pendulo amortecido em (pi,0)
#
# u = theta - pi
#
#       u' = omega
#       omega' = sin(u) - c*omega
#
# A singularidade original (pi,0) aparece em (0,0).
# ============================================================

c = 0.3

def campo(z):
    u, omega = z
    return np.array([
        omega,
        np.sin(u) - c*omega
    ])


# ============================================================
# Parametros da animacao
# ============================================================

dt = 0.03
T = 30
times = np.arange(0, T, dt)


# ============================================================
# Campo vetorial
# ============================================================

u = np.linspace(-2, 2, 25)
omega = np.linspace(-2, 2, 25)

U, OM = np.meshgrid(u, omega)


# ============================================================
# Condicoes iniciais das particulas
# ============================================================

initial_conditions = np.array([
    [1.5,-1.614],
])

# ============================================================
# Integracao mediante Runge-Kutta de ordem 4
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
    U,
    OM,
    OM,
    np.sin(U) - c*OM,
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
    label=r"Equilibrio $(\pi,0)$"
)

ax.axhline(0, linewidth=1)
ax.axvline(0, linewidth=1)

ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.spines["bottom"].set_visible(False)
ax.spines["left"].set_visible(False)

ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)

ax.set_xlabel(r"$u=\theta-\pi$")
ax.set_ylabel(r"$\omega$")

ax.set_title(
    r"Fluxo do sistema não linear" "\n"
    r"$u'=\omega$" "\n"
    r"$\omega'=\sin(u)-c\omega$" "\n"
    rf"$c={c}$"
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
# Inicializacao
# ============================================================

def init():

    for line, particle in zip(lines, particles):

        line.set_data([], [])
        particle.set_data([], [])

    return lines + particles


# ============================================================
# Atualizacao de cada frame
# ============================================================

def update(frame):

    for trajectory, line, particle in zip(
        trajectories,
        lines,
        particles
    ):

        line.set_data(
            trajectory[:frame+1, 0],
            trajectory[:frame+1, 1]
        )

        particle.set_data(
            [trajectory[frame, 0]],
            [trajectory[frame, 1]]
        )

    return lines + particles


# ============================================================
# Criar animacao
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
# Salvar GIF
# ============================================================

gif_path = "pendulo_nao_linear_instavel.gif"

animation.save(
    gif_path,
    writer=PillowWriter(fps=30)
)

plt.close(fig)

print(f"GIF guardado em: {gif_path}")

