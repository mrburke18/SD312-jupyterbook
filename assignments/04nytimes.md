# Clustering a very large dataset

Sometimes, when doing ML, we are bound by the size of a dataset and
limitations of our compute. Our tricks can be mathematical or computational;
in this lab we'll have to explore some of those.

## Explaining the dataset

[This dataset](nytimes.tgz) consists of two files, `docword.nytimes.txt` and
`vocab.nytimes.txt`. Together, they encode wordcounts from a corpus of NY
Times articles.  For reference, here are the first few lines of
`docword.nytimes.txt`:

```
300000
102660
69679427
1 413 1
1 534 1
1 2340 1
...
```

The first three lines are metadata - there are 300000 articles represented,
and 102660 words being counted. There are a total of 69,679,427 cases where a
word appears in an article. In article 1, word 413 appears once. Also in
article 1, word 534 appears once, as does word 2340.

The words these correspond to are in `vocab.nytimes.txt`. The first word is
`aah`. Word 2 is `aahed`, and word 413 is `actually`.  So `actually` appears
in article 1 once.

## The task

The goal is to cluster these articles and look at the words heavily used by
the centroids to understand what these articles are about. For example, if you
look at a centroid and see that the most heavily used words are "covid" and
"vaccine," then you've learned something about what that cluster of articles
is about.

## Making data smaller and algorithms faster

Normally before clustering we would make an $n\times m$ matrix, where $n$ is
the number of articles (300000), and $m$ is the number of words (102660). Each
entry is an integer, and there would have to be $300000 \times 102660 =
3\times 10^10$ of them.  At 4 bytes an integer, that's 123 GB just to
represent the matrix. So, we won't be doing that.

Fortunately, this array is very *sparse*, meaning that the vast majority of
the values of the array are 0, because most words are not used in most
articles (in fact, only $\frac{69679427}{3\times 10^10}=2.3\times 10^{-3}$, or
.2% are non-zero).

[There are a number of data structures for storing sparse matrices more
efficiently](https://docs.scipy.org/doc/scipy/reference/sparse.html). The
basic idea is that rather than storing the matrix, we store the locations and
value of the rare non-zero value. Each non-zero takes more space (because it
must be accompanied by a location), but you're not storing zeros at all. The
data structure you choose will determine how long everything that follows will
take to run.

We'll also want to reduce the dimension, because when we cluster, we don't
want to have to calculate distance in 102,000-dimensional space. So some
dimensionality reduction is in order. Now this can't be PCA, because the first
step in PCA is to center the data, and that would result in a very non-sparse
matrix.

Lastly, clustering K-means with 300000 articles might be slow!

## Your job

So, cluster the dataset. Whatever approaches you use you must explain and
justify. You must demonstrate that you understand what is happening in the
choices you make. You may use generative AI to help with syntax and coding,
but not in knowing what to do next. In other words, you can use it to help
with your coding, but you should be telling it what the next steps are, not
the other way around.
