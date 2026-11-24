"""
Generate the continuity equation intuition figure into ../figures/.
"""

from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np

FIGURE_DIRECTORY = Path(__file__).resolve().parent.parent / "figures"

def figure_trajectories():
    """
    Plot an illustrative figure of a collection of trajectories in (sigma, x) space
    """
    c_start = 1
    sigma_start = np.pi

    def x(c, sigma):
        return c*np.exp(np.sin(sigma))


    def v(x, sigma):
        return x*np.cos(sigma)

    x_start = x(c_start, sigma_start)
    sigma_grid = np.linspace(0, 2*sigma_start, 500)
    c_grid = np.geomspace(0.1, 15, 40)

    fig, ax = plt.subplots(figsize=(7, 4), dpi=200)

    for c in c_grid:
        ax.plot(sigma_grid, x(c, sigma_grid), color="grey", alpha=0.3)

    ax.plot(sigma_grid, x(c_start, sigma_grid), label=r"$a(\sigma)$")
    ax.plot(sigma_start, x_start, "o", color="black")
    ax.annotate(r"$(\sigma^*, x^*)$", (sigma_start, x_start), xytext=(5, 5), textcoords="offset points")
    ax.annotate("", xy=(sigma_start + 0.5, x_start + 0.5*v(x_start, sigma_start)), xytext=(sigma_start, x_start), arrowprops=dict(arrowstyle="->", color="black", lw=1.5))
    ax.annotate(r"$dx/d\sigma = v(x^*, \sigma^*)$", (sigma_start, x_start), xytext=(-6, -6), textcoords="offset points", ha="right", va="top")    
    ax.fill_between(sigma_grid, 0, x(c_start, sigma_grid), color="C0", alpha=0.1, zorder=0)
    ax.set_xlim(0, 2*np.pi)
    ax.set_ylim(0, 5.5)
    ax.set(xlabel=r"$\sigma$", ylabel=r"$x$")
    ax.legend()
    
    fig.savefig(FIGURE_DIRECTORY / "continuity-equation-trajectories.png")
    plt.close(fig)


def main():
    figure_trajectories()

if __name__ == "__main__":
    main()
