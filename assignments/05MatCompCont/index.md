# Matrix Completion, Part 2

Now that you've performed matrix completion on a small dataset, it's time to do it for the large dataset of movie ratings. Our goal now is to focus on all the non-implementation things we have to think about in building a good ML model.

Make a new notebook called `05MatrixComp.ipynb`, and copy over all your
functions. Create an additional function which takes in your full reproduction
of $A^*=PQ$ and a user row index, and returns the names of the ten movies that
you are predicting they'll like the most, that they have not yet watched.

Build the best model you can, where "best" is defined in terms of test error and qualitative performance.  To do this well, you should demonstrate appropriate and well-explained searches for optimizing the following:

- Some users or movies may be inadequately rated, and cannot be learned well. Decide if you want to eliminate rows or columns based on numbers of ratings.
- Your chosen value of assumed rank $k$.
- Your learning rate.
- Your policy for early stopping.

To help you qualitatively measure its performance, create a few new rows for your ratings matrix. One should be you and some of your ratings for these movies. Others should be representative users with different interests (one who likes comedy and dislikes action, one who likes rom-coms, one who like Tom Cruise, etc.) Make predictions for yourself and these other users.

Your submission will be graded based on the completeness and technical correctness of your hyperparameter search, the completeness of your qualitative exploration, and the ease of reading your explanation.

`~/bin/submit -c=SD312 -p=lab05_matrix_comp_2 05MatrixComp.ipynb`
