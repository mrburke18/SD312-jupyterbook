# Principle Component Analysis

Last time, we learned a bit about how our data, presented to us by an $n\times
m$ data matrix, can be viewed as points in $m$-dimensional space, and that
there might be other axes which are more helpful.  This is weird!  Why might
we want other axes?

### Data Analysis

This is the one we focused on last time.  We know we've made $m$ observations
about each data points, but are some of them just asking the same question
again (making them *linearly dependent*)?  Or, are they nearly asking the same
question again (asking about height AND weight, for example, because they have
a near-linear relationship, would result in at least one small *singular
value* in the SVD)?

### Compression

By using more descriptive axes, you may be able to use fewer of them, allowing
you to represent each data point with fewer numbers, while losing little
information.

### Better definition of "distance"

In clustering, we had to measure the distance between points.  If your points
actually lie in a lower-rank space than you're representing them, you're
artificially increasing the distances between some points.

## So what's the best set of axes?

Well, we start by assuming our data has a mean at the origin.  If it doesn't,
we move it so that it does (calculate the means of each feature, and subtract
that mean from each data point - distances, relationships between points, etc.
are all the same, we've just moved everything over).  All this just makes the
math a little easier.  For example, here's all the plebes' SAT scores (math on
the x-axis, and verbal on the y-axis) after being moved to be centered around
the origin:

![](sat.png)

Now, suppose you only got one line to draw on this graph.  Every point would
be moved to its closest point on that line.  The idea is to choose the line
that would minimize the total distance moved by all these points.  What line
do you draw?  Maybe this one?

![](onepc.png)

You can think of this as compression - each data point is being reduced from
two numbers to one (the location along the chosen axis), and has moved the
shortest distance (least information lost).

OK, great.  Now, suppose instead, you wanted the one line which, if all the
data was projected upon that line, would have the greatest variance?  Would it
be the same line?  (It would).

What one line best represents the relationship between the students two SAT
scores?  Is it the same line?  (It is).

This one line is the first column of $V$ from the SVD.  We also call it the
first *principal component*.

Now, what if we removed all variability that was explained by that axis, so
all that was left was the error resulting from that compression.  What would
the second such line look like?  Is it this one?

![](2pcs.png)

(I stretched it out so the axes were about equal scale, showing that the two
are orthogonal).

This is the second column of $V$ from the SVD, and the second principal
component.

So principal components are important in a lot of ways!

# So how are these computed?

I really like [this description
here](https://jeremykun.com/2016/05/16/singular-value-decomposition-part-2-theorem-proof-algorithm/).
I'm going to summarize it for you, but that link is worth a read for more
detail.

First, let's define the term *projection*.  Suppose we have a vector space
$V$, and a point $p$ which does not lie in that vector space.  For example,
maybe the vector space is the $(x,y)$ plane, and the point is at $(3,2,2)$.
That point is not in that space.  However, there a point $p'$ within $V$ which
is the closest to $p$ (in this case, it's the point $(3,2,0)$).  $p'$ is the
*projection* of $p$ into $V$, also denoted $p'=proj_V(p)$.

![](projection.png)

Suppose $V$ is defined by a single unit vector $v$, so $V$ is really just a
line.  The distance of $p'$ from the origin is just the dot product $p\cdot
v$ (remember that $x\cdot y=|x||y|\cos(\theta)$, where $\theta$ is the angle
between the two, and use some basic trig to work out why).  So, the projection
of $p$ onto $V$ as $proj_V(p)=(p\cdot v)v$.  We
can write out a pythagorean theorem here, where $pp^T=(p\cdot
v)^2+distance(p,p')^2$. So, $distance(p,p')=pp^T-(p\cdot v)^2$.  Good?  Good.

![](proj.jpg)

So, let's define what we really want here.  Let $A$ be an $n\times m$ data
matrix.  Obviously, this means we have $n$ points described in $\Re^m$. When
we calculate the principal components, we're trying to find the set of $k$
vectors, where each vector is in $\Re^m$ (call the resulting $m\times k$
matrix $P$), whose span minimizes the sum of squared distances from the points
in $A$ to their projection in $P$.  In other words, we're finding the vector
space of rank $k$, where points have to change as little as possible to be
expressed in that new vector space.  Let's start with just setting $k=1$, and
look for the single best vector we could project onto.

So this means, we want to solve the following (let $A_i$ mean the $i$th data
point, or row, in $A$, and $U$ be the set of all unit vectors):

$$
\operatorname{argmin}_{v\in U} \sum_{i=1}^n dist(A_i,proj_v(A_i))^2\\
=\operatorname{argmin}_{v\in U} \sum_{i=1}^n A_iA_i^T-(A_i\cdot v)^2
$$

Now, the various $A_i$ are part of the problem, we can't change them.  So
minimizing that whole thing can only be done by maximizing the second term:

$$
\operatorname{argmax}_{v\in U} \sum_{i=1}^n (A_i\cdot v)^2\\
=\operatorname{argmax}_{v\in U} \sum_{i=1}^n A_i\cdot v\\
=\operatorname{argmax}_{v\in U} |Av|
$$

Now, it turns out that the first principal component (and the first singular
vector) is defined precisely as the solution to this problem, and the first
singular value is defined as $|Av|$!  So the first principal component gives
you the direction which best represents all the data, and the first singular
value tells you how much of the data's spread is captured by that first
singular vector (big numbers: data's really close to that line, small numbers:
the data isn't that close).

To calculate the second principal component, you do $A-proj_{v_1}(A)$ and
repeat.  The third, you repeat again.  And so on.

It turns out, using a proof that I'm not going to go into, but which is
detailed in the link above, that this greedy algorithm results in the best
combined subspace.

I'll also note that this whole thing can, and often is, rederived not by
minimizing the points' distance to the line, but by finding the one line along
which the projections have the largest variance.  So, line along which the
data is most spread out.  This can be a convenient way to think about it, as
well.

# What was all that, and why do we care?

A data matrix is expressed in terms of the observations and questions YOU
chose to ask, rather than something that has been determined by the data.
It's the few peepholes through which you're looking at the actual data, not
the actual data itself.  We'd like the questions we asked to reveal something
about the data itself.  If we look at it in lots and lots of different ways,
but in fact our data is entirely determined by just a few variables, we'd like
to know that!  PCA and the SVD tells us how many of these underlying variables
there are, and how they interact with the observations we've chosen to make.
