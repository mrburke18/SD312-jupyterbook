---
title: Voting predictions
---

OK, so now you've built some neural nets!  Now it's time to do some classification.  We have a dataset which contains a wide variety of health and demographic data about each county in the US, along with how that county voted in 2020, across four candidates: Biden, Trump, Jorgensen, and Other.

[Here is a notebook which gets you started](07NNClassification.ipynb).

Once you're done, `File->Download` the .ipynb file, and submit as `07NNClassification`.

**What you should know after doing this lab (aside from the coding part)**

- How to set up the output layer of a classification problem.
- That a classification network outputs logits.
- How to compute probabilities from logits.
- That Cross Entropy Loss is usually used for multi-class classification problems.
- That classification is a special case of predicting a probability distribution, where one class is 100% and the others are 0%.
