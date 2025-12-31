---
title: Our first neural nets
---

Neural nets are doing many, many, many parallelizable operations that are best done on many small processing units in parallel.  GPUs, which are the computing hardware that traditionally use linear algebra to render graphics, and which monitors are plugged into, fit the bill perfectly.  Neural nets can run on CPUs, but have a training speedup of dozens of times when run on GPUs instead.  Depending on the scope of our projects, we're going to be using GPUs in two places.

First, your lab machine has a small GPU which is local and can be accessed in a straightforward way.  Take a note of the name of the machine you're sitting at now.  Write it down somewhere.  You might want from time to time to ssh into this machine in order to train a neural net.

Second, we'll be paying to use some of Amazon's.  This infrastructure will be handy later, but first we'll just be getting comfortable with neural nets locally, rather than adding on the new cloud computing infrastructure at the same time.

**Make yourself a new mamba virtual environment** for pytorch:

`mamba create -n gpu numpy scipy scikit-learn plotly matplotlib pandas jupyter pytorch torchvision torchaudio pytorch-cuda=12.1 -c pytorch -c nvidia`

This will create an environment called `gpu` that contains all those packages - including pytorch.  From now on, when doing GPU things, first run `mamba activate gpu` to get into that virtual environment, and only then run commands like `jupyter lab`.

So do that, then download [this notebook](06UniversalApprox.ipynb) to get started.

Submit this as `06UniversalApprox`.

**What you should know after doing this lab (aside from the coding part)**

- How to set up a regression problem using a neural net.
- How to set up a multiple regression problem using a neural net.
- A neural net regressor can be interprested as a feature generator followed by a linear regressor.
- What loss functions are appropriate for regression.
- How a neural net is trained.
