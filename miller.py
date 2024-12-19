from numpy import *

A = 2.2
kappa = 1.5
delta = 0.3
R0 = 2.5
theta = linspace(0, 2 * pi)
r = R0 / A
R_s = R0 + r * cos(theta + (arcsin(delta) * sin(theta)))
Z_s = kappa * r * sin(theta)

import matplotlib.pyplot as plt

def flux_surface(R0, r, theta, delta, kappa):
    """flux_surface
    
    Args
    ---------
    R0: 
    r: 
    theta: 
    delta: 
    kappa:

    """

    R_s = R0 + r*cos(theta + (arcsin(delta))*sin(theta))
    Z_s = r*kappa*sin(theta)

    return [R_s, Z_s]

def plot_surface(ans, savefig = True):
    """plot_surface
    
    Args
    ---------
    ans:
        A list containing to lists
        ans[0]: R_s
        ans[1]: Z_s

    """

    R_s = ans[0]
    Z_s = ans[1]

    plt.plot(R_s, Z_s)
    plt.axis("equal")
    plt.xlabel("R [m]")
    plt.ylabel("Z [m]")
    
    plt.savefig(
        "miller.png"
    )

def main(R0, r, theta, delta, kappa):

    param = flux_surface(R0, r, theta, delta, kappa)
    plot_surface(param)

if __name__ == "__main__":
    main(R0, r, theta, delta, kappa)