---
title: Matrix Completion
---

The goal of this lab is to apply all that we learned in the lab last week on the MIDN dataset to understanding a full ML development cycle.

### A note about supervised learning model development

Last week, you developed a method for performing matrix completion.  The *parameters* of this method were $P$ and $Q$, which were trained on the training data.  In order to do this, you first had to choose *hyperparameters*, like the assumed rank.  Creating a good ML predictive model consists of choosing the best hyperparameters, and then learning the best parameters for those hyperparameters.

So, how do we choose the best hyperparameters?  Well, if you've split your data into training, validation, and testing data, the best hyperparameters are the ones where, once you've learned the best parameters, the validation error is best.  So, in the case of this application, you would try a variety of ranks, and for each attempted rank, optimize it as best you can on the training data.  Whichever rank resulted in the best validation error is the model you would deploy.

So, the overall supervised model construction process looks like this:

- Split data into train/validation/test sets.
- For each of many hyperparameter settings,
  - train the parameters as best you can on the training data.
  - note the validation error
- keep the version that resulted in the best validation error

To illustrate this with a different model, consider linear regression.  Your *parameters* are the weights being applied to the features.  The *hyperparameters* are the feature set and the regularization parameter.

### Your task

Given the [ml-latest-small](https://grouplens.org/datasets/movielens/) movielens dataset, augment your existing notebook (copy it or convert and use as a source file for functions, rename to 05MatrixCompletion_<last_name>.ipynb) you just turned in to perform matrix completion on that dataset.

You will probably want a function that accepts a rank, and performs as many epochs of matrix completion as necessary to train the model (how will you know? Yes, **number of epochs** can be another hyperparameter. You can also run until a goal error is reached or that max number of epochs whichever is sooner), and then returns the validation error and resulting $P$ and $Q$.  You can then call that function on a loop iterating through various ranks to determine the best rank.

After all is said and done, test your best model with the testing set and record the results of the final training error, validation error, and testing error.

Add a row to the dataset with several movie rankings of your own.  You can do this either in your notebook, or just by adding some ratings to ratings.csv  as a userId that is not present. Recommend some movies to yourself based on predicted ratings.  

Questions:

1. What differences did you observe in model convergence and performance across your ks?

2. Did your training error differ from your validation error?  Why do you think this is or is not?

3. Did your end validation error differ from your testing error? By how much? was it more or less? What did you expect and does this conform with your expectations?

If you were unable to get your lab 04 to work, [you can use these functions](05MatComp.ipynb). Tell me if you plan to do this!
