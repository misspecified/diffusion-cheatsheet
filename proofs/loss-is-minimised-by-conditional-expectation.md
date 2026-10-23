We are aiming to choose $D$ to minimise:

$$
L_\sigma(D) = \mathbb{E} \lVert D(\mathbf{x}_\sigma; \sigma) - \mathbf{x}_0 \rVert^2
$$

We have that:

$$
\begin{aligned}
\mathbb{E} \lVert D(\mathbf{x}_\sigma; \sigma) - \mathbf{x}_0 \rVert^2
&= \int \int \lVert D(\mathbf{x}_\sigma; \sigma) - \mathbf{x}_0 \rVert^2 p(\mathbf{x}_0, \mathbf{x}_\sigma) d\mathbf{x}_0 d\mathbf{x}_\sigma \\
&= \int \int \lVert D(\mathbf{x}_\sigma; \sigma) - \mathbf{x}_0 \rVert^2 p(\mathbf{x}_0 \mid \mathbf{x}_\sigma) p_\sigma(\mathbf{x}_\sigma) d\mathbf{x}_0 d\mathbf{x}_\sigma \\
&= \int p_\sigma(\mathbf{x}_\sigma) \int \lVert D(\mathbf{x}_\sigma; \sigma) - \mathbf{x}_0 \rVert^2 p(\mathbf{x}_0 \mid \mathbf{x}_\sigma) d\mathbf{x}_0 d\mathbf{x}_\sigma
\end{aligned}
$$

Consider only the inner integral. Since $`p_\sigma(\mathbf{x}_\sigma) > 0`$ and there are no restrictions on the shape of $D$, we can minimise pointwise:

$$
\begin{aligned}
\int \lVert D(\mathbf{x}_\sigma; \sigma) - \mathbf{x}_0 \rVert^2 p(\mathbf{x}_0 \mid \mathbf{x}_\sigma) d\mathbf{x}_0
&= \int D(\mathbf{x}_\sigma; \sigma)^\top D(\mathbf{x}_\sigma; \sigma) p(\mathbf{x}_0 \mid \mathbf{x}_\sigma) d\mathbf{x}_0 \\
&\quad - 2 \int D(\mathbf{x}_\sigma; \sigma)^\top \mathbf{x}_0 p(\mathbf{x}_0 \mid \mathbf{x}_\sigma) d\mathbf{x}_0 \\
&\quad + \int \mathbf{x}_0^\top \mathbf{x}_0 p(\mathbf{x}_0 \mid \mathbf{x}_\sigma) d\mathbf{x}_0
\end{aligned}
$$

The final term can be ignored (assuming $`\mathbb{E} \lVert \mathbf{x}_0 \rVert^2 < \infty`$), since it does not depend on $D$. Then:

$$
\begin{aligned}
&\int D(\mathbf{x}_\sigma; \sigma)^\top D(\mathbf{x}_\sigma; \sigma) p(\mathbf{x}_0 \mid \mathbf{x}_\sigma) d\mathbf{x}_0 - 2 \int D(\mathbf{x}_\sigma; \sigma)^\top \mathbf{x}_0 p(\mathbf{x}_0 \mid \mathbf{x}_\sigma) d\mathbf{x}_0 \\
&\qquad = D(\mathbf{x}_\sigma; \sigma)^\top \left( D(\mathbf{x}_\sigma; \sigma) \int p(\mathbf{x}_0 \mid \mathbf{x}_\sigma) d\mathbf{x}_0 - 2 \int \mathbf{x}_0 p(\mathbf{x}_0 \mid \mathbf{x}_\sigma) d\mathbf{x}_0 \right) \\
&\qquad = D(\mathbf{x}_\sigma; \sigma)^\top \left( D(\mathbf{x}_\sigma; \sigma) - 2 \mathbb{E}[\mathbf{x}_0 \mid \mathbf{x}_\sigma] \right)
\end{aligned}
$$

We are minimising pointwise, so differentiate with respect to $`D(\mathbf{x}_\sigma; \sigma)`$:

$$
\begin{aligned}
\nabla_D \thinspace D(\mathbf{x}_\sigma; \sigma)^\top \left( D(\mathbf{x}_\sigma; \sigma) - 2 \mathbb{E}[\mathbf{x}_0 \mid \mathbf{x}_\sigma] \right)
&= 2 D(\mathbf{x}_\sigma; \sigma) - 2 \mathbb{E}[\mathbf{x}_0 \mid \mathbf{x}_\sigma] \\
&= \mathbf{0}
\end{aligned}
$$

Solving this gives:

$$
D(\mathbf{x}_\sigma; \sigma) = \mathbb{E}[\mathbf{x}_0 \mid \mathbf{x}_\sigma]
$$

Differentiating again with respect to $D$ gives $2I$, which is positive definite everywhere. Therefore, this is the global minimum.
