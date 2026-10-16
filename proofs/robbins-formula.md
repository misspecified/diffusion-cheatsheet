Assume the setup as in [Aside: Robbins' formula](../README.md#aside-robbins-formula).

By Bayes' rule, we have that:

$$
\begin{aligned}
\mathbb{E}[\theta \mid x]
&= \int \theta \frac{\mathrm{Pois}(x; \theta) g(\theta)}{p(x)} d\theta \\
&= \frac{\int \theta \, \mathrm{Pois}(x; \theta) g(\theta) d\theta}{p(x)}
\end{aligned}
\qquad (3)
$$

By definition:

$$
p(x) = \int \frac{\theta^x e^{-\theta}}{x!} g(\theta) d\theta
$$

Then:

$$
\begin{aligned}
\int \theta \, \mathrm{Pois}(x; \theta) g(\theta) d\theta
&= \int \frac{\theta^{x + 1} e^{-\theta}}{x!} g(\theta) d\theta \\
&= (x + 1) \int \frac{\theta^{x + 1} e^{-\theta}}{(x + 1)!} g(\theta) d\theta \\
&= (x + 1) p(x + 1)
\end{aligned}
$$

Substituting back into (3):

$$
\mathbb{E}[\theta \mid x] = (x + 1) \frac{p(x + 1)}{p(x)}
$$