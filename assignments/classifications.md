#Przewidywanie Polskich Bankructw (Predicting Polish Bankruptcies)

I have added a dataset to the si486l repository called "polishBankruptcy,"
which contains financial information about a large number of Polish companies,
and whether or not they have gone into bankruptcy in a 5-year period.  I'd
like you to build predictors of bankruptcy for this dataset.

[The dataset is explained
here](https://archive.ics.uci.edu/ml/datasets/Polish+companies+bankruptcy+data).
~~It is given to you in .arff form, which is the data format for
[Weka](https://www.cs.waikato.ac.nz/ml/weka/).  Fortunately, [scipy can also
read arff
files](https://docs.scipy.org/doc/scipy/reference/generated/scipy.io.arff.loadarff.html).~~ **Edit:** The data is presented as an .h5 file called training.h5.  The first column is the number 1-5 detailing which file the line is from.  The last column is the classification.

The dataset has the occasional piece of missing data.  Probably, you should
fill those in with something sensible (maybe with the mean for that feature?
maybe using matrix completion?).  ~~You should combine all five files into
one dataset, with the year as an additional feature.~~

You'll build your best possible predictor both with logistic regression, and
with a support vector machine.

You'll turn in a PDF report and code.

Your PDF should include confusion matrices, and information to explain what
choices you made, and what worked, and what didn't.

An A project does a good job of at least two of the following:

- Use Low-Rank Matrix Completion to fill in the missing data.  Justify your choice of number of principal components in your report.
- Considerable exploration of feature sets (PCA? polynomial terms? RBFs?
  Something else?) and kernel choices.
- Uses HPC techniques to speed up the process of trying many hyperparameters
  like regularization parameters/feature sets/kernel choices/cross-validation.
- Principled adjustments to class_weight, to overcome the uneven class sizes,
  or emphasize accurate prediction in one class or the other.

**Note:** there's a lot of sklearn functions that might be helpful to you aside from the ones we've already seen.

- [Imputer](https://scikit-learn.org/stable/modules/impute.html#impute): Useful for filling in missing data with simple statistics like the mean or median.
- [preprocessing](https://scikit-learn.org/stable/modules/classes.html#module-sklearn.preprocessing): A really useful set of classes that will standardize or normalize your features, or build a different feature set from your observations.
- [Pipeline](https://scikit-learn.org/stable/modules/classes.html#module-sklearn.pipeline): Useful for combining all these things together into one estimator (for example, calculate polynomial features, then normalize them, then fit Logistic Regression).

Submit as `bankruptcy`.

###Competition

I have withheld 4000 lines, evenly distributed from throughout the dataset, which are not missing any data.  Your best model will be tested against this validation dataset, and the group with the highest accuracy wins extra credit.

To submit a best solution, you should have a file called `myBest.py`, with a function called `predict`.  It should be organized as follows:

```python
#import statements

'''
predict should take in a 4000x65 numpy matrix.  This matrix will include all 
information from the 4000 chosen lines, untouched, minus the final column of 
labels.  It should return a numpy array of size (4000,) of all ones and zeros, 
of your model's prediction.
'''
def predict(data):
  #your code, resulting in a (4000,) numpy array called predictions
  predictions=np.random.randint(0,2,size=(4000,)) #probably don't do this

  #include the following tests to make sure what you're about to return
  #is the proper size and type
  assert predictions.shape==(4000,)
  assert predictions.dtype==int
  return predictions

if __name__=="__main__":
  #ALL OTHER CODE GOES IN THIS BLOCK
```

My testing code looks like this:

```python
import numpy as np
import h5py
import sklearn
import sklearn.metrics
from myBest import predict #importing your function!

with h5py.File('validation.h5') as f:
  data=f['data'][:,:-1] #Data is everything but the last column
  labels=f['data'][:,-1] #labels are the last column

data,labels=sklearn.utils.shuffle(data,labels)
labels=np.round(labels).astype(int) #make them integers
predictions=predict(data)
print(sklearn.metrics.accuracy_score(labels,predictions))
```

Your function can assume whatever files you submit are in the same directory as the running code.  [You can see documentation on storing and loading trained sklearn models here](https://scikit-learn.org/stable/modules/model_persistence.html).  Probably, your function will load a trained model, call .predict(data) on the new data, and return the result.
