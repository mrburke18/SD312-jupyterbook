# Language Processing and LLMs

This week we're going to do a high-level flythrough of LLMs and textual
generative AI. Just as image-based ML was unlocked with the creation of
convolutional layers, text-based ML was unlocked with the more recent
creation of transformers in a paper significant enough [to have its own
Wikipedia page](https://en.wikipedia.org/wiki/Attention_Is_All_You_Need).

In this first lecture, we're going to walk through the creation of feature
extractors for language, which are the backbone of networks that do all sort
of interesting things with language.

## The Decomposition of Language via Tokenization

The first stage in the Transformer pipeline is **Tokenization**, the process
of partitioning raw text into discrete numerical units. Modern Transformers
employ **sub-word tokenization**, where the language is broken down into a
discrete set of portions of words that have meaning. This method decomposes
words into the smallest sequences of characters that appear frequently in a
training corpus. For example, the word **"transformed"** may be broken into
three tokens: `trans` (a prefix indicating movement or change), `form` (the
root), and `ed` (a suffix denoting past tense). This structural breakdown
allows the model to handle rare or unseen words by interpreting their
constituent parts, ensuring it can derive meaning from a word like
"translocate" if it has previously encountered its components in other
contexts.

Tokens must be embedded - after all, neural nets can't work on words, they
need to work on numbers, so we need to create a vector to represent each
token. If those vectors are meaningful such that the geometry of embeddings
are semantically meaningful, so much the better (for example, perhaps the
embeddings of "hot" and "warm" should be close together, because they mean
similar things, while a word like "astronomy" should be quite distant, because
its meaning and use is quite different).

Naturally, we learn these embeddings through self-supervised learning, so we
can make use of the massive amount of unlabeled text available online. We task
the embedding model with a proxy problem, such as **Masked Language
Modeling**. In this scenario, the model is given a head that can classify over
all tokens and is given a sentence like "The chef cooked a delicious
**[MASK]**" and must predict the hidden token. To succeed, the model must
learn the statistical relationships between "chef," "cooked," and potential
targets like "meal" or "steak." Through backpropagation, the model adjusts the
token vectors until it can perform this task, and the geometric distances
between word embeddings accurately reflect these linguistic patterns.

## Contextual Refinement via Self-Attention

While embeddings provide a general definition of tokens, they don't solve the
whole problem. For example, consider the definition of "crane." Do you mean
the bird, or the construction equipment? The answer depends upon the context
of the sentence it is used in. The **Self-Attention** mechanism provides the
specific context required for this understanding. Self-attention allows each token in a sequence to "communicate" with every other token to resolve ambiguity. For example, in the sentence "The **crane** flew over the construction site," the mechanism calculates a high attention score between **"crane"** and **"flew,"** signaling that the word refers to a bird. If the sentence were "The **crane** lifted the steel beam," the attention would shift to "lifted" and "steel," updating the representation of "crane" to reflect a piece of machinery. This is achieved through three learned linear projections: **Queries** (what a token is seeking), **Keys** (what a token contains), and **Values** (the information content).

## The Transformer Block and Hierarchical Feature Extraction

A **Transformer Block** is the fundamental unit of the architecture, housing the multi-head self-attention mechanism and a position-wise feed-forward network. By stacking these blocks, the model functions as a hierarchical feature extractor, analogous to the layers of a **Convolutional Neural Network (CNN)**. In a CNN, early layers detect simple edges and textures while later layers identify complex objects like faces. Similarly, the initial blocks of a Transformer extract simple syntax and local word relationships. As data progresses through deeper layers, the model extracts increasingly abstract features, such as logical intent, thematic consistency, and global context. This stacking transforms raw token embeddings into sophisticated representations of human language.
