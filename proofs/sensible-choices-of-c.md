Assume the setup as in [Choosing $c_{\text{in}}$, $c_{\text{out}}$, $c_{\text{skip}}$](../README.md#choosing-c_textin-c_textout-c_textskip).

We want:

$$
\text{Var}(c_{\text{in}}(\sigma) x_{\sigma, i}) = 1
$$

We have that:

$$
\begin{aligned}
\text{Var}(c_{\text{in}}(\sigma) x_{\sigma, i})
&= c_{\text{in}}(\sigma)^2 \text{Var}(x_{\sigma, i}) \\
&= c_{\text{in}}(\sigma)^2 \text{Var}(x_{0, i} + \sigma \varepsilon_i) \\
&= c_{\text{in}}(\sigma)^2 \left(\text{Var}(x_{0, i}) + \text{Var}(\sigma \varepsilon_i) \right) \\
&= c_{\text{in}}(\sigma)^2 \left(\sigma_{\text{data}}^2 + \sigma^2 \right) \\
&= 1
\end{aligned}
$$

Rearranging this gives:

$$
c_{\text{in}}(\sigma) = \frac{1}{\sqrt{\sigma_{\text{data}}^2 + \sigma^2}}
$$

We also want the variance of the target to be 1, so:

$$
\text{Var}\left(\frac{x_{0, i} - c_{\text{skip}}(\sigma) x_{\sigma, i}}{c_{\text{out}}(\sigma)}\right) = 1
$$

We have that:

$$
\begin{aligned}
\text{Var}\left(\frac{x_{0, i} - c_{\text{skip}}(\sigma) x_{\sigma, i}}{c_{\text{out}}(\sigma)}\right)
&= \frac{1}{c_{\text{out}}(\sigma)^2} \text{Var}(x_{0, i} - c_{\text{skip}}(\sigma) x_{\sigma, i}) \\
&= \frac{1}{c_{\text{out}}(\sigma)^2} \text{Var}(x_{0, i} - c_{\text{skip}}(\sigma) (x_{0, i} + \sigma \varepsilon_i)) \\
&= \frac{1}{c_{\text{out}}(\sigma)^2} \left( (1 - c_{\text{skip}}(\sigma))^2 \text{Var}(x_{0, i}) + \sigma^2 c_{\text{skip}}(\sigma)^2 \text{Var}(\varepsilon_i) \right) \\
&= \frac{1}{c_{\text{out}}(\sigma)^2} \left( (1 - c_{\text{skip}}(\sigma))^2 \sigma_{\text{data}}^2 + \sigma^2 c_{\text{skip}}(\sigma)^2 \right) \\
&= 1
\end{aligned}
$$

Rearranging this gives:

$$
c_{\text{out}}(\sigma)^2 = (1 - c_{\text{skip}}(\sigma))^2 \sigma_{\text{data}}^2 + \sigma^2 c_{\text{skip}}(\sigma)^2 \qquad (8)
$$

We want to choose $c_{\text{skip}}(\sigma)$ to minimise $c_{\text{out}}(\sigma)$. This is equivalent to minimising $c_{\text{out}}(\sigma)^2$ since $c_{\text{out}}(\sigma) > 0$. This is just a quadratic in $c_{\text{skip}}(\sigma)$, so differentiate to find the stationary point:

$$
\frac{d}{d c_{\text{skip}}(\sigma)} c_{\text{out}}(\sigma)^2
= -2(1 - c_{\text{skip}}(\sigma)) \sigma_{\text{data}}^2 + 2 \sigma^2 c_{\text{skip}}(\sigma) = 0
$$

Rearranging this gives:

$$
c_{\text{skip}}(\sigma) = \frac{\sigma_{\text{data}}^2}{\sigma_{\text{data}}^2 + \sigma^2}
$$

The second derivative is $2 (\sigma_{\text{data}}^2 + \sigma^2) > 0$, so this is the global minimum.

Substituting this back into (8) gives:

$$
c_{\text{out}}(\sigma) = \frac{\sigma \sigma_{\text{data}}}{\sqrt{\sigma_{\text{data}}^2 + \sigma^2}}
$$
