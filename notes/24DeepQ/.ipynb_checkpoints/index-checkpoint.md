---
title: Deep Q-Learning
---

Tabular Q-Learning is a great algorithm for understanding Bellman error and how Q-values can adjust themselves until accurate given sufficient experience.  However, it's not realistic for real problems.  It has a few issues:

- The state space and action space both have to be discrete and small in order to actually list and store an approximation for every state-action pair. This itself is disqualifying for most problems.
- It's extremely inefficient. Every state-action pair has to have sufficient experience in order to become accurate. Given an experience at one state, we have no ability to update our expectations in *similar* states - they have to have independent experiences.  There's no generalization in what we learn.
- Each $(s,a,r,s')$ sample is only used once to update.  This seems sensible until you realize that $\hat Q(s',a')$ might change, therefore introducing new meaning into the $(s,a,r,s')$ sample that transitions into that state - why not learn from it again?

In many ways, this is similar to performing regression under a scenario where we keep an explicit table of the predicted values for every possible input.  We have never done this.  It would be stupid.  In some ways, that's notetaking, not machine learning.

Instead in regression, what we did was write a generalizing function that could take in any of our possible datapoints, perform some math on its elements, and then output a prediction.  This might be linear, for example: we take in a datapoint, calculate some interesting features, and then calculate weights which, when applied to the features, result in an accurate prediction.  When we adjust the weights to make a datapoint more accurate, we're adjusting the predictions of *all* datapoints, allowing us to learn generalizable things.  Alternatively, we might learn a neural network instead, which learns features for us - again, however, we can put in datapoints we've never experienced, and hope to get out an accurate prediction.

In RL, we can do similar things, where we write a function that takes in a state and an action, and spits out a predicted value.  Again, this could be linear, where the state-action pair are converted into some interesting features, then a linear combination is computed which results in accurate value predictions. [Our own Professor Taylor focused some of his dissertation on this kind of work, thinking about what such features should be](https://citeseerx.ist.psu.edu/document?repid=rep1&type=pdf&doi=21d38a3f57821e4343301d8cee1d81d660145806).  Updating the common weights to make the Bellman error more accurate on our samples may result in accurate value predictions even for state-action pairs that have never been experienced.

Alternatively, we could create a neural network, where a state is fed in, and the network has a output layer with a node for each action, producing the expected value of taking each action from that state.  Again, if adequately trained, any state could be fed in, and reasonable Q values produced.

These approaches solve both of the problems described for Tabular Q-Learning.  Our state space can now be continuous, or as large as we want, and we're learning generalizable facts about states, since every state is processed with the same function.  Noteably, the action space must still be small and discrete, as we have a finite number of nodes in the output layer.

We're going to learn about the neural net approach, called Deep Q-Learning, which is very well described [in this significant and well-written paper from 2013](https://arxiv.org/pdf/1312.5602.pdf).  We are going to use this paper as a text - it is expected that you will understand elements of this.

Important elements of this paper that are applicable to all deep q-learning implementations:

- The network takes in a datapoint, and has an output node for each possible action.
- The network is trained to minimize Bellman error, using the network as the source of $\hat Q(s,a)$ for both sides of the Bellman equation.
- Rather than training only on the most recent transitions, which are heavily correlated and may cause overtraining on that weird thing that happened recently, transitions are stored in an *experience replay*, which is a queue of the $N$ most recent transitions, where $N$ is fairly large. Samples for training are then randomly chosen from those $N$ transitions.  This keeps training batches varied and uncorrelated, but still recent enough to be relevant (choosing $N$ is a hyperparameter that trades off between these concerns).

There are several more interesting elements that had to be engineered to make this work on Atari games in particular.

- The source of all inputs was the actual image on the screen.
- An image on the screen doesn't reflect motion (we can see the ball/character/sprite, but we can't tell which way it's going), so a "state" is actually a set of four consecutive images resulting from taking an action four timesteps in a row.
- The image was processed in various ways that made it easier to learn on.
