# Movie Recommendations

For this project, we'll be using the data sets of movie rankings from the
[movielens web site](https://grouplens.org/datasets/movielens/).  You'll want
to start with the ml-latest-small, under "recommended for education and
development."

Assume your viewer has just finished one of the following movies (taken from
the USNA movies dataset):

- Black Panther
- Pitch Perfect
- Star Wars: The Last Jedi
- It
- The Big Sick
- Lady Bird
- Pirates of the Caribbean
- Despicable Me
- Coco
- John Wick
- Mamma Mia
- Three Billboards Outside Ebbing Missouri
- The Incredibles

Using the ml-latest-small dataset, recommend ten movies which are similar to
the movie they just finished using the k-NN approach.  Do this for each of
these movies.  Can you scale up to the larger dataset?

Useful libraries will likely include
[scipy.spatial.distance](https://docs.scipy.org/doc/scipy/reference/spatial.distance.html)
and
[sklearn.neighbors](https://scikit-learn.org/stable/modules/neighbors.html#neighbors).

An 'A' tries different distance metrics, and/or different ways of filling in blanks, qualitatively decides what's best, and states why you think that approach is working the best.

Give me a writeup explaining what you did, and what resulted in improved
recommendations.  This could be either a writeup in PDF format, or a notebook
downloaded in HTML format.

[Effort
survey](https://docs.google.com/forms/d/e/1FAIpQLSf33kWtQVHu_jiuuPg1RWAG5KHIB0SSK36ZaFY8rkDrnAbVow/viewform?usp=dialog)
