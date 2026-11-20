
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter

# ============================================================
# Sistema não linear do pêndulo amortecido em (0,0)
#
#     theta' = omega
#     omega' = -sin(theta) - c*omega
#
# Escolhemos c = 1.
# ============================================================

c = 0.3

def campo(z):
    theta, omega = z
    return np.array([
        omega,
        -np.sin(theta) - c*omega
    ])


# ============================================================
# Parâmetros da animação
# ============================================================

dt = 0.03
T = 30
times = np.arange(0, T, dt)


# ============================================================
# Campo vetorial
# ============================================================

theta = np.linspace(-2, 2, 25)
omega = np.linspace(-2, 2, 25)

TH, OM = np.meshgrid(theta, omega)


# ============================================================
# Condições iniciais das partículas
# ============================================================

initial_conditions = np.array([
    [1.8, -1.8],
])


# ============================================================
# Integração mediante Runge-Kutta de ordem 4
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
    -np.sin(TH) - c*OM,
    density=1.15,
    linewidth=0.8,
    arrowsize=1.0
)

# Equilíbrio
ax.plot(
    0,
    0,
    "o",
    markersize=9,
    label=r"Equilíbrio $(0,0)$"
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
    r"Fluxo do sistema não linear" "\n"
    r"$\theta'=\omega$"
    r" $\omega'=-\sin(\theta)-c\omega$"
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
# Inicialização
# ============================================================

def init():

    for line, particle in zip(lines, particles):

        line.set_data([], [])
        particle.set_data([], [])

    return lines + particles


# ============================================================
# Atualização de cada frame
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
# Criar animação
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

gif_path = "pendulo_nao_linear_estavel.gif"

animation.save(
    gif_path,
    writer=PillowWriter(fps=30)
)

plt.close(fig)

print(f"GIF guardado em: {gif_path}")

