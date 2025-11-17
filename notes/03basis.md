# Why we care about Vector Spaces and Basis

In your reading, you've read about *Linear Combinations*, *Linear
Independence* and *Vector Spaces*.  I'm going to assume you've understood that
information, and won't belabor it here.

I do want to add some insight into why we care about these topics.  Imagine
that we're running an investment company, and we'd like to understand the
behavior of stocks, and so we do some clustering.  Economics are very
complicated, so we make sure to collect a lot of data related to the health of
the stock, its strategic plan, and the economy as a whole.  Given this data,
we perform our clustering, and identify a cluster of stocks that eventually
grew quickly.  We also notice another new company in the cluster which has yet
to grow.  How confident should we be when we invest our money?

Probably, given what you know about clustering, you would have some questions.
You'd ask about how "distance" was defined, and which algorithm was used to
generate the clusters.  But even before learning what you know about
clustering, you would have asked questions like, "what data did you collect?"
"Are each of the pieces of data about each company unique, or are you just
asking the same question different ways?  "Were you thorough in considering
all kinds of relevant information?"

These questions can be asked more precisely using the linear algebra concepts
we've learned about.  Assume you have our standard $n\times m$ data matrix,
where each column corresponds to an observation we've made about each data
point.

### Span

The *span* of our matrix is the set of all possible vectors we could create
by performing linear combinations of the column vectors in our matrix.  As
long as you're in the world of linear combinations, you can think of the span
as the complete set of things you can predict from your observations.  If what
you want to predict isn't in that span, then there's going to be at least some
error in your prediction.

### Linearly Dependent Features

Suppose you duplicated a feature.  Clearly unnecessary and unhelpful, right?
In clustering, when optimizing cluster variance, the optimizer would find it
twice as important to decrease distance in the duplicate featuers than in any
other, which is obviously misleading.

What if they weren't duplicates, but merely two different views of the same
thing?  For example, a region's poverty rate and crime rate are likely highly
correlated.  Including both may be essentially duplicating the same feature.

In either case, because one feature can be calculated as linear combinations
of other features, we say these are linearly dependent - essentially, that
feature is adding no extra information to your data set.  There's nothing you
can predict with it that you couldn't predict without it.

### Basis

Consider our matrix of movie ratings.  Our observations are how much different
people liked different movies.  However, our conclusions about our movie
watchers might be just as accurate if we asked about actors, or genres.  In
other words, we might be able to make exactly the same predictions (have the
same span) with entirely different observations.  In fact, these other
observations may even be better!

A *basis* of a matrix is a set of vectors that span the same vector space as
the matrix's original vectors.  You can think of it as new axes in the same
space.  These axes may have some intuitive understanding ("how much they like
Tom Cruise"), or may just be mathematically convenient.

# The Singular Value Decomposition (SVD)

Suppose we got really silly, and movie rankers were asked to rank exactly the
same movie twice.  In our above ideal world, the rankers would produce two
identical columns, which would, of course, be linearly dependent.  In the real
world, people (and observations) aren't so clean.  It's entirely possible
somebody might rank a movie 4/5, and then five minutes later decide to rank it
a 3/5.  This would make our second feature nearly identical to the first, but
not quite linearly dependent.  Do we have a way of expressing "near
dependence?"

It turns out that yes, we do, with a really beautiful and wildly applicable
result called the Singular Value Decomposition (the SVD).  The SVD theorem can
be expressed like this:  Given a $n\times m$ matrix $A$, we can construct
three matrices $U (n\times n)$, $\Sigma (n\times m)$, and $V (m\times m)$, such
that $A=U\Sigma V^T$ and:

- $U$ is a basis of $A$.
- The columns of $U$ are orthonormal, meaning they are at right angles to each
  other, and are of length 1.
- $V$ is a basis of $A^T$.
- The columns of $V$ are orthonormal.
- $\Sigma$ is a diagonal matrix, meaning only the elements $\Sigma$[i,i] are
  non-zero.
- By convention, the elements of $\Sigma$ are in decreasing order, with the
  largest in the upper left, and the smallest in the lower right.

The nonzero elements of $\Sigma$ are known as the matrix's *singular values*,
and the vectors of $U$ and $V$ are known as the left-singular vectors and
right-singular vectors, respectively.

When $U$ and $\Sigma$ are multiplied, only the $i$th column of $U$ interacts
with the $i$th singular value - they correspond.  So, if a singular value is
0, this means that the corresponding left singular vector is unnecessary and
unused when reconstructing the original matrix.  So, we see that the number of
non-zero singular values is equal to the rank of the matrix.  Similarly, a
very small singular value means the corresponding vector is barely used.  A
common first step in understanding a data matrix, then, is to plot the
singular values.

We'll add some solidity to this idea at our next meeting when we discuss the
Principle Component Analysis (PCA).  For now, though, if you're trying to
separate signal from noise, the number of meaningful features can be reduced
to the number of singular values of reasonable size.

### Code from today's class (rename to \*.py)

- [A demonstration showing how points described in 3 dimensions can actually lie in 2 dimensions](spanPlot.notPY)
- [A demonstration showing the effects of dimensionality reduction in MNIST](mnistSVDDemo.notPY)
