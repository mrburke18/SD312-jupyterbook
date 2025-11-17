# Neural Net Outputs and Cost Functions

Neural Nets are very modular, where we can roughly break it down into three sections.  The first section is used to develop features that are useful for understanding the data.  You'll see domain-specific solutions here, where certain types of layers make good features for sound, or for images, or language, or what-have-you.  The second section is the fully-connected section, consisting of a few rows of normal linear-with-nonlinear-activation-function hidden layers.  This section is really good at finding interactions between the features that have been developed.  Here the human pretty much just needs to decide on a depth and width.  The final section is the output layers, which solve the type of problem you're looking to solve.  Today we'll be focusing on the options for that final section.

In particular, we're going to be focusing on solutions which result in useful representations for Regression, probability estimates (for Classification, for example), and embeddings.

## Regression

Regression is the easiest one.  If you're trying to regress upon a single number, you'll have a single output node.  This is most frequently a node that just does a single linear combination (with no activation function) of all those useful features constructed by the previous layers, outputting a single number, which is interpreted as the prediction $\hat y_i$ for the input data $x_i$ (where the right answer is $y_i$).  When this is pushed through as a batch of datapoints $\textbf{X}$, you end up with a vector of predictions $\hat {\textbf{y}}$, with one element for each row of $\textbf{X}$.

The **loss function** for this neural net would then usually be the Mean Squared Error between the vector you should have gotten, and the vector that was actually output.  The smaller this loss function is, the better your predictions on the dataset have become.

If you want to predict multiple things with the same data, you can have multiple output nodes, each of which are predicting their own individual thing from the common features developed by the previous layers.  Minimizing a single loss function which adds the MSEs of each output node would result in the learning of features that enable all the predictions you're trying to make.

## Probability Representation

To think about this, let's start by thinking about classification.  We have seen how a logistic regressor, which outputs a "probability of being in a specific class" can be a useful thing - it understands and communicates uncertainty.  In more complicated classification scenarios, this can even go further - suppose we're trying to classify what a picture is of.  We can imagine a "dog" class, and a "road" class, and a "ball" class.  But, what if it's a dog with a ball on a road?  Coming down firmly on one specific class could only mean overfitting, because there are multiple right answers.

Our logistic regressor did a linear combination of features $x_i w$, which was then fed into teh logistic sigmoid: $\frac{e^{x_i w}}{1+e^{x_i w}}$, which represented the probability.  $x_i w$ is referred to as a *logit*.

It is common for neural nets built around classification to have an output neuron for each of the classes; for example, a "dog" neuron, and a "road" neuron, and a "cow" neuron.  Each of these outputs a logit.  To turn this into a probability, we take the logit value output from a neuron, apply the exponent function, and divide it by the sum of the exponents of all the logits.  The bigger the logit, the bigger the probability.

Suppose for our picture of a dog on a road, the "dog" neuron outputs a logit of 1.2, the "road" neuron outputs 1.7, and the "cow" neuron outputs a logit of -.5.  We then call exp() on each of these, and get 3.32, 5.47, and .61.  We then calculate $\frac{3.32}{3.32+5.47+.61}=.35$ for dog, $\frac{5.47}{3.32+5.47+.61}=.58$ for road, and $\frac{.61}{3.32+5.47+.61}=.06$ for cow.  So, according to our neural net, there's a 35% chance it's a dog, a 58% chance it's a road, and a 6% chance it's a cow, resulting in a final output of the vector [.35,.58,.06].  This operation from logits to probabilities is called the "softmax" operator.

To train this, we then compare this to the label.  Suppose the human labeling the dataset has decided this is a picture of a dog.  The "right" answer therefore, would be [1,0,0].  We can compare this desired vector to our actual output using "cross entropy loss."  The derivation of this is outside the scope of our course, but this is a way to compare two probability distributions to each other - if they're identical, the value is 0; if different, the value increases.

## Embeddings

Neural networks are often used to create compressed versions of complex objects.  Imagine, for instance, a neural net that takes an input vector of size 30, then has a hidden layer of size 5, and then an output layer of size 30 again.  We could write a loss function based around the reconstruction error, comparing the output vector to the input vector.  This would train the neural net to compress the data as effectively as possible so it could be reproduced.  This temporary vector of size 5 is an example of an embedding.

One example of the use of an embedding is in facial recognition.  In facial recognition, a neural network compresses an image down to a smaller vector.  Given two images, we can write a loss function on the resulting two vectors.  If the images are of the same person (albeit from differing angles/lighting/facial hair/etc), then the resulting embedding vectors should be similar.  If the images are of different people, they should be different.

A facial recognition system then could compare the embedding of a picture of a face from a security camera to the embeddings of every drivers license photograph in the state, and compare their differences.  The most similar embeddings can then be investigated further.

Word (or document) embeddings are another famously useful example of embeddings.  Two words should have similar embeddings if they can be swapped in for each other in documents without the change making the documents less likely.
