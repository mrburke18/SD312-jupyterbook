---
title: Deep Q-Learning
---

We're going to use Deep Q-Learning to learn to perform the [Cart Pole task](https://gymnasium.farama.org/environments/classic_control/cart_pole/), a venerable RL environment with a continuous state space and a discrete action space.

You will want access to [the paper](https://arxiv.org/pdf/1312.5602.pdf), and especially to Algorithm 1.

We will need to use our lab machines local GPUs to train our network.  [Here's your notebook](12Deep_cartpole.ipynb).  RL is a bit twitchy - once you get a reasonable implementation that is learning something, you will probably want to do several runs, with several different hyperparameter settings, to keep your best version.
