# Supervised Learning

## Unsupervised Wrapup

We've just finished our unit on unsupervised learning.  Unsupervised learning mostly consists of clustering and dimensionality reduction.  Here are some high-level things I hope you understand now!

- Unsupervised learning has a heavy "art" component, due to not knowing what the "right" answer is.
- Unsupervised learning can be used to understand and summarize a data set.
- Unsupervised learning can be a first step on a variety of data-driven tasks to simplify a data set in either of its dimensions.
- Though it's limited, unsupervised learning is incredibly important, due to the fact that most data is not labeled.

## Supervised Learning

Though appropriate data for supervised learning is much more rare, supervised learning is a much more approachable problem, because it is much easier to measure success.  It's also where you go from "understanding and summarizing data" to "building systems that make predictions and decisions autonomously."

In this lecture, we're going to preview the basic construction and concepts of a supervised learning problem.

In supervised learning, each data point comes with a *label*.  The goal is to train a system which, given a new data point, is able to correctly predict the label that should be assigned to that data point.  If the label is a continuous number, this is known as *regression*.  If it's a member of a discrete set, it's known as *classification*.

We will first, though, study a rarer problem called *matrix completion*, which is a core approach to recommender systems, which is not technically either regression nor classification.

The underlying difficulty in ML is that we are trying to build a predictor that will work on ANY data point, despite the fact that we only have a sampling of those possible data points.  So, we are trying to learn things about the data we have that is generalizable to other examples.  Most of learning about supervised learning is about how we can produce good, generalized learning from our examples.

From a high level, the assumption we depend upon is that the data we have is a reasonable representation of all possible data sets; if we can build a system that works well on the data we have, then we should be able to trust that it will also work well on new data points.

The data we use to train our system is called the *training data* or the *training set*.  If our training data doesn't look like the data we'll actually use the system on, then our assumptions are invalid.

We commonly solve supervised learning problems via optimization problems: "build the version of this predictor that minimizes error on the training data."  Sometimes, though, this causes us to overlearn on the training set, where we perform very well on the data we have, but we have learned things that are too specific, and do not generalize to new data points.  We call this *overfitting*.

We can usually modify our problem design to reduce the risk of overfitting.  We call the things we can change *hyperparameters*.  For example, in K-Means clustering, the choice of K is a hyperparameter - it's a choice you made prior to optimization.

To choose appropriate hyperparameters, we often take our collected data and split it into two data sets, the *training set*, and the *testing set*.  We train our learner on the training set, and never allow it to see the testing set while improving.  We can then give it the testing set and see how well it performs, giving us a good idea of how well it generalizes.  In response, we alter our hyperparameters in a way that we hope would cause the error on our testing set to improve, even if it means performing worse on the training set.  We will learn a lot about how to do these modifications.

```
while the testing error is unacceptable
  choose hyperparameters
  perform optimization with the training set to build the best model with those hyperparameters
  check testing error
```
