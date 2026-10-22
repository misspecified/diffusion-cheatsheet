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
\mathbb{E}[x_0 \mid x_\sigma] = x_\sigma + \sigma^2 \frac{d}{dx_\sigma} \log p_\sigma(x_\sigma) \qquad (1)
$$

[Proof](proofs/tweedies-formula-1d.md)

This is a convenient property since it allows us to estimate $x_0$ using only the distribution of the noisy observations, without knowing $p_0$.

This result is checked against simulation in the [numerical verification](verification.md).

#### Aside: Robbins' formula

$x$ is a count with $x \mid \theta \sim \text{Poisson}(\theta)$. Suppose also that we have a $\theta \sim g$ prior. Let $p$ be the marginal pmf of $x$.

Then:

$$
\mathbb{E}[\theta \mid x] = (x + 1) \frac{p(x + 1)}{p(x)}
$$

[Proof](proofs/robbins-formula.md)

Note the similarities to (1). We can estimate the latent $\theta$ value using only the distribution of the observations, without knowing $g$. In addition, we only depend on $p$ through $p(x + 1)$ and $p(x)$, which is the discrete equivalent of only depending on $p$ and $p'$.

## Setup: additive Gaussian noise in $n$ dimensions


$`\mathbf{x}_0`$ is a real-valued vector quantity with density $p_0$. We consider the situation where we can only observe $`\mathbf{x}_\sigma`$, a *noisy* observation of $`\mathbf{x}_0`$:

$$
\mathbf{x}_\sigma = \mathbf{x}_0 + \boldsymbol{\varepsilon}, \qquad \boldsymbol{\varepsilon} \sim N(\mathbf{0}, \Sigma) \text{ independent of } \mathbf{x}_0, \qquad (5)
$$

where the symmetric, positive-definite matrix $\Sigma$ is known.

Denote the density of $`\mathbf{x}_\sigma`$ by $p_\sigma$.

### Tweedie's formula

The expected value of $`\mathbf{x}_0`$, given an observation of $`\mathbf{x}_\sigma`$, can be calculated using only $`\mathbf{x}_\sigma`$, $\Sigma$, and $p_\sigma$.

$$
\mathbb{E}[\mathbf{x}_0 \mid \mathbf{x}_\sigma] = \mathbf{x}_\sigma + \Sigma \nabla_{\mathbf{x}_\sigma} \log p_\sigma(\mathbf{x}_\sigma) \qquad (6)
$$

[Proof](proofs/tweedies-formula-nd.md)

## Denoisers

A denoiser is a function $`D(\,\cdot\,; \sigma) : \mathbb{R}^n \to \mathbb{R}^n`$ that takes the noisy value $`\mathbf{x}_\sigma`$ and outputs an estimate for $`\mathbf{x}_0`$.

For some choice of $D$, we can define its loss by:

$$
L_\sigma(D) = \mathbb{E} \lVert D(\mathbf{x}_\sigma; \sigma) - \mathbf{x}_0 \rVert^2
$$

The choice of $D$ that minimises this loss is given by:

$$
D(\mathbf{x}_\sigma; \sigma) = \mathbb{E}[\mathbf{x}_0 \mid \mathbf{x}_\sigma] \qquad (7)
$$

[Proof](proofs/loss-is-minimised-by-conditional-expectation.md)

For this $D$ and the setup in equation (5):

$$
\nabla_{\mathbf{x}} \log p_\sigma(\mathbf{x}) = \Sigma^{-1}(D(\mathbf{x}; \sigma) - \mathbf{x})
$$

This is a simple corollary, obtained by substituting (7) into (6) and rearranging.