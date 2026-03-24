# Adversarial Examples

Our big neural nets have been designed and trained in a very empirical way - in other words, if they work, we have not thought very hard about them.  One question we might ask is, are there inputs we could put into this network that behave very poorly?  What do they look like?  Can we *create* them?

The answer is, it's quite easy to create such *adversarial examples*.  The
idea is very simple.  We have a loss function that declares what "right" is.
Normally, we put a datapoint through, calculate the loss, and then perform
gradient descent on the parameters of the network to make it smaller, thus
training *the network* to perform better.  What happens if we leave the
parameters of the network alone and instead, after calculating the loss, we
*calculate the gradient with respect to the pixels of the image* and **update
the pixels of the image** with the goal of reducing the loss to a *wrong* classification for that image? With a few repeated tiny updates of the pixels, the result is a change to the *predicted label* of our example to a desired "wrong" classification.

[Here is but one example (among hundreds of attacks) of this kind of adversarial attack](adversarial.html).  In this example, we train a network which classifies goats (class 0) from mules (class 1) from unicorns (class 2).  We then have an image of a goat, meaning normally we optimize the network until it outputs [1, 0, 0].  In this case, we're going to optimize the image until the network outputs [0, 1, 0].  We're going to try to do this without changing the image too much visually.

Our attack here is called the Fast Gradient Sign Attack (FGSM).  The algorithm works like this:

- Calculate the gradient with respect to the image of the loss function on the image and desired output.  This gradient would have a component for every channel of every pixel.
- Replace each component with the sign of that component, losing all magnitude information, and replacing each with a +1 or -1.
- Multiply this by some small number epsilon.
- Subtract this from the image, making it slightly more likely to be (desirably) misclassified when pushed through again.

This sign attack limits the amount of change on any channel on each iteration, allowing us to limit the total change on the image, making it harder to visually detect.

In this example, we are able to manipulate the picture of our goat from being 95% likely to be a goat to 100% likely to be a mule in only five iterations, with no real visual affect.

## Variations

This idea opens the door to many variations of this attack.

- [Stickers that make a stop sign be misclassified as a speed limit sign](https://medium.com/self-driving-cars/adversarial-traffic-signs-fd16b7171906)
- [A sweatshirt which makes it so you are not classified as human](https://www.cs.umd.edu/~tomg/projects/invisible/)
- [An attack that makes images misbehave under facial recognition](https://arxiv.org/pdf/2101.07922.pdf)

[There is also *poisoning*, in which training data is altered in order to cause misbehavior in future testing examples.](https://arxiv.org/pdf/2009.02276.pdf)
