"""
Generate the Tweedie verification figures into ../figures/.
"""

from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm, gaussian_kde

FIGURE_DIRECTORY = Path(__file__).resolve().parent.parent / "figures"
SEED = 0
MUS = [-2, 1]
SIGMAS = [0.5, 1]
WEIGHTS = [0.3, 0.7]
SIGMA = 1
N_SAMPLES = 5000

class Gaussian:
    def __init__(self, mu, sigma):
        self.mu = mu
        self.sigma = sigma

    def posterior(self, x_sigma, sigma):
        precision_posterior = (1/sigma**2) + (1/self.sigma**2)
        variance_posterior = 1/precision_posterior
        sigma_posterior = np.sqrt(variance_posterior)
        mu_posterior = variance_posterior * (x_sigma/sigma**2 + self.mu/self.sigma**2)
        return Gaussian(mu_posterior, sigma_posterior)

    def noised(self, sigma):
        return Gaussian(self.mu, np.sqrt(self.sigma**2 + sigma**2))
    
    def density(self, x_sigma):
        return norm.pdf(x_sigma, self.mu, self.sigma)

    def derivative(self, x_sigma):
        return -((x_sigma - self.mu)/self.sigma**2)*self.density(x_sigma)

    def sample(self, rng):
        return rng.normal(self.mu, self.sigma)

class TwoComponentGaussianMixture:
    def __init__(self, gaussians, weights):
        self.weights = np.asarray(weights, dtype=float)
        self.gaussians = list(gaussians)
        if not (len(self.gaussians) == 2 and self.weights.shape == (2,)):
            raise ValueError("gaussians and weights must all have exactly 2 entries")
        if not all(isinstance(g, Gaussian) for g in self.gaussians):
            raise TypeError("gaussians must all be Gaussian objects")
    
    def posterior(self, x_sigma, sigma):
        posterior_gaussians = [self.gaussians[0].posterior(x_sigma, sigma), self.gaussians[1].posterior(x_sigma, sigma)]
        densities = [self.gaussians[0].noised(sigma).density(x_sigma), self.gaussians[1].noised(sigma).density(x_sigma)]
        weighted = self.weights * densities
        posterior_weights = weighted / weighted.sum()
        return  TwoComponentGaussianMixture(posterior_gaussians, posterior_weights)

    def mean(self):
        return self.weights[0]*self.gaussians[0].mu + self.weights[1]*self.gaussians[1].mu

    def noised(self, sigma):
        return TwoComponentGaussianMixture(
            [self.gaussians[0].noised(sigma), self.gaussians[1].noised(sigma)],
            self.weights
        )

    def density(self, x_sigma):
        return self.weights[0]*self.gaussians[0].density(x_sigma) + self.weights[1]*self.gaussians[1].density(x_sigma)
    
    def derivative(self, x_sigma):
        return self.weights[0]*self.gaussians[0].derivative(x_sigma) + self.weights[1]*self.gaussians[1].derivative(x_sigma)

    def sample(self, n, rng):
        components = rng.choice(2, size=n, p=self.weights)
        gaussian_choice = [self.gaussians[i] for i in components]
        sample = [gaussian.sample(rng) for gaussian in gaussian_choice]
        return sample

class GaussianKDE:
    def __init__(self, samples):
        self.kde = gaussian_kde(samples)

    def density(self, x_sigma):
        return self.kde(x_sigma)

    def derivative(self, x_sigma):
        """
        Only valid on a sorted, finely spaced grid of points.
        """
        return np.gradient(self.density(x_sigma), x_sigma)

def tweedie(p_sigma, x_sigma, sigma):
    return x_sigma + sigma**2 * p_sigma.derivative(x_sigma) / p_sigma.density(x_sigma)

def make_x_sigma_grid(mixture, width=3, n_points=500):
    mus = [mixture.gaussians[0].mu, mixture.gaussians[1].mu]
    sigmas = [mixture.gaussians[0].sigma, mixture.gaussians[1].sigma]
    return np.linspace(
        np.min(mus) - width*np.max(sigmas),
        np.max(mus) + width*np.max(sigmas),
        n_points
    )

def bayes_tweedie_comparison(mixture, sigma=1):
    """
    Plot the posterior mean from Bayes' rule and Tweedie's formula for a given Gaussian mixture.
    """
    noised_mixture = mixture.noised(sigma)
    x_sigma_grid = make_x_sigma_grid(noised_mixture)

    posteriors = [mixture.posterior(x, sigma) for x in x_sigma_grid]
    posterior_means = np.array([posterior.mean() for posterior in posteriors])

    tweedie_means = tweedie(
        noised_mixture,
        x_sigma_grid,
        sigma
    )

    fig, ax = plt.subplots(figsize=(7, 4), dpi=200)
    ax.plot(x_sigma_grid, posterior_means, lw=2, label="Bayes")
    ax.plot(x_sigma_grid, tweedie_means, ls="--", label="Tweedie")
    ax.legend(loc="upper left", frameon=False)
    ax.set(xlim=(x_sigma_grid[0], x_sigma_grid[-1]), xlabel=r"$x_\sigma$", ylabel=r"$\mathbb{E}[x_0 \mid x_\sigma]$")
    fig.savefig(FIGURE_DIRECTORY / "bayes-tweedie-comparison.png")
    plt.show()

def kde_tweedie_comparison(mixture, rng, n=5000, sigma=1):
    """
    Plot Tweedie's formula for an exact density and a KDE of the same density.
    """
    noised_mixture = mixture.noised(sigma)
    x_sigma_grid = make_x_sigma_grid(noised_mixture)

    tweedie_means = tweedie(
        noised_mixture,
        x_sigma_grid,
        sigma
    )

    samples = noised_mixture.sample(n, rng)
    estimated_distribution = GaussianKDE(samples)
    estimated_tweedie = tweedie(
        estimated_distribution,
        x_sigma_grid,
        sigma
    )

    fig, ax = plt.subplots(figsize=(7, 4), dpi=200)
    ax.plot(x_sigma_grid, tweedie_means, lw=2, label="Exact Tweedie")
    ax.plot(x_sigma_grid, estimated_tweedie, ls="--", label="KDE Tweedie")
    ax.legend(loc="upper left", frameon=False)
    ax.set(xlim=(x_sigma_grid[0], x_sigma_grid[-1]), xlabel=r"$x_\sigma$", ylabel=r"$\mathbb{E}[x_0 \mid x_\sigma]$")
    fig.savefig(FIGURE_DIRECTORY / "tweedie-kde-comparison.png")
    plt.show()

def main():
    rng = np.random.default_rng(SEED)
    mixture = TwoComponentGaussianMixture(
        [Gaussian(MUS[0], SIGMAS[0]), Gaussian(MUS[1], SIGMAS[1])],
        WEIGHTS
    )
    bayes_tweedie_comparison(mixture, SIGMA)
    kde_tweedie_comparison(mixture, rng, N_SAMPLES, SIGMA)

if __name__ == "__main__":
    main()
