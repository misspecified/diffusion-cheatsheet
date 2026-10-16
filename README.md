# Diffusion Cheatsheet

## Setup: additive Gaussian noise in 1 dimension

$x_0$ is a real-valued quantity with density $p_0$. We consider the situation where we can only observe $x_\sigma$, a *noisy* observation of $x_0$:

$$
x_\sigma = x_0 + \sigma \varepsilon, \qquad \varepsilon \sim N(0, 1) \text{ independent of } x_0,
$$

where $\sigma > 0$ is known.

Denote the density of $x_\sigma$ by $p_\sigma$.

### Tweedie's formula

The expected value of $x_0$, given an observation of $x_\sigma$, can be calculated using only $x_\sigma$, $\sigma$, and $p_\sigma$.

$$
\mathbb{E}[x_0 \mid x_\sigma] = x_\sigma + \sigma^2 \frac{p'_\sigma(x_\sigma)}{p_\sigma(x_\sigma)}
$$

[Proof](proofs/tweedies-formula-1d.md)

This is a convenient property since it allows us to estimate $x_0$ using only the distribution of the noisy observations without knowing $p_0$.

