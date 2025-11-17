# K-Means Clustering

This portion should be done in a Jupyter notebook.

Implement K-Means Clustering.  Write a function that takes in an $n\times m$
data matrix and a value for $k$, and returns a $k\times m$ matrix of centroids,
an $n\times 1$ vector of integers describing which cluster each row belongs to,
and the average distance from every data point to its centroid (this is a
single scalar).  As much as possible, this should be done using numpy/scipy
functions which will run in C, making it much faster.  Your code should be
short as a result! Try not to loop over rows or columns of the matrix.

Given the "Some points" data set, run k-means 100 times for each value of $k$
from 2-20.  Plot (1) the best average distance found for each value of $k$ over the 100 runs, and
(2) the mean average distance for each value of $k$ over the 100 runs.

For a choice informed by the above graph, display the data and the $k$
centroids.  The data should be colored to make it clear which cluster each
belongs to.

This portion should be submitted as an HTML file from the notebook as `kmeans`.

![](images/unsupervisedcomic.jpg){width=45%}

*comic by [thejenkinscomic](https://thejenkinscomic.wordpress.com/2022/09/23/unsupervised-learning/)*
