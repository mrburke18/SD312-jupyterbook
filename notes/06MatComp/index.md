# Matrix Completion

**Matrix completion** is a supervised learning approach used to predict individual user rankings for specific items (movies) by filling in the missing elements of a data matrix. This problem assumes the data matrix is low-rank, implying that user preferences are not independent across items.

This approach was a key part of the submission which won the [Netflix
Prize](https://en.wikipedia.org/wiki/Netflix_Prize), in which Netflix shared
some of their data and then awarded 1 million dollars to the team which could
dramatically improve upon their recommendation system.

## Low-Rank Approximation

An $n \times m$ matrix $A$ has a Singular Value Decomposition (SVD) such that $A=U\Sigma V^T$, where $U$ is $n\times n$, $\Sigma$ is a diagonal $n\times m$ matrix, and $V$ is $m\times m$.

By retaining only the $k$ largest singular values in $\Sigma$, we can approximate $A$ while discarding columns and rows that contribute negligibly to the reconstruction. This results in the approximation:

$$A\approx U_k \Sigma_k V_k^T$$

where $U_k$ is $n\times k$, $\Sigma_k$ is $k\times k$, and $V_k^T$ is $k\times m$.

This decomposition allows us to represent the approximation as the product of two smaller matrices, $P$ and $Q$, such that $A\approx PQ$ (for example, $P=U\Sigma$, and $Q=V^T$, though that's not the only way). Here, $P$ is an $n\times k$ matrix and $Q$ is a $k\times m$ matrix. While $P$ and $Q$ may lack the orthonormal properties of SVD matrices, they provide a valid decomposition for low-rank data.

## Optimization Problem

To predict missing rankings, we must determine matrices $P$ and $Q$ such that their product accurately approximates the observed elements of $A$. Let $p_i$ represent the $i$-th row of $P$ and $q_j$ represent the $j$-th column of $Q$. We define $T$ as the set of observed rankings in $A$.

The objective is to minimize the squared error between the observed values $A_{ij}$ and the predicted values $p_i \cdot q_j$:

$$argmin_{P,Q} \sum_{A_{ij}\in T} \left( A_{ij}-p_i\cdot q_j\right) ^2$$

Once solved, the estimate for the full matrix is $\hat A = PQ$.

## Algorithm: Stochastic Gradient Descent (SGD)

We solve the minimization problem using Stochastic Gradient Descent (SGD), optimizing the objective function $\mathcal{L}$ with respect to $P$ and $Q$. SGD updates the parameters by considering one data point $A_{ij}$ at a time.

The partial derivatives of the squared error for a single observation are:

$$\frac{\partial}{\partial p_i}( A_{ij} - p_i \cdot q_j )^2 = -2 q_j( A_{ij}-p_i\cdot q_j)$$

$$\frac{\partial}{\partial q_j}( A_{ij} - p_i \cdot q_j )^2 = -2 p_i ( A_{ij}-p_i\cdot q_j) $$


**The SGD Algorithm:**

1. Randomly initialize matrices $P$ and $Q$.
2. Iterate until convergence using the following update rules for all known
rankings $A_{ij}$:

$$p_i \leftarrow p_i + \alpha q_j^T(A_{ij}-p_i \cdot q_j)$$

$$q_j \leftarrow q_j + \alpha p_i^T(A_{ij}-p_i \cdot q_j)$$

**Note:** The factor of 2 from the derivative is absorbed into the learning
rate $\alpha$.

Upon convergence, $\hat A = PQ$ provides the estimated rankings for the empty
cells in the original matrix.

### Assumptions and hyperparameters

If you choose to build a recommendation system this way, you have assumed that
a linear combination of a small number of features is an appropriate way to
make these predictions.

You have assumed that a fully-complete matrix $A$ would be approximately rank
$k$.

Your **hyperparameters** are $k$, $\alpha$, and the training time.

If $k$ is too small, the model will underfit - too large, and it will overfit.

If $\alpha$ is too small, improvement will be slow. Too large, and the
values will explode due to overshooting the minimum.

If the training time is too small, the model will underfit. Too large, and the
model will overfit. It is common to use *early stopping*, where training stops
when the test error begins to increase.
