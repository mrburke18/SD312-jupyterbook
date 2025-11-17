---
title: Feasibility of Learning
---

Here, I show the solutions to some of the exercises in the reading for today.

### Exercise 1.8

We use the binomial distribution.  The probability of getting exactly $k$ red marbles in 10, from a set that is $\mu$ percentage red is:

$$
p(k)={10 \choose k}\mu^k(1-\mu)^{10-k}.
$$

To get a $\nu\leq 0.1$, we need to pull either 1 or 0 red marbles.  So, $p(\nu\leq 0.1)=p(0)+p(1)$.  Throw the correct values of $k$ and $\mu$ into the above, once for $k=0$, and once for $k=1$, and you get:

$$
\begin{align}
p(\nu\leq 0.1)=p(0)+p(1)=&{10 \choose 0}.9^0(1-.9)^{10}+{10\choose 1}.9^1(1-.9)^9\\
=&10^{-10}+(10)(.9)(10^{-9})\\
=&10^{-10}+9\times 10^{-9}
\end{align}
$$

That's quite unlikely!

### Exercise 1.9

Here, we just plug into the Hoeffding Inequality, with $\epsilon=.8$ and $N=10$.

$$
\begin{align}
P(|\nu-\mu|>\epsilon)\leq& 2e^{-2\epsilon^2N}\\
P(|\nu-\mu|>.8)\leq& 2e^{(-2)(.8^2)(10)}\\
\leq& .0033
\end{align}
$$
