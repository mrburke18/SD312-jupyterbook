# Data Exploration with Clustering

As we've seen, clustering can be a valuable tool in understanding the structure of complex data.  For this next assignment, you're going to practice this.

In June of 2023, [Fajzel et al. published a paper called "The Global Human Day,"](https://www.pnas.org/doi/full/10.1073/pnas.2219564120) in the Proceedings of the National Academy of Sciences.  A primary contribution of this paper is a dataset which estimates the amount of time the average resident of a country spends doing a variety of different tasks (Table 2 in the paper contains the full list of subcategories).

The dataset we'll be using [is best downloaded here](https://zenodo.org/record/8040631), by clicking "Download" next to GlobalHumanDay.zip.  When you unzip that, go into `outputData`; we'll be using `all_countries.csv`, which contains calculated estimates for each country for each subcategory.  For example, on the first line of the dataset, we see that Aruba (ABW) spends 1.47 hours per day on food preparation; on the second line, we see the same country spends 0.17 hours per day on food growth and collection.

You'll want to start by reworking this dataset into a data matrix, where a row
is a country, and a column is a subcategory (ie, the numbers on a row should add up to ~24 hrs).

Begin with a basic exploration of the dataset. Is everything there? On what
subcategories does the world spend the most time on? Least time? Which
features have the most variance? Are any heavily correlated with each other?
Should countries' populations be taken into account with any of these answers?

Once you've done that, I would like you to cluster countries based on their
average day, so that countries that spend their time on the same things end up
in the same cluster.

**It's important you understand how the scikit-learn (aka
sklearn) library works, so for the actual clustering, do not use generative
AI.** Instead, consult [the
documentation](https://scikit-learn.org/stable/modules/clustering.html), which
is fantastic, and almost a machine learning textbook on its own.

What can you tell me about the different kinds of countries, and how they spend their time?  Do there seem to be economic or population reasons for why?  For example, do the elements of one cluster have more people than countries in another?  Once you've done your clustering, analyzing through a lens of economics, population, density, etc. are all fair game.

Demonstrated curiosity is rewarded, and you must include at least one other dataset in your analysis.

Only one partner needs to submit something.  [Don't forget the effort
survey,](https://docs.google.com/forms/d/e/1FAIpQLSeZhPrXQqjub_teh6AUgxwN2nllkezqK6mn5ryYxVh7ZjCBHQ/viewform?usp=dialog)
or to include a Generative AI statement.
