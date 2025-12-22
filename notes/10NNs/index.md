---
title: Neurons and neural nets
---

Prime takeaways:

- A *neuron* takes in a number of features, performs a linear combination of them, then applies a nonlinear "activation function" to the result. The weights of the linear combination are learnable to make the final output of the neuron more accurate.
- A single neuron is not particularly useful, and can be better replaced with a more standard linear model, which can usually be trained faster.
- However, if the output of one neuron is used as an input to a second neuron, then the first one can be said to have produced a *feature* for the second neuron.
- By training all neurons at the same time, we can learn useful features to then be linearly combined by the final output neuron.

[A demonstration of this idea using the Pytorch library can be found here](NeuronWeb.html).
