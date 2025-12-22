---
title: NNs for Regression and Classification
---

This lecture is about the common *output layers* of neural networks built for
regression and classification, and the loss functions used to optimize them.

**Main Points**

- For **regression**, output layers are typically just a linear combination,
  with no activation function. They are performing linear regression on the
  features designed by the earlier layers.
- These networks are then typically trained using squared error.
  - Even if the function is called "MSE", it is not uncommon for the
    implementation to by default skip dividing by the size of the set. This
    makes calculating somewhat faster (as it skips the division, which is
    unnecessary for minimization), but makes comparing training/testing error
    more difficult as the datasets may be different sizes.
- You can have multiple output nodes if regressing on multiple functions with
  the same data simultaneously. They will share features, but combine them
  differently to fit their separate functions.
- For **classification**, normally there is an output node for each possible
  class. These output nodes have no activation functions and so output a *logit*, like for logistic regression.
- These outputs are then put through a *softmax* function.  If $z_i$ is the output logit of the $i$th class, then the softmax function is $\frac{e^{z_i}}{\sum_j e^{z_j}}$.
- This number is between 0 and 1, and the sum of all the results of all classes sums to 1, so the outputs, after applying softmax, can be interpreted as a vector of probabilities.
  - For example, suppose we are classifying an image as one of dog, cat, or bird. Our output layer would have three nodes outputting logits. Suppose the "dog" neuron outputs a logit of 1.2, the "cat" outputs a logit of 1.7, and the "bird" outputs a logit of -.5.
  - We then call exp() on each of these, and get 3.32, 5.47, and .61.  We then calculate $\frac{3.32}{3.32+5.47+.61}=.35$ for dog, $\frac{5.47}{3.32+5.47+.61}=.58$ for cat, and $\frac{.61}{3.32+5.47+.61}=.06$ for bird.  So, according to our neural net, there's a 35% chance it's a dog, a 58% chance it's a cat, and a 6% chance it's a bird, resulting in a final output of the vector [.35,.58,.06].
  - To train this, we then compare this to the label.  Suppose the human labeling the dataset has decided this is a picture of a dog.  The "right" answer therefore, would be [1,0,0].  We can compare this desired vector to our actual output using *"cross entropy loss."*
- If you remember your logistic regression, cross-entropy loss will look very similar (this is perhaps not a surprise - after all, both are performing classification by outputting probabilities).
- Define $p(x)$ to be the "true" probability for a data point and class (for example, $p(dog)$ in the above example would be 1, and $p(cat)$ and $p(bird)$ would be 0). Define $q(x)$ to be the output probability (in our example, this would be pulled from the vector [.35,.58,.06]).
- The cross entropy loss for a single datapoint is calculated as:

$$
\begin{align*}
-\sum_x p(x) \log_2 q(x).
\end{align*}
$$

- So, for our example, the cross entropy loss would be:

$$
\begin{align*}
-\sum_x p(x) \log_2 q(x) =& -((1)\log_2(.35)+(0)\log_2(.58)+(0)\log_2(.06))\\
=& 1.515
\end{align*}
$$

- Over a dataset, we sum up the cross entropy loss of each datapoint to arrive at an overall loss.
- Like with logistic regression, minimizing the cross entropy is equivalent to maximizing the likelihood. You can think of likelihood in the following way.  Suppose the neural net were correct about all its probabilities, meaning that if you asked a huge number of human labelers, that picture really is labeled a dog 35% of the time, and a cat 58% of the time, and a bird 6% (perhaps there's a cat in the foreground, a dog in the background, and a shadow that looks like a bird).  The fact that the picture is labeled as a dog is somewhat unlikely, but not impossible (35% likely!).  We could compile all these likelihoods for the whole dataset, and quantify how likely the dataset as a whole is, assuming the model is correct. Changing the model would then change this cumulative likelihood.  In some sense, the "best" model is the one that maximizes this likelihood - and minimizes cross-entropy loss.

Multi-Class Classification:
[You can see a notebook demonstrating a classification problem here](Classification.html).

Binary Classification:
The ships demo of a Fully Connected Binary Classifier example with L2 regularization.
[Binary Ships Classifier Here!](ships_example.html).



