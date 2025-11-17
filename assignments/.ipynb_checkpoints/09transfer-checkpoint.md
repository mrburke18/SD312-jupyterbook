# Transfer Learning

Most image recognition tasks don't have enough data to adequately train a full-sized convolutional neural network.  As a result, it's common to instead to *transfer learning*.  In transfer learning, we first train a large neural net on a very large dataset we do have (or, more likely, we let someone else do it for us).  Presumably, those convolutional layers will then be able to extract useful features for all sorts of image tasks, not just the ones they were specifically trained for.

We then take that large, trained neural net, chop off the fully-connected part at the end, replace it with a randomly-initialized new fully-connected part, and then train on our smaller dataset, only allowing those new layers to train.  Given the good features from the convolutional layers, we can hopefully build a good network for our specific task.

You're going to build a neural net which performs classification between two types of things of your choice using transfer learning.  To do this, we're going to scrape Bing Images (yes! Bing!) for our dataset of images.

## Step 0: Set up your environment

Make a new virtual environment for this project.

- `mamba create -n transfer numpy scipy scikit-learn pandas plotly matplotlib jupyter pytorch torchvision opencv imutils tqdm torchinfo`
- `mamba activate transfer`
- `pip install standard-imghdr`
- `mkdir imgs && cd imgs`
- `pip install git+https://github.com/ostrolucky/Bulk-Bing-Image-downloader`
- `cp ~/.local/bin/bbid* .`

If that last command doesn't work, try `cp ~/mambaforge/bin/bbid* .` instead.

Then, in order to get around ITSD's nonsense, disable SSL verification by
opening up `bbid.py`, and just below all the import statements, add:

```python
import ssl
_create_unverified_https_context = ssl._create_unverified_context
ssl._create_default_https_context = _create_unverified_https_context
```

## Step 1: Build a dataset

You can download images of whatever you like to build your classifier.  Inside `~/imgs` is a file called `bbid.py`.  If you run `python bbid.py goats`, it will download a bunch of pictures of goats into `imgs/bing`.  You can then use [this script](mvr.sh) as `bash mvr.sh goats` to move most of them into `imgs/train/goats`, and the rest into `imgs/test/goats`.

You'll want to do this for at least two types of things, of your choice, to build a classifier between.

### Step 2: Train a neural net, based off the ResNet18 architecture

[Here's some code](transfer.notPY).  UNDERSTAND IT.  Run it on your data.  It will probably work pretty well.  Then, look for things to modify.  Depth?  Width?  Dropout layers (google it!)? Activation functions?  More classes of images? Number of epochs?

Here are some questions to explore:

- How does adding more classes impact the performance of your learned model? Are some classes harder to differentiate from each other than others (confusion matrix)?
- How does adding more layers impact the speed of convergence and the ultimate performance of the model?
- Can you find some classes that you are unable to learn particularly well?
- Does changing the learning rate have any effect?
- If you remove the random transformations to the training set, or add others, how does test performance change?  Does it take longer to overfit?
