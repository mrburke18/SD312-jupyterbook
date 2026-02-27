# Transfer Learning

Convolutional networks (and other kinds of feature extractors) tend to work far better when very, very deep. This causes problems because in any standard problem, you don't have enough data to train a very, very deep network without extreme overfitting (if you can even afford the compute to do so!). So, it *seems* that the actual applicability of convolutional networks and other feature extractors is limited.

In practice, we rarely train these things from scratch ourselves. Instead, we
allow a big research shop like someone in academia or Google to train a
network on a similar problem (with sufficient data) which will likely create
similar features to what we want. We can then carve off the feature extraction
portion (the "backbone") and use it for our own purposes.

## Strategies: Freezing vs. Fine-Tuning

A pre-trained network consists of a feature extraction portion followed by a dense classification head. When adapting this to a new task, we have two primary mechanical choices:

* **Freezing:** The weights of the pre-trained layers are kept constant ($w_{frozen}$). Only the weights of the new, untrained dense layer are updated during backpropagation.
* **Fine-Tuning:** After the new head has been partially trained, we unfreeze some or all of the feature extraction layers and continue training with a very low learning rate to subtly adjust the features for the specific target domain.

The choice between freezing and fine-tuning is dictated by the relationship between the source data and the target data.

| Dataset Size | Similarity to Source | Recommended Strategy |
| --- | --- | --- |
| **Small** | **High** | Freeze the backbone; train only the new head to prevent overfitting. |
| **Small** | **Low** | Difficult; freeze only the earliest layers and hope for general feature overlap. |
| **Large** | **High** | Fine-tune the entire network to achieve maximum precision. |
| **Large** | **Low** | You may opt to train from scratch since data is sufficient and features differ. |

When fine-tuning, you run the risk of "catastrophic forgetting," where the
features become overfit to your new task, destroying their original abilities.
Fine-tuning with a smaller learning rate in the backbone than the learning
rate in the head is therefore common to mitigate this.

## The Model Zoo

Rather than designing architectures, practitioners select from a "Model Zoo" of proven structures.

**ResNet**

ResNet is often the default choice for general-purpose transfer learning.
Calculation of the gradient of a weight early in a deep network can get
unmoored from the signal from the loss function; skip connections help resist
this, making a smooth, well-behaved loss surface for fine-tuning. It is best
for high-performance applications where maximum depth is required, or where
training stability is a priority.

**Inception**

Inception backbones are designed for computational efficiency and capturing
spatial information at varying scales simultaneously. They use multiple filter
sizes $(1\times 1, 3\times 3, 5\times 5)$ at the same level to capture features
at different scales. Inception backbones achieve comparable accuracy to
ResNet, with significantly fewer parameters. Particularly effective for
datasets where the objects of interest vary significantly in size relative to
the frame.

**MobileNet**

MobileNet is optimized for speed and efficiency on devices with limited
computational power. Not as accurate, but much faster and smaller.


## Self-Supervised Learning (SSL)

While standard transfer learning relies on **Supervised Learning** (using
labeled data like ImageNet), **Self-Supervised Learning** allows a model to
learn features from huge amounts of unlabeled data.

The model solves "puzzles," such as predicting the next word in a sentence or identifying the rotation of an image. This creates a massive "foundation model" that can then be transferred to specific tasks where labels are scarce.

## Risks and Limitations

* **Negative Transfer:** If the source domain is too different from the target (e.g., transferring a model trained on natural landscapes to medical X-rays), the pre-trained weights may provide a worse starting point than random initialization.
* **Computational Constraints:** Even if training time is shortened, the resulting models are often very large and may exceed the memory limits of the target hardware.
* **Bias Inheritance:** Models inherit the biases present in the massive datasets used by the original "research shops."
