import numpy as np
import matplotlib.pyplot as plt


def flux_surface(R0, delta, kappa, A):
    """flux_surface

    Args
    ---------
    R0:
    r:
    theta:
    delta:
    kappa:

    """

    theta = np.linspace(0, 2 * np.pi)
    r = R0 / A
    R_s = R0 + r * np.cos(theta + (np.arcsin(delta) * np.sin(theta)))
    Z_s = kappa * r * np.sin(theta)

    return [R_s, Z_s]


def plot_surface(ans, savefig=True):
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

    plt.savefig("miller.png")


def main():
    A = 2.2
    kappa = 1.5
    delta = 0.3
    R0 = 2.5

    param = flux_surface(R0, delta, kappa, A)
    plot_surface(param)


if __name__ == "__main__":
    main()
