# Discriminative Embeddings

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

## Discriminative Embeddings

Oftentimes, we want to calculate an embedding based purely on the idea that if
two points are similar, their low-dimensional embeddings should be similar, as
well; also, if two points are *not* similar, their low-dimensional embeddings
should also not be similar. These are called *discriminative* embeddings,
because we're learning how to put points in space where we can easily
distinguish between different types of things.

We can define "similar" in all sorts of ways.  Perhaps, for example, we want
to say that all words that can fill in the following gap in the sentence are
similar: "The `______` slept on the rug in the sun."  Certainly, we can
imagine various words that go there (dog, cat), but they're all similar in
some meaningful way (small domestic animals). If our embedding respected that
similarity, then small domestic animals would all be similar in our embedding
space, while other words would not be.  If we consider many, many sentences
with gaps and define similar similarities, then many complex relationships
that are otherwise hard to mathematically define between words would appear in
the distances between embeddings.  Importantly, we could do this with only a
large enough corpus of English text (ie, the internet), and no labels, as we
could manufacture our own sentences with gaps.

In another example, perhaps we're trying to learn things about time series
data, which is something being measured over time. It is common that we have a
lot of data, and very little of it is labeled, so doing supervised learning
(what activity is happening at a given point in time, or does this engine
being monitored need maintenance) requires very smart feature engineering and
expensive human labeling. Instead, perhaps we say that moments close in time
to each other are similar (because things don't change too quickly) and all
other points are dissimilar. Once we train an embedding, moments in time are
organized in a space where supervised learning is easier, allowing for less
labeling. [This by the way is one of my research
areas](https://arxiv.org/abs/2410.15416).

This type of embedding learning, where we try to define a push-pull between similar and dissimilar objects, is known as Contrastive Learning, and is a core concept in a number of applications.

One good case study of this is in facial recognition.  Suppose we have a dataset of pictures of faces from various angles, lightings, facial hair, sunglasses, etc (the first datasets of this came from tabloids, who have many pictures of many celebrities).  We want to train an embeddings so that two pictures of the same person will be close together, and two pictures of different people will be far apart.

We define a neural network $E$ which takes in a facial image $x$ and outputs a small-dimensional embedding $E(x)$.  A single training "point" will actually consist of three images, an *anchor* image $a_i$, another image of the same person (known as the *positive* image) $p_i$, and an image of a different person (known as the *negative* image) $n_i$.  For each such $(a_i,p_i,n_i)$ sample, we calculate and seek to minimize the *Triplet loss*, defined as

$$
\begin{align*}
L(a_i,p_i,n_i)=\max\left[ \| E(a_i)-E(p_i)\|_2-\| E(a_i)-E(n_i)\|_2 +margin, 0\right].
\end{align*}
$$

The loss function over the entire dataset is therefore $\sum_i L(a_i, p_i, n_i)$.

To understand this loss function, start by focusing on the $\| E(a)-E(p)\|_2-\| E(a)-E(n)\|_2$ terms.  In order to minimize this, the distance between $E(a)$ and $E(n)$ must be larger than the distance between $E(a)$ and $E(p)$. This is to say, the embeddings of the anchor and negative pictures (those of different people) must be further from each other than the embeddings of the anchor and positive pictures (those of the same people).  Minimizing this results in the embeddings of $a$ and $p$ moving closer together, and the embeddings of $a$ and $n$ moving further apart.

Now, consider we have two sets of images in our batches, $a_1, p_1, n_1$ and $a_2, p_2, n_2$.  Data point 1 ($a_1, p_1, n_1$) is already well behaved, where the embeddings behave as we like.  Data point 2, on the other hand, is not.  We'd like the overall loss function to prioritize working on data point 2, rather than just continuing to optimize the good-enough data point 1.  To do this, we define a "margin," which is a measure of this loss function that is "good enough," where no more optimization is required or helpful.  This is the role of the margin and max terms in the Triplet loss.  Once the difference between the distances is sufficiently large, there is no longer any benefit to enlarging it.

Once you have trained this system for long enough, you trust it to make the embeddings of images of the same person close, and the embeddings of images of different people far apart, even for people whose faces were not in the training set.  You then assemble a set of "gallery images" of people you might be interested in recognizing (Maryland police, for example, have the Maryland Image Repository System of drivers' license photographs, mug shots, and other photographs shared by nearby states).  You take each of those faces in your gallery, and calculate their embeddings.  Then, when you have a "probe image," like an image from a security or doorbell camera, you calculate that image's embedding, and extract the $k$ closest embeddings from the gallery images.  Those are your suspects.

[You can see an example of code that would train something like this
here](17contLearn), though it won't have run due to technical limitations on
the web server.
