# Let's remember the SVD!

The SVD is going to be a key component of our next recommendation system, and it's just a good thing to understand when exploring datasets.  This reminder
material is going to use some terms you'll need to remember from Linear
Algebra, like "linearly independent," "rank," and "span."  If you don't
remember those terms, please look them up and refresh your memory.

As a one-place reminder of the SVD, recall that the SVD theorem can
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
very small singular value means the corresponding vector is barely used.

***Applying SVD Notionally to a Movie Ratings Matrix***

There are probably underlying reasons that people like some movies and don't
like other movies.  For example, fans of action movies have a set of movies
they'll like more than people who are not fans of action movies.  So, perhaps
if we knew those main underlying reasons, and we could ask if people liked
action movies, or artsy movies, or Tom Hanks, that might allow us to
reasonably predict all these ratings from only a few questions.

We can interpret the SVD as extracting those few most necessary underlying
reasons for liking movies.  Suppose $A$ is a ratings matrix like in our last
lab.  Each column of $U$ represents an underlying reason they might like movies, and a value for a given
user in that column is the user's affinity for that reason.  Maybe, for
example, the first column represents how much people like action movies. An
action movie fan would have a large value; someone who doesn't like action
movies would have a negative value.  Similarly, a row of $V^T$ (aka a column
of $V$) tells us how much that underlying reason applies to a given movie. A
Jason Statham movie would have a large value.  A movie with a lot of talking
would have a small value.  The corresponding singular value says how much that
property matters in the prediction of someone's movie rating.  So, maybe
"action movie" is really important, and so has a large singular value, and
"likeable leading man" is less important, and so has a smaller singular value.

Of course, often they're not so interpretable as that; they're mathematical
artifacts.  Nevertheless, the number of large singular values tells us how
many actual questions would have to be asked in order to reasonably predict
all these heavily-correlated ratings.  If we excluded the questions associated
with the small singular values, we would get a somewhat less accurate resulting matrix, but these
likely reflect noise, not useful signal.


