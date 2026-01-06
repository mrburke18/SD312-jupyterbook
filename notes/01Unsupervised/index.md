# Unsupervised Learning

You are already familiar with unsupervised learning, but perhaps it is not
clear *why* you would do unsupervised learning. It makes a good place for us
to start, and transition to thinking about subjects in ML in our way, using
material you're already familiar with.

Unsupervised learning involves the analysis of datasets lacking labeled response variables. As data labeling is a time-intensive process, the vast majority of real-world data remains unlabeled. Consequently, unsupervised learning is often the necessary first step in data science pipelines, serving as a primary tool for exploratory data analysis.

The two primary categories of unsupervised learning are **Clustering** and **Dimensionality Reduction**.

## Clustering

Clustering reduces complex datasets by grouping observations into  distinct categories or "kinds" of things.

We assume you recall how K-Means works; if you don't, feel free to refer back
to the ISL textbook.

In this class, it is important to understand what mathematics are being done,
but we will generally not implement these algorithms ourselves. Instead, we
focus on understanding the human side - under what circumstances is this
algorithm appropriate? What assumptions does it bring? Are those assumptions
correct? What are the hyperparameters, and how do I choose them?
:::{margin}
**Parameter**: a variable or value computed by a machine learning algorithm in
order to minimize some function.

**Hyperparameter**: a variable or value chosen by the person setting up the
machine learning problem.
:::

K-Means is a useful way for us to demonstrate this thought process, though we
won't always list all these so explicitly.

**Hyperparameter**: K-Means takes in a human-chosen value $K$. $K$ is the
hyperparameter.

**Assumptions**: K-Means uses the K-Means algorithm to place all datapoints
into one of $K$ clusters, each of which is based around a centroid. It
minimizes the sum of within-cluster variance over all the clusters, so it
prefers round clusters. When you choose K-Means, you are assuming that round
clusters around a centroid are a good answer for your problem.

**How do we tune the hyperparameter**: An illustration of one way to choose
$K$ is in our example notebook. There is much art in this process - a good
practice is to try many different values of $K$, and draw conclusions from the
results from them all, rather than over-trusting the results of a single run.

You can see an [example of analysis through clustering
here](./02foodCluster.ipynb).

## Dimensionality Reduction

Dimensionality reduction transforms high-dimensional data into a lower-dimensional representation.

This approach serves two main functions:

1. **Compression:** By representing data with fewer features, we reduce storage requirements and substantially increase the speed of subsequent computational steps (e.g., in Machine Learning pipelines).
2. **Analysis:** It facilitates the visualization of complex datasets, allowing for the identification of patterns that are not visible in high-dimensional space.

You can [see an example of analysis through PCA here](./pcaNoSVD.ipynb).
