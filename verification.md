# Numerical verification

The following visually verifies 1-dimensional [Tweedie's formula](proofs/tweedies-formula-1d.md) for a Gaussian mixture prior:

$$
p_0(x_0) = 0.3 N(x_0; -2, 0.5^2) + 0.7 N(x_0; 1, 1^2)
$$

and $\sigma = 1$.

We calculate $\mathbb{E}[x_0 \mid x_\sigma]$ by direct calculation via Bayes' rule and by Tweedie's formula. Both methods give the same result:

<img src="figures/bayes-tweedie-comparison.png" alt="Tweedie's formula vs. exact Bayes posterior mean for a Gaussian mixture" width="500">

We also show that we can apply KDE to 5000 samples of $x_\sigma$ to obtain estimates of $\mathbb{E}[x_0 \mid x_\sigma]$ that are close to those obtained with knowledge of the true prior predictive distribution.

<img src="figures/tweedie-kde-comparison.png" alt="Applying Tweedie's formula to estimated density" width="500">

Regenerate: `python scripts/verify_tweedie.py`