import numpy as np
import matplotlib.pyplot as plt
import argparse


def flux_surface(R0, delta, kappa, alpha):
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
    r = R0 / alpha
    R_s = R0 + r * np.cos(theta + (np.arcsin(delta) * np.sin(theta)))
    Z_s = kappa * r * np.sin(theta)

    return [R_s, Z_s]


def plot_surface(filename, ans, savefig=True):
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

    plt.savefig(filename)


def main():
    parser = argparse.ArgumentParser(
        prog="Miller",
        description="Takes some input and does some calcs!",
        epilog="Help arrived!!",
    )

    parser.add_argument("--filename", help="Help text")
    parser.add_argument(
        "-R", "--R0", help="Help text", default=2.5, type=float
    )  # positional argument
    parser.add_argument(
        "-D", "--delta", help="Help text", default=0.3, type=float
    )  # option that takes a value
    parser.add_argument("-K", "--kappa", help="Help text", default=1.5, type=float)
    parser.add_argument("-A", "--A", help="Help text", default=2.2, type=float)

    args = parser.parse_args()
    print(args.R0, args.delta, args.kappa, args.A)

    param = flux_surface(args.R0, args.delta, args.kappa, args.A)
    plot_surface(args.filename, param)


if __name__ == "__main__":
    main()
