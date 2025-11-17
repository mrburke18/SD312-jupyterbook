---
title: Supervised Learning
---

The next thing we're going to learn about is _matrix completion_, or an approach where we try to predict each individual user's rankings of each individual movie.  To do this, we're going to switch from _unsupervised_ learning to _supervised_ learning, where you know what the right answers are for some of your data (in this case, the nonempty elements of the matrix).  If your system can correctly predict the data you do have, this gives you confidence that it will correctly predict the data you don't have.  Many people are more comfortable with supervised learning, because you can tell how well you're doing.

For an illustration, suppose I'm training a system to recognize pictures of goats from pictures of mules.  First, I collect a whole bunch of pictures of goats, and label them as such, and a whole bunch of pictures of mules, and train them as such.  I then use these images as my dataset to train a model that takes in a picture of a quadruped, and returns either "goat" or "mule."  The ones I get wrong in this set are known as the "training error."  Here, my pictures are pulling double duty - they're both the images we use to teach the model to get better, and the images we use to test if it's working.  These images are known as the *training set*.

The second question is, once our training error is low, does it work well on new images it has never seen before?  After all, maybe it simply memorized the ones we gave it, and didn't learn anything about general goats and mules.  This is known as *overfitting*, and we're going to spend a lot of time on it this semester.  To test this, we collect a second dataset, and see if our system correctly predicts these new goats and mules.  This is known as "testing error," and those images are known as the *testing set*.

# Matrix Completion

So suppose rather than coming up with some hacky way of ignoring or justifying
the empty spaces in our data matrix, we wanted to fill it in with how that
person would likely rate the movie.  Because our data matrix is likely low
rank (due to movie-liking not being independent from movie to movie), we can
do this with some concepts we already have.

We know that every $n\times m$ matrix $A$ has an SVD decomposition, such that
$A=U\Sigma V^T$, where $U$ is $n\times n$, $\Sigma$ is a diagonal $n\times m$,
and $V$ is $m\times m$ (and there are also lots of other constraints, like
orthonormality and whatnot).  We also know that we can remove the smallest
elements of $\Sigma$ without losing much accuracy when we remultiply and
reconstruct $A$.

Think about what happens when we remove these small values, keeping, say $k$
singular values.  This means all columns after the $k$-th column and all rows
after the $k$th row of $\Sigma$ are now entirely zeros.  So, let's imagine
multiplying this $U\Sigma$.  Because of all the zero-value rows of $\Sigma$,
do you see how all columns after the $k$th column of $U$ contribute nothing at
all?  They might as well not be there!

Similarly, if we multiply $\Sigma V^T$, because all the final columns of
$\Sigma$ are zeros, we don't need any rows of $V^T$ after the $k$th one!  So,
we could discard all those rows and columns that contribute nothing, and
rewrite the whole reconstruction as: $A\approx U_k\Sigma_k V^T_k$, where $U_k$
is $n\times k$, $\Sigma_k$ is $k\times k$, and $V^T$ is $k\times m$.  If $k$
is small, those matrices are a whole lot smaller, and our reconstruction is
still very close to $A$.

Now, we could make a matrix $P$ such that $P=U_k\Sigma_k$.  $P$ wouldn't have
any of the nice orthonormal properties of $U$, but we can see that if there is
an acceptable $k$-rank SVD reconstruction of $A$, we can say $A\approx PV^T_k$.
Alternatively, we could start all this by creating a $Q=\Sigma_PV^T_k$, and
saying $A\approx U_kQ$.

OR, we could just say that by melding $\Sigma_k$ into one or the other, two
matrices $P$ and $Q$ exist such that $A\approx PQ$, where $P$ is $n\times k$,
and $Q$ is $k\times m$.  Now, the vectors of $P$ and $Q$ would no longer be of
unit lengths like in the SVD, but the decomposition nonetheless exists.
Again, all this depends upon our data being able to be represented with just a
few principal components.

### Well, that was a lot.  Who cares?

Well, now we just need to say that we need to find versions of $P$ and $Q$
such that when we multiply them together, the elements that we DO have in our
matrix $A$ are correct (or close to correct).  These elements are our training
set.  If they get all the elements we *do* have right, we can maybe trust
that they're getting all the other ones right, too, and so we can use those
approximate rankings to recommend some movies.

We need to define an optimization problem.  Let $p_i$ represent the $i$th row
of $P$, and $q_j$ represent the $j$th column of $Q$.  Naturally, for some
ranking that we do have $A_{ij}$, we can feel comfortable with $P$ and $Q$ if
$p_i\cdot q_j=A_{ij}$.  Let $T$ be the set of all rankings for which
we have a ranking in $A$.  What we want is:

$$
\argmin_{P,Q} \sum_{A_{ij}\in T}\left(A_{ij}-p_i\cdot q_j\right)^2
$$

Once we have the solution to that, we can say that $\hat A=PQ$, and read off
everybody's estimated rankings!  So, OK, but how do we solve that?  Stochastic Gradient Descent!


### Applying SGD to low-rank matrix completion

So, again:

$$
\argmin_{P,Q} \sum_{A_{ij}\in T}\left(A_{ij}-p_i\cdot q_j\right)^2
$$

Here, $T$ is the data that we have.  $P$ and $Q$ are the $w$ in the general
purpose algorithm.  That whole function is $\mathcal{L}$.  So, we have $\mathcal{L}(T,P,Q)$, and
we'd like to find the $P$ and $Q$ that minimize $\mathcal{L}$ given our data $T$.

We're going to get our stochasticity by only considering one data point
$A_{ij}$ at a time.  So, for some $A_{ij}$, let's solve for the gradient with
respect to $p_i$ and with respect to $q_j$.

$$
\frac{\partial}{\partial p_i}\left(A_{ij}-p_i\cdot q_j\right)^2
=-2q_j(A_{ij}-p_i\cdot q_j)
$$

and

$$
\frac{\partial}{\partial q_j}\left(A_{ij}-p_i\cdot q_j\right)^2
=-2p_i(A_{ij}-p_i\cdot q_j)
$$

Right?  Basic calculus.  So, SGD for this problem just becomes:

1. Randomly initialize $P$ and $Q$.
2. Until convergence, for all known rankings $A_{ij}$:

$$
  p_i\leftarrow p_i + \alpha q_j^T(A_{ij}-p_i\cdot q_j)
$$

and...

$$
  q_j\leftarrow q_j + \alpha p_i^T(A_{ij}-p_i\cdot q_j)
$$

And that's it!  Once (if) that converges, you have a $P$ and $Q$ such that
$\hat A=PQ$ correctly approximates all your known rankings, so perhaps the
rest of them are correct, as well!  You have a speculative full set of
rankings from which to make recommendations!
