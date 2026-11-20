
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter

# ==================================================
# 1. PARAMETROS Y CONDICIONES INICIALES
# ==================================================

c = 0.3         # Coeficiente de amortiguamiento
theta0 = 1.5+np.pi     # Angulo inicial
omega0 = -1.615     # Velocidad angular inicial

T = 30               # Tiempo total de simulacion
dt = 0.03               # Paso temporal

# Longitud del pendulo
r = 1.0

# ==================================================
# 2. SISTEMA DIFERENCIAL
# ==================================================

def campo(z):
    theta, omega = z

    return np.array([
        omega,
        -np.sin(theta) - c*omega
    ])

# ==================================================
# 3. METODO RUNGE-KUTTA DE ORDEN 4
# ==================================================

def rk4(z, dt):
    k1 = campo(z)
    k2 = campo(z + dt*k1/2)
    k3 = campo(z + dt*k2/2)
    k4 = campo(z + dt*k3)

    return z + dt*(k1 + 2*k2 + 2*k3 + k4)/6

# ==================================================
# 4. CALCULO DE LA SOLUCION
# ==================================================

times = np.arange(0, T + dt, dt)

sol = np.zeros((len(times), 2))
sol[0] = [theta0, omega0]

for i in range(len(times)-1):
    sol[i+1] = rk4(sol[i], dt)

theta = sol[:, 0]

# Posicion de la masa
x = r*np.sin(theta)
y = -r*np.cos(theta)

# ==================================================
# 5. CONFIGURACION DE LA FIGURA
# ==================================================

fig, ax = plt.subplots(figsize=(6, 6))

ax.set_xlim(-1.4, 1.4)
ax.set_ylim(-1.4, 1.4)
ax.set_aspect("equal")

# Ejes centrados
ax.axhline(0, color="black", linewidth=1.5, zorder=0)
ax.axvline(0, color="black", linewidth=1.5, zorder=0)

# Ocultar marco exterior
for spine in ax.spines.values():
    spine.set_visible(False)

ax.set_xticks([])
ax.set_yticks([])

# Soporte
ax.plot(
    [-0.2, 0.2], [0, 0],
    color="black", linewidth=5,
    solid_capstyle="round"
)

# Pivote
ax.plot(0, 0, "ko", markersize=6, zorder=5)

# Varilla
rod, = ax.plot([], [], color="royalblue", linewidth=3)

# Masa
mass, = ax.plot(
    [], [], "o",
    color="darkorange",
    markeredgecolor="black",
    markersize=17
)

# Trayectoria de la masa
trail, = ax.plot(
    [], [],
    color="gray",
    linewidth=1,
    alpha=0.6
)

# Texto con el tiempo y el angulo
info = ax.text(
    0.03, 0.95, "",
    transform=ax.transAxes,
    fontsize=11,
    verticalalignment="top"
)

ax.set_title("Movimento do pêndulo", fontsize=14)

# ==================================================
# 6. FUNCIONES DE ANIMACION
# ==================================================

def init():
    rod.set_data([], [])
    mass.set_data([], [])
    trail.set_data([], [])
    info.set_text("")

    return rod, mass, trail, info


def update(i):

    # Posicion actual de la masa
    xi = x[i]
    yi = y[i]

    # Actualizar varilla
    rod.set_data([0, xi], [0, yi])

    # Actualizar masa
    mass.set_data([xi], [yi])

    # Actualizar trayectoria
    trail.set_data(x[:i+1], y[:i+1])

    # Informacion
    info.set_text(
        rf"$t={times[i]:.2f}$" + "\n" +
        rf"$\theta={theta[i]:.2f}$"
    )

    return rod, mass, trail, info


# ==================================================
# 7. CREAR Y MOSTRAR ANIMACION
# ==================================================

ani = FuncAnimation(
    fig,
    update,
    frames=len(times),
    init_func=init,
    interval=30,
    blit=True
)

plt.show()

# ==================================================
# 8. GUARDAR COMO GIF (OPCIONAL)
# ==================================================

ani.save(
    "pendulo_animado.gif",
    writer=PillowWriter(fps=30)
)

