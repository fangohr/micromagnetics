import numpy as np
import matplotlib.pyplot as plt
from fidimag.micro import Sim
from fidimag.micro import FDMesh
from fidimag.micro import Zeeman
from analytic_solution import macrospin_analytic_solution

# Material parameters
Ms = 8.6e5  # saturation magnetisation (A/m)
alpha = 0.1  # Gilbert damping
gamma = 2.211e5  # gyromagnetic ratio

# External magentic field.
B = 0.1  # (T)
mu0 = 4*np.pi*1e-7  # vacuum permeability
H = B/mu0

############
# Simulation
############
# Finite difference mesh.
mesh = FDMesh(nx=1, ny=1, dx=10, dy=10, unit_length=1e-9)

sim = Sim(mesh)
sim.Ms = Ms
sim.alpha = alpha
sim.gamma = gamma
sim.add(Zeeman((0, 0, H)))
sim.set_m((1, 0, 0))  # initial magnetisation

# Sampling time steps.
t_array = np.arange(0, 5e-9, 0.01e-9)

mx_simulation = []
for t in t_array:
    sim.run_until(t)
    m = sim.spin.reshape((len(sim.spin)/3, 3))
    mx_simulation.append(m[:, 0][0])


###################
# Analytic solution
###################
mx_analytic = macrospin_analytic_solution(alpha, gamma, H, t_array)

###################
# Plot comparison.
###################
plt.figure(figsize=(8, 5))
plt.plot(t_array/1e-9, mx_analytic, 'o', label='analytic')
plt.plot(t_array/1e-9, mx_simulation, linewidth=2, label='simulation')
plt.xlabel('t (ns)')
plt.ylabel('mx')
plt.grid()
plt.legend()
plt.savefig('macrospin.pdf', format='pdf', bbox_inches='tight')
