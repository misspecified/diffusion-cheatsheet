Assume the setup as in [Setup: additive Gaussian noise in n dimensions](../README.md#setup-additive-gaussian-noise-in-n-dimensions).

By Bayes' rule, we have that:

$$
\begin{aligned}
\mathbb{E}[\mathbf{x}_0 \mid \mathbf{x}_\sigma]
&= \int \mathbf{x}_0 \frac{p(\mathbf{x}_\sigma \mid \mathbf{x}_0) p_0(\mathbf{x}_0)}{p_\sigma(\mathbf{x}_\sigma)} d\mathbf{x}_0 \\
&= \frac{\int \mathbf{x}_0 N(\mathbf{x}_\sigma; \mathbf{x}_0, \sigma^2 \Sigma) p_0(\mathbf{x}_0) d\mathbf{x}_0}{p_\sigma(\mathbf{x}_\sigma)}
\end{aligned}
\qquad (4)
$$

Consider $`p_\sigma(\mathbf{x}_\sigma)`$ separately. By the definition of $`\mathbf{x}_\sigma`$ as a sum of two independent variables:

$$
\begin{aligned}
p_\sigma(\mathbf{x}_\sigma)
&= \int p_0(\mathbf{x}_0) N(\mathbf{x}_\sigma - \mathbf{x}_0; \mathbf{0}, \sigma^2 \Sigma) d\mathbf{x}_0 \\
&= \int p_0(\mathbf{x}_0) N(\mathbf{x}_\sigma; \mathbf{x}_0, \sigma^2 \Sigma) d\mathbf{x}_0 
\end{aligned}
$$

Applying Leibniz's rule to this quantity:

$$
\begin{aligned}
\nabla_{\mathbf{x}_\sigma} p_\sigma(\mathbf{x}_\sigma)
&= \int p_0(\mathbf{x}_0) (\sigma^2 \Sigma)^{-1} (\mathbf{x}_0 - \mathbf{x}_\sigma) N(\mathbf{x}_\sigma; \mathbf{x}_0, \sigma^2 \Sigma) d\mathbf{x}_0 \\
&= (\sigma^2 \Sigma)^{-1} \int \mathbf{x}_0 p_0(\mathbf{x}_0) N(\mathbf{x}_\sigma; \mathbf{x}_0, \sigma^2 \Sigma) d\mathbf{x}_0 - (\sigma^2 \Sigma)^{-1} \int \mathbf{x}_{\sigma} p_0(\mathbf{x}_0) N(\mathbf{x}_\sigma; \mathbf{x}_0, \sigma^2 \Sigma) d\mathbf{x}_0 \\
&= (\sigma^2 \Sigma)^{-1} \int \mathbf{x}_0 p_0(\mathbf{x}_0) N(\mathbf{x}_\sigma; \mathbf{x}_0, \sigma^2 \Sigma) d\mathbf{x}_0 - (\sigma^2 \Sigma)^{-1} \mathbf{x}_\sigma p_{\sigma}(\mathbf{x}_\sigma)
\end{aligned}
$$

Rearranging this gives:

$$
\int \mathbf{x}_0 p_0(\mathbf{x}_0) N(\mathbf{x}_\sigma; \mathbf{x}_0, \sigma^2 \Sigma) d\mathbf{x}_0 = \mathbf{x}_\sigma p_{\sigma}(\mathbf{x}_\sigma) + \sigma^2 \Sigma \nabla_{\mathbf{x}_\sigma} p_\sigma(\mathbf{x}_\sigma)
$$

Substituting this back into (4):

$$
\begin{aligned}
\mathbb{E}[\mathbf{x}_0 \mid \mathbf{x}_\sigma]
&= \frac{\mathbf{x}_\sigma p_{\sigma}(\mathbf{x}_\sigma) + \sigma^2 \Sigma \nabla_{\mathbf{x}_\sigma} p_\sigma(\mathbf{x}_\sigma)}{p_\sigma(\mathbf{x}_\sigma)} \\
&= \mathbf{x}_\sigma + \sigma^2 \Sigma \frac{\nabla_{\mathbf{x}_\sigma} p_\sigma(\mathbf{x}_\sigma)}{p_\sigma(\mathbf{x}_\sigma)} \\
&= \mathbf{x}_\sigma + \sigma^2 \Sigma \nabla_{\mathbf{x}_\sigma} \log p_\sigma(\mathbf{x}_\sigma) 
\end{aligned}
$$