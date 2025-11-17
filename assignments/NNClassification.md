#Classification using Neural Networks

Using your (filled-in) data for the bankruptcies, build a classifier using a feed-forward neural network.  To do this, you'll have to make decisions on the following hyperparameters:

- Depth of the model
- Width of each layer
- How long to train
- Optimizer learning rate

It's unclear which of these will have the biggest effect, so use a random hyperparameter search to decide.  Write a program which takes the above as command line arguments, and then builds and trains the network, then write a script that runs it repeatedly with random values within a sane range to try lots of options.

Submit your code and a pdf explaining your results.  Your pdf should include a graph of the training and testing loss as a function of training epochs.

Tribble is not so big - be a good shared-resource citizen, and try to share.  Don't run too many jobs in a row, and only use one GPU at a time.  Running things overnight is a good idea.
