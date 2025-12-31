---
title: Transfer Learning
---

Today we're going to investigate transfer learning.  We're going to leverage a pretrained ResNet-18 network to build us some features to solve arbitrary small-data image classification problems.

### Creating a dataset

The first thing you need to do is create a dataset.  Perhaps, for instance, you want to start by looking into how well you can accomplish binary classification, for instance latest MIG vs FA-18 (or DDGs Luyang III and Type 055 Renhai-class Cruiser or DDG type I, II  or III)? To do this,

- download [this tarball](scraper.tgz) and move it into an appropriate place, 
- [run `tar xzf scraper.tgz`](https://xkcd.com/1168/),
- this will create a few files, one of which is `scraper.sh`.  Make it executable by running `chmod +x scraper.sh`
- run `./scraper.sh MIG<latest num>` and `./scraper.sh FA-18`. You may want to add other names for the same plane to get more pictures later.
- You'll notice that this creates two new folders, called `train` and `test`.  Explore those folders a little bit, so you understand what's been built.
- Start up your jupyter lab, making sure the notebook is in the same directory as your dataset folders.  Change `dataset_path` to include your dataset Location. 

### Training your classifier

Of course, when we perform transfer learning, we use some foundational model trained on some other, related task with a large dataset.  In this case, we'll use the ResNet18 model, which has been trained on the ImageNet dataset.

[Here's your notebook](transfer.ipynb) to get you started.


**What you should know after doing this lab (aside from the coding part)**

- When would you use transfer learning instead of training a full system from scratch?
- Which parts are typically kept, and which parts are typically replaced with an untrained replacement?
- You should be able to reason about how to modify a trained network to apply it to a new task.
- Under what circumstances is transfer learning an appropriate approach?
