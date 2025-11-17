# Perceptron

The reading you did from LFD does a nice job of introducing the perceptron, but I wanted to provide a little more context.

The perceptron was developed in the late 50s, primarily by Frank Rosenblatt of
Cornell, on a grant from the Office of Naval Research.  The perceptron kicked
off the first big AI boom, where AI was expected to solve everything, soon.
From [the NY Times article "New Navy Device Learns by
Doing"](https://www.nytimes.com/1958/07/08/archives/new-navy-device-learns-by-doing-psychologist-shows-embryo-of.html),
*"The service said it would use this principle to build the first of its
Perceptron thinking machines, that will be able to read and write.  It is
expected to be finished in about a year at a cost of $100,000 ... Later
Perceptrons will be able to recognize people and call out their names and
instantly translate speech in one language to speech or language in another
language."*  The Navy was wrong.

Instead, in the 60s, Marvin Minsky published a book proving the theoretical limitations of the perceptron (namely, that it could only learn classifiers on data that was *linearly separable*), and everybody got very angry at each other for a couple decades.

However, when lots and lots of perceptrons are combined such that the outputs of some become the inputs to others, this creates a neural network, which does not have the same limitations, and is indeed resulting in machines that can do all the things the Navy promised, just way after the one-year deadline, and at a much higher cost than predicted, perhaps making it a pretty typical Navy project.

Some people claim that perceptrons act like neurons in the brain, an idea you will occasionally see referenced in popular articles about neural networks.  These people are right from a very high, hand-wavy, computer-scientist level of understanding of biology, but are very upsetting to actual biologists.

## A Mathematical Note on the Algorithm

Recall that the book introduces the following weight vector update rule, for some data-label pair $(x(t),y(t))$:

$$
w(t+1)=w(t)+y(t)x(t).
$$

For my notation, I'm going to drop the time notation, and introduce a subscript to indicate the data point, so,

$$
w\leftarrow w+y_ix_i.
$$

The book does not derive this at all, which is too bad, as it's easy and is simply SGD.

First, we define a loss function $L$ to minimize.  In this function, let $M$ be the set of data points that are misclassified.

$$
L(D,w)=\sum_{(x_i,y_i)\in M}-y_iw^Tx_i
$$

Because we want to perform *stochastic* gradient descent, we don't calculate the gradient of this function on all data points, but rather, just on one element of $M$ at a time.  For a given element $(x_i,y_i)$, that results in this loss function:

$$
L((x_i,y_i),w)=-y_iw^Tx_i.
$$

As we know, the SGD update is: $w\leftarrow w-\alpha \nabla_w L(D,w)$.  So, we now need the gradient with respect to w:

$$
\nabla_w L=-y_ix_i
$$

Plug it in to SGD, and: $w\leftarrow w+\alpha y_ix_i$.  Choose $\alpha=1$, and we're left with $w\leftarrow w+y_ix_i$, which is of course just the perceptron update as written in the book.

## What can perceptrons do?

The perceptron algorithm has the following guarantees:

- If the training data is linearly separable, the perceptron algorithm will eventually build a perfect classifier for that training data.
- That's it.

Notably missing from that list?

- Speed.  If a solution exists, there is no guarantee that the perceptron will find it quickly.
- Halting.  If a solution does not exist, the algorithm will run forever.
- Good-enough-ness.  If a perceptron has been training for a long time, and you check in on it, there's no guarantee that it will be getting *almost* everything right.
