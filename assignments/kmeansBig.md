---
title: NY Times Dataset
---

First, [review the notes on how to use the cluster](https://www.usna.edu/Users/cs/taylor/si470/resources/cluster.html).

On that cluster, let's cluster using the [NY Times Bag of Words data set](https://archive.ics.uci.edu/ml/datasets/Bag+of+Words).

1. On that page, "Download" has a link to a .zip file you should put in your beegfs folder.  `wget` or `curl` are good tools for downloading files without a browser.

2. Using [sklearn's clustering
package](https://scikit-learn.org/stable/modules/clustering.html) (which is a great example of documentation done extremely right, and nearly stands as a clustering textbook itself), find
something interesting to say about this data set.  Based on the centroid
values, what words appear in the largest and most dense clusters?  What topics
got clustered together?  What was in the news?  Write me a brief report on this, telling me what you
did, and what your results are.

Some thoughts that will likely help:

- This is a very large dataset, and you will have difficulty fitting it into
  memory!  Fortunately, it's also very *sparse*, in that the vast majority of
the entries are 0. [Scipy offers a set of data structures for storing sparse
matricies](https://docs.scipy.org/doc/scipy/reference/sparse.html) that you
can use like any other numpy array.  Ones worth noting are csc_matrix, which
is fast for column slicing, but slow for row slicing; scr_matrix, which is
fast for row slicing, but slow for column slicing; and coo_matrix or
lil_matrix, which are fast for construction, and then can be converted into one of the other two (but cannot itself be sliced or used in arithmatic).  Look at the documentation for these types to learn more!
- If you need it, there's also a `himem` HPC cluster partition, so that can help. Remember, there's only 4 of those, and there's more than 4 groups in this class, so if you go this route, you have to share.
- Right now, words like "the" get equal weight to others, like "politics." Should being 10 "the"s different count the same as being 10 "politics" different?  Probably not.  Consider _normalizing_ your dataset by dividing the counts by the (number of times the word appears in the whole dataset/1000) so that words that tend to show up a lot have to have a bigger difference to make the documents far apart (the 1000 is just so all your values aren't tiny).  Even better, implement [tf-idf weighting](https://en.wikipedia.org/wiki/Tf%E2%80%93idf).
- This code will take a long time to run!  Waiting until the night before is likely impossible!
- I will expect that you perform some dimensionality reduction in your final product.
- Because you're working on the compute cluster, you'll be running this as a program, not as a Jupyter notebook.  Your submission can therefore be as a just a normal PDF that you've written up.
- Develop on a small version of the dataset, so you don't have to wait for everything to run on the full one.
- Develop a basic, technically working full pipeline, and then begin improving individual steps.
- Consider saving results at useful stopping points so that you can just load results partway through, rather than having to rerun everything over and over again.

An 'A' not only has some interesting results, but also demonstrates curiosity,
in which you try some extra stuff (preprocessing, other algorithms, etc.), and
explains well what you did and why.

Please submit to the submit system as `03NYTimesClustering`.

[Don't forget your effort survey](https://docs.google.com/forms/d/e/1FAIpQLSdKOIUX-cMiHmgA5EjI-6_vD8-IuIYpXHAP7xdrFQ7ATE1b_A/viewform?usp=sf_link).
