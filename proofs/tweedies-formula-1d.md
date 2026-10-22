Assume the setup as in [Setup: additive Gaussian noise in 1 dimension](../README.md#setup-additive-gaussian-noise-in-1-dimension).

By Bayes' rule, we have that:

$$
\begin{aligned}
\mathbb{E}[x_0 \mid x_\sigma]
&= \int x_0 \frac{p(x_\sigma \mid x_0) p_0(x_0)}{p_\sigma(x_\sigma)} dx_0 \\
&= \frac{\int x_0 N(x_\sigma; x_0, \sigma^2) p_0(x_0) dx_0}{p_\sigma(x_\sigma)}
\end{aligned}
\qquad (2)
$$

Consider $p_\sigma(x_\sigma)$ separately. By the definition of $x_\sigma$ as a sum of two independent variables:

$$
\begin{aligned}
p_\sigma(x_\sigma)
&= \int p_0(x_0) N(x_\sigma - x_0; 0, \sigma^2) dx_0 \\
&= \int p_0(x_0) N(x_\sigma; x_0, \sigma^2) dx_0 
\end{aligned}
$$

Applying Leibniz's rule to this quantity:

$$
\begin{aligned}
p'_\sigma(x_\sigma)
&= \int p_0(x_0) \frac{(x_0 - x_\sigma)}{\sigma^2} N(x_\sigma; x_0, \sigma^2) dx_0 \\
&= \frac{1}{\sigma^2} \int x_0 p_0(x_0) N(x_\sigma; x_0, \sigma^2) dx_0 - \frac{1}{\sigma^2} \int x_{\sigma} p_0(x_0) N(x_\sigma; x_0, \sigma^2) dx_0 \\
&= \frac{1}{\sigma^2} \int x_0 p_0(x_0) N(x_\sigma; x_0, \sigma^2) dx_0 - \frac{x_\sigma}{\sigma^2} p_{\sigma}(x_\sigma)
\end{aligned}
$$

Rearranging this gives:

$$
\int x_0 p_0(x_0) N(x_\sigma; x_0, \sigma^2) dx_0 = x_\sigma p_{\sigma}(x_\sigma) + \sigma^2 p'_\sigma(x_\sigma)
$$

Substituting this back into (2):

$$
\begin{aligned}
\mathbb{E}[x_0 \mid x_\sigma]
&= \frac{x_\sigma p_{\sigma}(x_\sigma) + \sigma^2 p'_\sigma(x_\sigma)}{p_\sigma(x_\sigma)} \\
&= x_\sigma + \sigma^2 \frac{p'_\sigma(x_\sigma)}{p_\sigma(x_\sigma)} \\
&= x_\sigma + \sigma^2 \frac{d}{dx_\sigma} \log p_\sigma(x_\sigma) 
\end{aligned}
$$