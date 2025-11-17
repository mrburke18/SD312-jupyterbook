# Neural Network Regression

Using your young-adult-migration dataset from the previous project, you'll do regression on the same inputs using a neural network, rather than linear regression.  Of course, you'll want to experiment with different depths, widths, learning rates, and activation functions.  Because you're doing regression, you shouldn't have an activation function on your final layer at all, making it just a linear combination of the features the previous layers have calculated.  How close can you get your test set?  Does it behave better than the linear regression did?

You'll be doing this on the GPUs on the machines in the lab.  SSH into a lab machine that nobody is using.  Write down its hostname somewhere so you can find it later.  Make yourself a new conda environment for gpu things.

- `mamba create -n gpu numpy scipy matplotlib plotly scikit-learn jupyter`
- `mamba activate gpu`
- `pip3 install torch torchvision`

If you then start the python interpreter, and run:

```python
import torch
print(torch.cuda.device_count())
```

it should print out a 1, indicating it is aware of 1 GPU.

After that, do the project, and build the best predictor you can.  Does it
outperform your linear regression project?

Put your code in your normal, backed-up directory.  Put your data in
`/SI470/youralpha`, which is stored *on the machine itself*.  This directory is not backed up, and is not accessible from any other machine, but is accessible from *that* machine much quicker.

## Analysis

Once you have your best predictor, you naturally want to know which of your inputs are the most important.  Unlike with our linear models, we can't easily analyze the coefficients to know which are being used the most heavily.  But, we can do an *ablation test*.  In an ablation test, we remove an input, then re-train.  If the model gets substantially worse, then that input is probably pretty important for your prediction!
