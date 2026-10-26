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
\mathbf{x}_\sigma = \mathbf{x}_0 + \sigma \boldsymbol{\varepsilon}, \qquad \boldsymbol{\varepsilon} \sim N(\mathbf{0}, \Sigma) \text{ independent of } \mathbf{x}_0, \qquad (5)
$$

where $\sigma > 0$ and the symmetric, positive-definite matrix $\Sigma$ are known.

Denote the density of $`\mathbf{x}_\sigma`$ by $p_\sigma$.

### Tweedie's formula

The expected value of $`\mathbf{x}_0`$, given an observation of $`\mathbf{x}_\sigma`$, can be calculated using only $`\mathbf{x}_\sigma`$, $\Sigma$, $\sigma$, and $p_\sigma$.

$$
\mathbb{E}[\mathbf{x}_0 \mid \mathbf{x}_\sigma] = \mathbf{x}_\sigma + \sigma^2 \Sigma \nabla_{\mathbf{x}_\sigma} \log p_\sigma(\mathbf{x}_\sigma) \qquad (6)
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
\nabla_{\mathbf{x}} \log p_\sigma(\mathbf{x}) = (\sigma^2 \Sigma)^{-1}(D(\mathbf{x}; \sigma) - \mathbf{x})
$$

This is a simple corollary, obtained by substituting (7) into (6) and rearranging.

### Training a denoiser

We can't usually calculate $`\mathbb{E}[\mathbf{x}_0 \mid \mathbf{x}_\sigma]`$ directly.
$p_0$ may be unknown and complex.
For example, denoisers can be used to generate images by starting from pure noise and repeatedly refining.
This aims to produce a sample from $p_0$, but the true distribution of all possible images is both unknown and complex.
Using the obvious finite approximation (the empirical distribution of the training set) will only be capable of producing images from the training set itself as $\sigma \to 0$.

In this case, we would still like to be able to fit a denoiser.
[Karras et al. (2022)](https://arxiv.org/abs/2206.00364) suggest fitting the form:

$$
D_\theta(\mathbf{x}_\sigma; \sigma) = c_{\text{skip}}(\sigma) \mathbf{x}_\sigma + c_{\text{out}}(\sigma) F_\theta(c_{\text{in}}(\sigma) \mathbf{x}_\sigma; c_{\text{noise}}(\sigma))
$$

where $F_\theta$ is a neural network to be fitted, and each $c$ is a deterministic function of $\sigma$.

This form reflects the fact that we can choose the target of $F_\theta$. There are two basic regimes we could consider:
 * Target the noise, $`\boldsymbol{\varepsilon}`$, so $`D_\theta(\mathbf{x}_\sigma; \sigma) = \mathbf{x}_\sigma - \sigma F_\theta(\cdot)`$.
 * Target the clean value, $`\mathbf{x}_0`$, so $`D_\theta(\mathbf{x}_\sigma; \sigma) = F_\theta(\cdot)`$.

For small $\sigma$, we would prefer to be in the first regime. The noisy value should already be very close to the clean value, and $\sigma$ scales down the errors in $F_\theta$. In the second regime, $F_\theta$ would have to reproduce $`\mathbf{x}_\sigma`$ almost exactly, and the errors in $F_\theta$ would pass straight into $D_\theta$ with nothing to shrink them. For large $\sigma$, we would prefer to be in the second regime. The noisy value does not give much information about the clean value. In the first regime, the large $\sigma$ would scale up the errors in $F_\theta$.

In practice, we can choose the $c$ functions to sit partway between both regimes, depending on the value of $\sigma$.


The squared loss can be written as:

$$
L_\sigma(D_\theta) = \mathbb{E} \lVert D_\theta(\mathbf{x}_\sigma; \sigma) - \mathbf{x}_0 \rVert^2
= c_{\text{out}}(\sigma)^2 \thinspace \mathbb{E} \left\lVert F_\theta(c_{\text{in}}(\sigma) \mathbf{x}_\sigma; c_{\text{noise}}(\sigma)) - \frac{\mathbf{x}_0 - c_{\text{skip}}(\sigma) \mathbf{x}_\sigma}{c_{\text{out}}(\sigma)} \right\rVert^2
$$

Therefore, $F_\theta$ can be fit on squared loss with target $`\frac{\mathbf{x}_0 - c_{\text{skip}}(\sigma) \mathbf{x}_\sigma}{c_{\text{out}}(\sigma)}`$.

#### Preconditioning

Neural networks behave best when their inputs and targets are on the same scale (e.g. both unit variance).
Additionally, we want $c_{\text{out}}(\sigma)$ to be small, since this scales down the errors in $F_\theta$.
Suppose that $\text{Var}(x_{0,i}) = \sigma_{\text{data}}^2$ and $\Sigma_{ii} = 1$ for $i = 1, 2, \dots, n$.
Imposing these properties gives:

$$
c_{\text{in}}(\sigma) = \frac{1}{\sqrt{\sigma_{\text{data}}^2 + \sigma^2}}
$$

$$
c_{\text{out}}(\sigma) = \frac{\sigma \sigma_{\text{data}}}{\sqrt{\sigma_{\text{data}}^2 + \sigma^2}}
$$

$$
c_{\text{skip}}(\sigma) = \frac{\sigma_{\text{data}}^2}{\sigma_{\text{data}}^2 + \sigma^2}
$$


[Proof](proofs/sensible-choices-of-c.md)