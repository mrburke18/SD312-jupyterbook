---
title: Data Exploration with Unsupervised Learning
---

As we've seen, unsupervised learning can be a valuable tool in understanding the structure of complex data.  For this next assignment, you're going to practice this.  Start by downloading [this jupyter notebook](unsupervised.ipynb) to modify.  You can download files like this by right-clicking, and choose "Save Link As", or, if you're on a terminal, with `wget --no-check-certificate <url>` or `curl -O <url>`.

Organize yourself, and make a directory for your course, and within that, for this lab, and put the file and dataset in there.  We're going to have a lot of datasets and code, and you'll want to be able to track what's what.

In June of 2023, [Fajzel et al. published a paper called "The Global Human Day,"](https://www.pnas.org/doi/full/10.1073/pnas.2219564120) in the Proceedings of the National Academy of Sciences.  A primary contribution of this paper is a dataset which estimates the amount of time the average resident of a country spends doing a variety of different tasks (Table 2 in the paper contains the full list of subcategories).

The dataset we'll be using [is best downloaded here](https://zenodo.org/record/8040631), by clicking "Download" next to GlobalHumanDay.zip.  When you unzip that, go into `outputData`; we'll be using `all_countries.csv`, which contains calculated estimates for each country for each subcategory.  For example, on the first line of the dataset, we see that Aruba (ABW) spends 1.47 hours per day on food preparation; on the second line, we see the same country spends 0.17 hours per day on food growth and collection.

I would like you to explore this dataset using unsupervised learning.  First, you are going to cluster countries based on their average day, so that countries that spend their time on the same things end up in the same cluster.  This will require you to rework the dataset a bit so that a row contains all the estimated times for a country (ie, the numbers on a row should add up to ~24 hrs) - we have given you this code.

Once you've done that, you will use PCA to explore how different countries trade off their time.

Submit your .ipynb file as `01unsupervised` at `submit.usna.edu`.

This is due before next lab on 1/16.
