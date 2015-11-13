import numpy as np
import matplotlib.pyplot as plt
from fidimag.micro import Sim
from fidimag.micro import FDMesh
from fidimag.micro import UniformExchange
from fidimag.micro import UniaxialAnisotropy
from analytic_solution import domain_wall_analytic_solution

# Material parameters
Ms = 8.6e5  # saturation magnetisation (A/m)
A = 1.3e-11  # exchange energy constant (J/m)
K = 5e3  # uniaxial anisotropy (J/m**3)
alpha = 5  # Gilbert damping
gamma = 2.211e5  # gyromagnetic ratio

############
# Simulation
############
# Finite difference 1D mesh.
mesh = FDMesh(nx=500, ny=1, nz=1, dx=2, dy=2, dz=2, unit_length=1e-9)


# Initial magnetisation function.
def init_m(pos):
    x = pos[0]
    if x < 450:
        return (1, 0, 0)
    elif 450 <= x < 550:
        return (0, 1, 1)
    else:
        return (-1, 0, 0)

sim = Sim(mesh)
sim.alpha = alpha
sim.gamma = gamma
sim.Ms = Ms
sim.add(UniformExchange(A))
sim.add(UniaxialAnisotropy(K))
sim.set_m(init_m)
sim.relax(dt=1e-13, stopping_dmdt=0.001, max_steps=5000)

# Magnetisation x component.
mx_simulation = sim.spin.reshape((len(sim.spin)/3, 3))[:, 0]

###################
# Analytic solution
###################
d = 1000e-9  # sample length (nm)
n_points = 500
mx_analytic = domain_wall_analytic_solution(A, K, d, n_points)

###################
# Plot solutions
###################
plt.figure(figsize=(8, 5))
x_array = np.linspace(0, d, n_points)
plt.plot(x_array/1e-9, mx_simulation, 'o', label='simulation')
plt.plot(x_array/1e-9, mx_analytic, linewidth=2, label='analytic')
plt.xlabel('x (nm)')
plt.ylabel('mx')
plt.grid()
plt.legend()
plt.savefig('domain_wall.pdf', format='pdf', bbox_inches='tight')
