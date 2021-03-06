import numpy as np
import matplotlib.pyplot as plt
from analytic_solution import macrospin_analytic_solution

# Material parameters
Ms = 8.6e5  # saturation magnetisation (A/m)
alpha = 0.1  # Gilbert damping
gamma = 2.211e5  # gyromagnetic ratio

# External magentic field.
B = 0.1  # (T)
mu0 = 4 * np.pi * 1e-7  # vacuum permeability
H = B / mu0
# meaningful time period is of order of nano seconds
t_array = np.arange(0, 5e-9, 0.01e-9)

############
# Simulation
############
#
# Simulation code
# goes here.
#

# results for m_x at times t_array in
mx_simulation = np.zeros(t_array.shape)

###################
# Analytic solution
###################
mx_analytic = macrospin_analytic_solution(alpha, gamma, H, t_array)

###################
# Plot comparison.
###################
plt.figure(figsize=(8, 5))
plt.plot(t_array / 1e-9, mx_analytic, 'o', label='analytic')
plt.plot(t_array / 1e-9, mx_simulation, linewidth=2, label='simulation')
plt.xlabel('t (ns)')
plt.ylabel('mx')
plt.grid()
plt.legend()
plt.savefig('macrospin.pdf', format='pdf', bbox_inches='tight')
