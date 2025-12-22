---
title: Unsupervised Learning
---


### Main points

- Unsupervised Learning is extremely useful for understanding a dataset
- Data labeling is time-intensive, so a huge chunk of the world's data is unlabeled. Learning as much as you can from unlabeled data is a necessity.
- Unsupervised Learning usually refers to either *clustering* or *dimensionality reduction*.
- Clustering lets you understand that, yes, ok, we have a very large amount of data, but really we can think of this as $k$ kinds of things, which is much easier.
- We will assume you remember how clustering works - if not, you can find the details in the ISL textbook.
- [Example of analysis through clustering here](foodCluster.html).
- Dimensionality reduction is useful for a couple reasons. First, it's useful for *compression*. Compression allows you to represent your data in potentially far fewer features, allowing for substantially faster computation. This is a very common first step in ML.
- Second, it's useful for analysis. [See an example here](PCAExample.html). And a second example, which doesn't have any references to the SVD, [here](pcaNoSVD.html).
