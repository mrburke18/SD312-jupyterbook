---
title: Diffusion and Large-Language Models
---

So now we've seen some of the major parts of neural nets, so we can understand a bit better how these pieces can be put together in order to create some of the tools that are making a big impact today.  Let's start by talking about...

### Diffusion Models

Diffusion Models are the basis of most of the image-creation tools we see and maybe use, like Stable Diffusion, or Midjourney.  They all have a slightly different approach, but many of the ideas are the same.  First let's talk about the components, and then maybe we can understand how they all can go together to make a full tool.

The first element to think about is **denoising**.  You can perhaps imagine constructing a dataset where we take some images, and artificially add noise.  We could then build a neural net which takes in a noisy image, and is intended to output a less-noisy version; an error function would be easy to write (difference between the produced image, and the actual image from prior to noising), and so we could imagine training this in a fairly straightforward fashion.  We could do this with data points that weren't images, too, but were instead just vectors from a certain well-defined dataset.  We could pass in a noised vector, and it would output one that would be more likely to actually be a datapoint from the set.

Once we have such a system, we could imagine passing a vector through the denoiser over and over again, and producing an interatively-less-noisy version.  We could even start with a perfectly random vector, pass it through again and again, and it would eventually output a vector that actually looks like a random datapoint that could be concieveably be from the dataset.

The second thing to think about is an **upsampler**, which takes a small image, and produces a larger, more detailed version of that image.  Again, this is easy to image training, where you take some high-resolution images, downsample them, and then train a network to take the downsampled images and produce an image as close as possible to the full-resolution image.

The third thing to think about is an images **latent space**, which you can think of as compression, or an embedding.  Suppose we built a network which consisted of an *encoder*, (which takes in an image, and produces a smaller-dimensional embedding), and a *decoder* (which takes in an embedding, and produces an image).  We could imagine training this with the intention of having the encoded-then-decoded image looking as similar as possible to the original image.  If we did this, we could then view the embedding as a chokepoint, where the most crucial information about what the image should look like is encoded efficiently in a small-dimensional space.  This embedding, of course, is just a vector; you could even imagine creating a random embedding, and therefore producing a coherent, if random, decoded image.

The final thing to think about is the **embedding of the prompt**.  We have talked about how we can take text, embed each word, push them through some transformers, and produce an embedding that encodes the meaning of that text.  We could even imagine training a dual image-and-description network which is designed to produce similar embeddings from an image, and from a textual description of that image.

We now have all the parts necessary to create a diffusion model.  We train an image-and-text encoder-decoder with the following properties: the latent space of the encoded image is similar to the embedding of the text description, and the decoded image is similar to the original.  For the purposes of this description, imagine the latent space is a vector of size 512.

We then separately build a denoiser, which denoises vectors from the latent space.  We generate the latent encodings of many, many images, and store those vectors of size 512.  We then noise them, and train the denoiser to produce the original, denoised vector.

We then train an upsampler to take an image of the size created by the decoder, and produce a higher-resolution version.

Finally, we have a system.  The text prompt is inputted, and the embedding created.  We then create a random latent space vector, and iteratively denoise it, over and over, with some encouragement to come out more similar to the textual embedding.  We then take the denoised vector, and decode it, to create a small image.  We then upsample it to create a high-resolution version.  Voila!  A high-resolution random (thanks to the randomly initialized latent vector) image, which could be described by the given prompt.

### Large-Language Models

Large-Language Models are actually conceptually much more simple, though they're difficult to engineer and train.  LLMs are essentially classifiers, which take in some text, and output a probability distribution over all the words in the output language, which represent the likelihood that word would be the next word in the text chain.  This dataset for training is pretty easy to put together.  Given this probabilistic output, the system can then randomly choose a word from the output distribution (where it's more likely to choose the higher-probability words), and then input the resulting string, with the new word, into itself again, outputting the next word, and so on until complete.


