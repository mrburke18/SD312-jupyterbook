# Data Matrices

In Discrete Math and AI, you learned the fundamentals of linear algebra, which is the kind of math we most frequently do with matrices of data measurements.  You will need this knowledge!  A review reading is available for you from the main page.

Suppose a $n$ people have written down their ratings for $k$ movies.  We can organize this into a table of numerical rankings, which is $n$ tall and $k$ wide.  We say this matrix of numbers is $n\times k$ (# of rows first).

A row of this matrix is a *datapoint*.  It's one person's worth of measurements.  It consists of $k$ numbers, so we can also think of it as a point in $k$-dimensional space, or a vector in $k$ dimensional space.  Sometimes this will be convenient, such as if we want to talk about "is this person similar to that person," can be turned into "is their datapoint close to that person's datapoint?"  We can denote a point in $k$-dimensional space by saying that the row $\in \Re^k$, which is the set of all $k$-dimensional points (all combinations of $k$ real numbers).

A column of this matrix is a *feature*.  Features are points or vectors in $n$-dimensional space.  If two movies are very similar, probably the community of people rated them similarly - again, we can talk about the similarity of features using distance.

Finally, the matrix as a whole contains a lot of useful information.  For example, maybe you didn't know that two movies would be rated the same.  Maybe how much you like one movie strongly suggests if you'll like a different movie.  Maybe you can figure out if people can be accurately broken down into groups, like action fans or romance fans.

There will be lots of interesting things we'll do with matrices in this class, so pay attention to the reading!
