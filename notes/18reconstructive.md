# Reconstructive and Generative Embeddings

## Reconstructive Embeddings

The core principle of reconstructive embeddings is that the quality of a
learned representation, or embedding, is measured by its ability to
reconstruct the original input data from it, meaning it somehow encodes all
the necessary information, in a lower-dimensional latent space $z$, needed to
describe the data. The goal is not to generate new data but simply to compress
and describe existing data.

The most common model for this task is the Autoencoder (AE). An Autoencoder consists of two primary components: an **Encoder** and a **Decoder**. The Encoder $e(\cdot)$ is a network that maps the high-dimensional input data $X$ to the low-dimensional latent embedding $z$, as described by $z = e(X)$. The Decoder $d(\cdot)$ is a network that attempts to reverse this process, mapping the embedding $z$ back to a reconstruction $\hat{X}$ of the original input, such as $\hat{X} = d(z) = d(e(X))$.

This architecture forces the network to learn a compressed representation because the dimensionality of $z$ is significantly smaller than that of $X$, creating an "information bottleneck." To learn, the model is trained to minimize a **reconstruction loss**, which is simply the difference between the original input $X$ and its reconstruction $\hat{X}$. For image data, this loss function is often the Mean Squared Error (MSE), $L(X, \hat{X}) = ||X - \hat{X}||^2$, which penalizes differences in pixel values.

The resulting latent space of a standard Autoencoder is optimized purely for
this compression-reconstruction task. It is *not* structured for generation.
The space between learned data points in $z$ is often un-mapped and undefined.
If one were to sample two embeddings $z_1$ and $z_2$ from two different inputs
and interpolate between them, the decoded results would likely be non-sensical
or non-plausible, as the model has no incentive to make the whole of the
latent space meaningful.

A key variant is the **Denoising Autoencoder**, which is fed a corrupted input $X'$ but is trained to reconstruct the original *clean* data $X$. This forces the embedding $z$ to capture more robust and essential features, learning to discard noise. The most prominent application of reconstructive models is **anomaly detection**. A model trained only on "normal" data will learn to reconstruct it very well (low error). When presented with an anomalous sample, it will fail to reconstruct it accurately, resulting in a high reconstruction error that flags the data as an outlier. This approach is also widely used for dimensionality reduction and non-linear feature extraction.

## Generative Embeddings

The primary principle of generative embeddings is to learn to produce new
datapoints that appear as if they could be a member of a dataset.
Mathematically, we say that they are learning the underlying probability
distribution $P(X)$ of the training data. For example, if we are working with
a dataset of images of dogs, we start by thinking about all possible images,
including static, pictures of people, abstract art, etc. A small portion of
that space is likely to appear in a dataset of image sof dogs.

Unlike reconstructive models, which aim to compress and decompress known data,
generative models are designed to **synthesize new, novel data samples**
$\hat{X}$ that are plausible and appear to be drawn from the same distribution
as the original data. This requires learning a latent space $z$ that is not
just a compressed code but a structured, continuous representation from which
meaningful samples can be drawn.

### The Variational Autoencoder (VAE)

The **Variational Autoencoder (VAE)** is a probabilistic generative model that directly modifies the Autoencoder architecture to achieve this. It effectively builds a bridge between reconstruction and generation by imposing a specific structure on its latent space.

The VAE's encoder is **probabilistic**. Instead of mapping an input $X$ to a single, deterministic latent vector $z$, the encoder outputs the parameters—a mean vector $(\mu)$ and a variance vector $(\sigma^2)$—that define a Gaussian probability distribution. The latent vector $z$ is then *sampled* from this distribution, $z \sim \mathcal{N}(\mu, \sigma^2)$. This sampling step is a crucial distinction, as it introduces a controlled stochasticity into the encoding process.

The decoder $d(\cdot)$ functions as a "generator." It takes one of these sampled latent vectors $z$ and attempts to reconstruct the original input $\hat{X} = d(z)$.

The key to the VAE's function lies in its unique loss function, derived from the Evidence Lower Bound (ELBO), which has two components:

1.  **Reconstruction Loss:** This is the same as in a standard Autoencoder, such as Mean Squared Error $L(X, \hat{X})$. This term encourages the model to be a good autoencoder, ensuring that the sampled embedding $z$ contains enough information to faithfully reconstruct the original input $X$.
2.  **Kullback-Leibler (KL) Divergence:** This term $D_{KL}(\mathcal{N}(\mu, \sigma^2) || \mathcal{N}(0, I))$ acts as a powerful regularizer. It measures the difference between the distribution $\mathcal{N}(\mu, \sigma^2)$ output by the encoder and a standard normal distribution (mean=0, variance=1), which is set as a *prior*.

This KL divergence term forces the latent space to be **organized**. It penalizes the encoder for creating distributions that are far from the origin or have very small variances. This prevents the model from "cheating" by assigning each data point to a separate, non-overlapping region of the latent space. By forcing all encoded distributions toward the central $\mathcal{N}(0, I)$ prior, the VAE ensures the latent space is **continuous** and densely populated.

Because the latent space is continuous and centered, the VAE is generative. We can now discard the encoder, sample a random vector $z$ directly from the prior distribution $\mathcal{N}(0, I)$, and pass it to the decoder. The decoder, trained on this structured space, will generate a new, plausible data sample $\hat{X}$ that is not a copy of any single item in the training set.

### Generative Adversarial Networks (GANs)

A different generative philosophy is used by **Generative Adversarial Networks (GANs)**. GANs do not use reconstruction. Instead, they model the generation process as a zero-sum game between two competing networks:

1.  A **Generator $G(\cdot)$** takes a random noise vector $z$ (sampled from $\mathcal{N}(0, I)$) and attempts to create a fake data sample $\hat{X} = G(z)$.
2.  A **Discriminator $D(\cdot)$** acts as a classifier, trained to distinguish real data $X$ from the generator's fake data $\hat{X}$.

The Generator is trained to produce fakes that *fool* the Discriminator, while the Discriminator is trained to *not be fooled*. This adversarial process forces the Generator to produce increasingly realistic samples. The latent space $z$ of a GAN learns a complex mapping from simple noise to the data manifold, often resulting in sharper, more realistic images than VAEs, though their training is known to be less stable.
