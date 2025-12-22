---
title: Embeddings and Autoencoders
---

An application of neural nets that has been growing in importance is in
learning useful *embeddings*.  An embedding is a low-dimensional
representation of a data point, which encodes some useful information.  One example of an embedding is PCA, where we can condense each point down to a point in some lower-dimensional space, without losing much variance.

For another example, suppose we'd like to do something neural-netty on text.
Well, you can't do math on words, so each word needs to map to a numerical
value before it can be used as an input.  You could do this naively, for
example, by making `aardvark` map to 1, and `abacus` map to 2, and so on
through the dictionary.  Each word now has a number, but those numbers are
meaningless; it would be better for ML purposes if words that were synonyms
had similar mappings, so that the network they were input into viewed them
similarly.

For example, there is a famous result from a technique called Word2Vec, which
creates embeddings for words, where each word is represented as a point in
200-(or so)-dimensional space.  They showed that the learned embedding for
"king" (a point in 200-dimensional space) minus the embedding for "man"
(another point in 200-dimensional space, so subtraction just works), plus the
embedding for "woman," got you a new point in 200-dimensional space which was
very close to the embedding for "queen."  So, `king - man + woman = queen`.
So, these embeddings seemed to encode actual meaning, not just being a
computationally-necessary translation from words to numbers.  If two words had
similar embeddings, that meant those words meant about the same thing.

As another example into why these might be so useful, consider if we could
create an embedding for text and an embedding for an image such that the
textual description of an image (like "[an inspiring watercolor painting of a
majestic goat at sunset, standing over a defeated, mangy
mule](https://gemini.google.com/share/9562e18969de)") and the embedding of the
image itself would be very similar.  Training embeddings like this is an
important step in Image Search and in AI that generates images from
descriptions.

This week we're going to learn about two (of many) ways to train embeddings.
Today is...

### Autoencoders

Autoencoders are a form of unsupervised learning and are best thought of as learned compression and decompression
algorithms.  Imagine we have some datapoint (it's easy to imagine it as an image, but it doesn't have to be) that is high-dimensional.  We then create a network where each layer of the network contains fewer and fewer nodes, ultimately condensing down to a much smaller number.  This small vector is known as the *latent space*, and this first half of the network is known as the *encoder*.

We then widen the network again, taking the small sized vector and widening it until it once again reproduces a data point the same size as the original datapoint.  This is called the decoder.

We can then train it based on reconstruction error, attempting to minimize the difference between what is input and what is output.  If successful, you've created a compression system; you divorce the encoder from the decoder, and then data can be encoded, then cheaply transfered in the small latent space, then decoded, with little loss.

Now, we can get a little weird.  Suppose we have only the decoder.  Every point in the latent space can be rendered by a decoder into an image.  So, if we could plug in the right point in latent space, we could create an entirely new image that way. However, constraints as they are currently defined give no guarantees that any randomly selected point in latent space will necessarily decode into a meaningful output, or in other words an output that would sensibly belong to the dataset or represent a natural transition within it. For example, given our 28x28 MNIST digits dataset, consider a 28x28 image of a unicorn or Abe Lincoln... these are possible images in that 28x28x1 framework, but do not belong to the manifold representing the MNIST dataset in its input space. A randomly selected latent encoding could, just as likely, instead produce such an off-manifold output when decoded.  Likewise, nothing about this architecture enforces continuity, i.e., the idea that two points which are close in proximity in the latent space should produce outputs which are close or similar to one another.

To produce continuous and meaningful (or *on-manifold*) outputs, we have to add an extra requirement to the autoencoder - the space needs to not only be small-dimensional, but the compressed versions of "real" inputs need to lie somewhere predictable in that latent space, so we can create new points in that place where real images lie and decode them into something sensible for the trained dataset. 

Now we've arrived at the need for a *Variational Autoencoder (VAE)*. VAEs encode inputs as distributions instead of a fixed m-dimensional point in latent space. Additionally, the latent space in properly tuned VAEs is structured such that it is regularized by constraining the constituent latent-space distributions (in each latent-space dimension) to be well-behaved Gaussians which have a mean close to zero and a standard deviation close to 1. With these constraints, the resulting model will encode data close together and encourage some overlapping of distributions. Together these properties combine to result in a latent space structure with the desired continuity and on-manifold dataset representation. These properties can come at the price of a higher decoding error, however, a tradeoff which can be managed by hyper-parameter tuning. 

Continuity and completeness in manifold representation tend to result in smooth transitions over the properties or information encoded in the latent space. Thus a point in latent space which is equidistant between the means of two encoded (latent space) distributions should result in a decoded datapoint which is intermediate between the two source inputs for those encoded distributions.  

And so, with the above, we have provided some motivation for and intuition about our first *generative* ML model. [See an example of a VAE for MNIST here](mnist.html).
