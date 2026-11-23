Assume the setup as in [ODE formulation](../README.md#ode-formulation).

We aim to show:

$$
\frac{\partial p}{\partial \sigma} = \sigma \frac{\partial^2 p}{\partial x^2}
$$

Recall from the [proof of Tweedie's formula](tweedies-formula-1d.md) that:

$$
p(x; \sigma) = \int p_0(x_0) N(x; x_0, \sigma^2) dx_0
$$

We will use two derivatives of the Gaussian density $N(x; x_0, \sigma^2)$:

$$
\frac{\partial}{\partial x} N(x; x_0, \sigma^2) = -\frac{x - x_0}{\sigma^2} N(x; x_0, \sigma^2)
$$

$$
\frac{\partial}{\partial \sigma} N(x; x_0, \sigma^2) = \frac{(x - x_0)^2 - \sigma^2}{\sigma^3} N(x; x_0, \sigma^2)
$$

Using the first identity:

$$
\frac{\partial p}{\partial x} = \int p_0(x_0) \frac{\partial}{\partial x} N(x; x_0, \sigma^2) dx_0 = \frac{1}{\sigma^2} \int p_0(x_0) (x_0 - x) N(x; x_0, \sigma^2) dx_0
$$

Differentiating again, and using the first identity:

$$
\begin{aligned}
\frac{\partial^2 p}{\partial x^2}
&= \frac{1}{\sigma^2} \left[ \frac{1}{\sigma^2} \int p_0(x_0) (x_0 - x)^2 N(x; x_0, \sigma^2) dx_0 - \int p_0(x_0) N(x; x_0, \sigma^2) dx_0 \right] \\
&= \frac{1}{\sigma^4} \int p_0(x_0) \left( (x - x_0)^2 - \sigma^2 \right) N(x; x_0, \sigma^2) dx_0 \qquad (10)
\end{aligned}
$$

Similarly, using the second identity:

$$
\frac{\partial p}{\partial \sigma} = \int p_0(x_0) \frac{\partial}{\partial \sigma} N(x; x_0, \sigma^2) dx_0 = \frac{1}{\sigma^3} \int p_0(x_0) \left( (x - x_0)^2 - \sigma^2 \right) N(x; x_0, \sigma^2) dx_0 \qquad (11)
$$

Comparing (10) and (11):

$$
\frac{\partial p}{\partial \sigma} = \sigma \frac{\partial^2 p}{\partial x^2}
$$
