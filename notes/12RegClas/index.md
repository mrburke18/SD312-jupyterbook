# NNs for Regression and Classification

This lecture is about the common *output layers* of neural networks built for
regression and classification, and the loss functions used to optimize them.


Multi-Class Classification:
[You can see a notebook demonstrating a classification problem here](Classification.html).

Binary Classification:
The ships demo of a Fully Connected Binary Classifier example with L2 regularization.
[Binary Ships Classifier Here!](ships_example.html).


## Regression

* **Output Layer Structure**: The output layer typically consists of one or more nodes with no activation function, effectively performing a linear combination of the features extracted by previous layers.
* **Multiple Outputs**: Multiple output nodes allow the network to regress on several functions simultaneously using the same input data. While these nodes share underlying features, they combine them differently to fit their respective targets.
* **Loss Function**: These networks are standardly trained using **Squared Error**.
* **Implementation Note**: While often referred to as Mean Squared Error (MSE), some implementations omit the division by the dataset size during calculation to increase computational efficiency. While this does not affect the minimization process, it can make comparing training and testing errors difficult across datasets of different sizes.

## Classification 

The network generally contains one output node per possible class.

1. **Logits**: Output nodes initially produce raw numerical values called *logits** ($z_i$), which (just like in regression) are simply linear
combinations of features that do not use an activation function.
2. **Softmax Function**: To interpret these as probabilities, the logits are passed through the **softmax** function:

$$\sigma(z)_i = \frac{e^{z_i}}{\sum_{j=1}^{K} e^{z_j}}$$

This ensures each output is between 0 and 1, and that the sum of all outputs equals 1, creating a valid probability distribution.
3. Example: In a dog/cat/bird classifier, if the output logits are $1.2$, $1.7$, and $-0.5$ respectively, the softmax conversion results in a probability vector of $[0.35, 0.58, 0.06]$.

### Cross-Entropy Loss

Model performance is evaluated by comparing the predicted probability vector
$q(x)$ to the "true" probability vector $p(x)$ (typically a one-hot encoded vector where the correct class is 1 and others are 0). The **Cross-Entropy Loss** for a single data point is calculated as:

$$H(p, q) = -\sum_{x} p(x) \log_2 q(x)$$

* **Optimization**: Minimizing cross-entropy is mathematically equivalent to
 maximizing the **likelihood** of the dataset given the model parameters.
 This should look familiar to you given your familiarity with logistic
 regression.
* You can think of likelihood in the following way.  Suppose the neural net were correct about all its probabilities, meaning that if you asked a huge number of human labelers, that picture really is labeled a dog 35% of the time, and a cat 58% of the time, and a bird 6% (perhaps there's a cat in the foreground, a dog in the background, and a shadow that looks like a bird).  The fact that the picture is labeled as a dog is somewhat unlikely, but not impossible (35% likely!).  We could compile all these likelihoods for the whole dataset, and quantify how likely the dataset as a whole is, assuming the model is correct. Changing the model would then change this cumulative likelihood.  In some sense, the "best" model is the one that maximizes this likelihood - and minimizes cross-entropy loss.
