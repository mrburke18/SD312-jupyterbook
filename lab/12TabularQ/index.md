---
title: Tabular Q-Learning
---

In this lab, we're going to be implementing Tabular Q-Learning to solve some simple RL tasks.  We will NOT need a GPU for this lab, and so we don't need to use AWS.  Instead, we'll go back to running a notebook on `ssh.cs.usna.edu`, like we did at the beginning of this class.

We'll be using a library called Gymnasium, which is a collection of RL problems.  SSH into `ssh.cs.usna.edu`, and make yourself a new conda/mamba environment, which has:

- numpy
- scikit-learn
- plotly
- jupyter

After you've done that, and activated it, run `pip install gymnasium gymnasium[toy_text] gymnasium[classic_control]`

You'll want to familiarize yourself with some of the Gymnasium documentation.

- [Basic Usage](https://gymnasium.farama.org/introduction/basic_usage/) (Read
  through "Explaining the Code")
- [Frozen
  Lake](https://gymnasium.farama.org/environments/toy_text/frozen_lake/): This
is the simple RL problem we will start with.

Now you're ready for [your notebook](12TabularQ.ipynb).

**Generative AI**

You may use Generative AI on this lab to answer short, easy questions (for
example, "Using numpy, how do I get the maximum value of a matrix?").  You may
not use it to write large block of text ("Implement Q-Learning on the frozen
lake gymnasium environment").
