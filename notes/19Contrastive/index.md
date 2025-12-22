---
title: Contrastive Learning and Facial Recognition
---

Oftentimes, we want to calculate an embedding based purely on the idea that if two points are similar, their low-dimensional embeddings should be similar, as well; also, if two points are *not* similar, their low-dimensional embeddings should also not be similar.

We can define "similar" in all sorts of ways.  Perhaps, for example, we want to say that all words that can fill in the following gap in the sentence are similar: "The `______` slept on the rug in the sun."  Certainly, we can imagine various words that go there (dog, cat), but they're all similar in some meaningful way (small domestic animals). If our embedding respected that similarity, then small domestic animals would all be similar in our embedding space, while other words would not be.  If we consider many, many sentences with gaps and define similar similarities, then many complex relationships that are otherwise hard to mathematically define between words would appear in the distances between embeddings.  Importantly, we could do this with only a large enough corpus of English text (ie, the internet), and no labels, as we could manufacture our own sentences with gaps.

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

[You can see an example of a system like this being trained here](contLearn.html).
