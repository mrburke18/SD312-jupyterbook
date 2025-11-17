# Neural Net Feature Generators

For many kinds of data, fully-connected networks like we've learned about are sufficient, learning useful features based around the interactions between the observed dimensions and nonlinear transformations. However, there are some kinds of data for which we have especially good ideas - and this is where neural nets have really changed the state of the art.

## Image Data

The neural net boom really took off when [a deep network decisively moved the state of the art in the ImageNet image classification competition in 2012](https://en.wikipedia.org/wiki/AlexNet). They key was the deep implementation of convolutional layers, which look for patterns in 2D regions in images (or other grid-like data).  This allows the network to consider relationships between neighboring pixels, rather than considering every pixel value to be independent.  As with much of neural nets, convolutional networks weren't a new idea, but the ability to perform computation on a deep enough version wasn't around until more recently.

Convolutional layers are built around *filters*.  Suppose a filter is 3x3; therefore, it consists of 9 numbers.  That filter then looks at every 3x3 block of pixels in the image, and outputs a number for each which indicates the similarity between the filter's 9 numbers and that block's 9 numbers. So, a grid (the image) comes in, and a grid (similarity values to the filter) come back out, but now it's converted from pixel values to places where that filter's values are mirrored in the image.  So, if the filter, for instance, represents a line moving from lower left to upper right, the filter's output will show us everywhere in the image that appears.

We then do this with a lot of filters. So, after the first layer, we now know everywhere there's ascending lines, descending lines, etc.  We can then apply new filters to those grids, potentially learning, for instance, where ascending lines then become descending lines, creating upward-facing triangles (which might be useful features in detecting, for instance, cat ears).

The makeup of the filters is what is learned; those filter values are learned via optimization to be the filters that best help later parts of the network do whatever the task is.

[Stanford has some good, more complete, notes about the details of conv nets here](https://cs231n.github.io/convolutional-networks/)

## Time-Series Data (like text)

*Time-Series Data* refers to data that comes in a sequence, where the order matters.  Language is a great example: "You will do this" and "Will you do this" differ only in word order, but the meaning is very different.  It's also very complex - consider the meaning of the word "it" in the sentences: "The cat drank the milk. It felt better." and "The cat drank the milk. It was refreshing."  Grammatically, there are no rules distinguishing when "it" refers to the cat, and when "it" refers to the milk; it depends entirely on the meaning of the surrounding words.  This is a very hard computational problem.  Very recently (2017), a feature generator called a *transformer* was described to learn this kind of understanding - these transformers are what is behind the sudden success of large language models.

Transformers are built around the idea of *attention*, where it is learned which elements of the sequence are most relevant in understanding a certain element.  For example, consider the sentences "The cat drank the milk. It was refreshing."  The words most important in understanding "it" are "refreshing," and "milk." A transformer computes a probability vector over all other words in a prompt, with higher values on words that require attention (because they're relevant), and lower values for words that do not; all words in the prompt get their own attention vector. A word's embedding is then replaced with a linear combination of all the surrounding embeddings, where the coefficients of the linear combination are this probability vector.  So, for each word, a single embedding that encodes not only the word's meaning, but its context in the sentence is computed.  The learned part is this probability vector.

So, the words' embeddings convey meaning, and the attention vectors convey their relationship to each other.  These are good features for language understanding.

Multiple attention nodes are learned at each layer, so that each can learn how to capture different types of relationships.

The best detailed description I've found online is [here](https://towardsdatascience.com/deconstructing-bert-part-2-visualizing-the-inner-workings-of-attention-60a16d86b5c1).
