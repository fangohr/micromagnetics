import numpy as np


def domainwall_analytic_solution(A, K, d, n_points):
    """
    Computes Neel domain wall magnetisation x component
    in absence of an external magnetic field.
    """
    x_array = np.linspace(0, d, n_points)
    mx_analytic = -np.tanh((x_array - d / 2.) / np.sqrt(A / K))

    return mx_analytic
