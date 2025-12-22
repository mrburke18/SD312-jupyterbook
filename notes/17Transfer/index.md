---
title: Transfer Learning
---

Convolutional networks (and other kinds of feature extractors) tend to work far better when very, very deep.  This causes problems because in any standard problem, you don't have enough data to train a very, very deep network without extreme overfitting (if you can even afford the compute to do so!).  So, it *seems* that the actual applicability of convolutional networks and other feature extractors is limited.

In practice, we rarely train these things from scratch ourselves.  Instead, we allow a big research shop like someone in academia or Google to train a network on a similar problem (with sufficient data) which will likely create similar features to what we want.  For example, suppose we want to classify the difference between horses and mules, and we only have a hundred pictures of each.  Well, a network trained to classify the difference between many, many things would likely build useful features which would help to solve this much simpler problem.

Such a network would consist of a feature extraction portion, followed by a dense network to perform the classification using the extracted features.  So, we can take the trained feature extraction layers, with the trained weights, and glue it onto a new (untrained) dense layer that performs the task we want it to perform (like, for example, classifying into our two classes).  We can then either train only that dense portion (if we believe the features to be sufficient) or the whole network (if we believe the features should be fine-tuned for the new problem).

**Problems Transfer Learning can solve...**

- Small amounts of data for exquisite problem.
  
- Time is short... --and/or--

- Computational Power is limited...

