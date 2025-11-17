# Movie Rating Completion

Given the movielens dataset, we want a recommendation system which uses low-rank matrix completion to make recommendations.  Create a new row on the movielens rating matrix, for yourself, with several ratings filled in for your own preferences.  Perform matrix completion and make recommendations for yourself.  Your work should be presented in a PDF or HTML file.

I want you to implement this algorithm yourself, not use any libraries. You
may use Generative AI in reading in and cleaning the data, and in making
plots, but not in performing the algorithm.

You'll need to perform the following steps:

- Randomly split the available ratings into training and testing sets.
- Choose a rank to assume about your dataset.
- Construct and randomly initialize $P$ and $Q$.
- Perform the algorithm.  Every several steps, print out the RMSE for the reconstructed training set, and the RMSE for the reconstructed testing set.  For a set of indices of known values $T$, RMSE is calculated as:

$$
RMSE = \sqrt{\frac{1}{|T|}\sum_{ij\in T} (A_{ij}-p_iq_j)^2}.
$$

- Stop the algorithm when testing error bottoms out.

RMSE, of course, is like the loss function that we're minimizing.  $|T|$ is the number of elements in the set $T$, therefore averaging that, so they're comparable between different sized sets.  Finally, the square root makes it so it's in the original units, making it easy to think about how wrong your model is.

- Produce recommendations for yourself.  Are they any good?

Things you may want to consider:

- Rows or columns of the matrix that are very sparse will be difficult to predict on.  Maybe users that haven't seen many movies or movies almost nobody's seen should be thrown out.
- You will have to choose a rank to assume about your dataset.  Smaller ranks assume a lot of structure, allow for faster learning, generalize to testing data better, and depend upon less data for good results.  Larger ranks assume less structure, require more learning and data, but are more flexible and able to represent more personalized results.
- Your initialization of $P$ and $Q$ will have heavy impact on how long it takes to find an optimum (big values, and you might even have numerical overflow when you do the dot products).  How should you initialize those matrices so you start off in the ballpark (for example, if ratings are 1-5, and you initialize $P$ and $Q$ with large values, your initial predictions will be way too large)?
