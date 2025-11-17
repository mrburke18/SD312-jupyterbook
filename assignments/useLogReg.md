# Classifiers!

On the Datasets page is a dataset labeled "Census Income."  Given a variety of factors, we are going to try to predict whether somebody makes over $50K/yr.  It has been split into a training and testing set for you already; adult.data is the training data, adult.test is the testing data.  You'll note the final column is either >50K or <=50K - this is our target, or what we're trying to predict.

Your ultimate goal is to build the best possible predictor you can, using both a logistic regressor and a SVM, then analyze it to tell me what has the biggest impact on a person's income.  You'll turn in a Jupyter Notebook for this.

Here are some things you'll want to think about.

- The two classes are unbalanced.  Imagine an extreme case in which 99% of a
  dataset is in class A, and 1% is in class B.  An optimizer can easily get to
99% accuracy just by saying everything is in class A... but that's not that
helpful. To fix this, ptimization functions can be altered to punish errors in
one  directory more than in the other direction, encouraging the optimizer to
find a more legitimate decision boundary. Read the documentation!
- Your report should include a *confusion matrix*, which shows how well you are predicting each of the two classes.
- Several of these provided features are *categorical* (for example, race, in which each person is in one of several bins).  It is common to turn a categorical feature into *one-hot encoding*.  For example, suppose we have a feature which is the color of a car.  You look at your dataset, and see that cars are either black, white, or red.  You turn this into three features.  The first of these is 1 if the car is black, and 0 if it's anything else.  The second is 1 if it's white, and 0 if it's anything else.  The third is 1 if it's red, and 0 if it's anything else.  You'll find the pandas function `get_dummies` to be shockingly helpful with this.
- Your regularization parameters should be chosen based on performance on the test set.
- You should try augmenting or otherwise altering your feature set.  For example, perhaps you want to make the "education level" from categorical to an estimated number of years in school.  Or, perhaps you want to combine many smaller types of jobs into one larger type of job, so it doesn't overfit.  Or, perhaps you want to include monomials on some of the numerical values.  You won't get an A without altering your feature set.
- For the SVM, you should try multiple kernel choices.
- I'd like to see more automated approaches now.  For example, a loop which
  runs for multiple regularization values, keeping the one which is best on
the test set.
- SVMs are fast for what they are, which is a nonlinear optimizer... but
  nonlinear optimizers are slow (for example, there is an inversion of an
$n\times n$ matrix, where $n$ is the number of data points... That's roughly
$O(n^3)$.  So, polynomial, but slow).  Expect SVMs to take some time.
