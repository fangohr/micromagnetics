import numpy as np


def macrospin_analytic_solution(alpha, gamma, H, t_array):
    """
    Computes the analytic solution of magnetisation x component
    as a function of time for the macrospin in applied external
    magnetic field H.
    """
    t0 = 1/(gamma*alpha*H) * np.log(np.sin(np.pi/2)/(1+np.cos(np.pi/2)))
    mx_analytic = []
    for t in t_array:
        phi = gamma*H*t
        costheta = np.tanh(gamma*alpha*H*(t-t0))
        sintheta = 1/np.cosh(gamma*alpha*H*(t-t0))
        mx_analytic.append(sintheta*np.cos(phi))

    return np.array(mx_analytic)
