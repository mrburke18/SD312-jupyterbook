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

It is very important in all of our techniques, that you understand when the
technique is appropriate, and when it is not. You must also understand that
when you choose an approach, you have chosen a set of assumptions, which may
or may not be appropriate.

### Assumptions and Limitations

* **Assumption of :** The algorithm assumes the number of clusters, , is known.
* **Validation:** Because the data is unlabeled, there is no ground truth to verify if the clusters are "correct." The results are exploratory and qualitative.

You can see an [example of analysis through clustering here](./foodCluster.html).

## Dimensionality Reduction

Dimensionality reduction transforms high-dimensional data into a lower-dimensional representation.

This approach serves two main functions:

1. **Compression:** By representing data with fewer features, we reduce storage requirements and substantially increase the speed of subsequent computational steps (e.g., in Machine Learning pipelines).
2. **Analysis:** It facilitates the visualization of complex datasets, allowing for the identification of patterns that are not visible in high-dimensional space.

You can [see an example of analysis through PCA here](./PCAExample.html).
  And a second example, which doesn't have any references to the SVD, [here](./pcaNoSVD.html).
