---
title: Feature Manipulation
---

Last semester, you primarily worked with linear models, where the question of "what can we do with linear combinations of our features" is the core idea.  Of course, if the vector space defined by your features isn't useful, the answer is, "not very much."  This can seem extremely limiting.  For example, consider the following classification problem:

![](percepFeat1.png)

In this example, our features are the x-coordinate, and the y-coordinate.  If we want to do our classification with logistic regression, for example, using the notation from your book last semester, we would need to find the values $\beta_i$ such that the logit $\beta_0+\beta_1 x +\beta_2 y$ allows us to calculate the probability that a point is red.  Because the logit is a linear function on the features given, the point where the probability is .5, or the "decision boundary," will be a line; our linear classifier says everything on one side of that line is probably a red dot, and everything on the other side of that line is a blue dot. (If this doesn't sound familiar, you can read about it again in chapter 4.3 of [the ISL book](https://www.usna.edu/Users/cs/SD312/resources/ISL.pdf)).

**As a minor parenthetical notation note** - statisticians tend to like the notation from your ISL book. I, and many ML people, tend to prefer a more linear algebraic notation. Here, I can organize the linear combination like so:

$$
\begin{bmatrix} x & y & 1 \end{bmatrix} \begin{bmatrix} \beta_1 \\ \beta_2 \\ \beta_0 \end{bmatrix},
$$

then allowing us to organize all datapoints into a single matrix, giving us a single multiplication that gives us the logits of all datapoints:

$$
\begin{bmatrix} x_1 & y_1 & 1 \\ x_2 & y_2 & 1 \\ \vdots & \vdots & \vdots \end{bmatrix} \begin{bmatrix} \beta_1 \\ \beta_2 \\ \beta_0 \end{bmatrix}.
$$
Also, I tend to use $w$, not $\beta$, to refer to that vector of weights.  **End of parenthetical aside**

There is no line that remotely classifies these points.  Logistic Regression will give you one, but it won't be useful or accurate.

However, a very, very, very important idea is that in linear models, you are limited to linear combinations of features, but you can use literally any features you want!  This basic idea makes linear models very powerful.  For example, for this data, suppose rather than using the features $[x,y]$, we instead used the features $[x^2,y^2]$?  That is, suppose we had a dot at $[-1,.5]$.  Well, rather than having its row in the matrix represented with those two numbers, I'll instead use $[-1^2, .5^2]$, or $[1,0.25]$.  If I do this for all points in this set, and plot it on this new $x^2, y^2$ axes, this is what I get:

![](percepFeat2.png)

That data is entirely separable, and we can build a dependable classifier, as shown here.  

![](percepFeat3.png)

The line in this image is the *decision boundary*, such that things on one side are in the black set, and things on the other are in the yellow set.  Of course, it's linear.  If we were to move every point on that line back to the original data set, though, it wouldn't be.  By that, I mean that every point on that line in $(x^2,y^2)$ space, maps to (actually 4) points in the original space: $(\sqrt{x^2},\sqrt{y^2}),(-\sqrt{x^2},\sqrt{y^2}),(\sqrt{x^2},-\sqrt{y^2}),(-\sqrt{x^2},-\sqrt{y^2})$.  That looks like this:

![](percepFeat4.png)

Again, everything on one side of this decision boundary is black, and everything on the other is yellow.  And it's still a linear classifier - but not in the original space!  We've used a linear classifier to make a non-linear decision boundary.  And that's OK!  And normal!  And super, super powerful!

So, we can see that the features chosen heavily impact the behavior of our
linear models; they are, in fact, nearly the whole game.  So what kinds of
funcations might people use to transform their features?

### Domain Expertise

It may be that you know something about your dataset, and you can make up some features that can improve things.  For example, maybe you're trying to predict, from a dataset of information about people, how many hours per week they work.  One of your features may be age.  With a linear predictor, and age as a feature, you can learn things like, "as age increases, hours working also increase."  But, that's probably not true.  People's hours working jump considerably when they leave school, and drop considerably when they retire.  So, it may be that instead of using age as a feature, you instead want to use a binary feature of "are they between the ages of 18 and 65?"

This is known as feature design, and is a main reason why a machine learning expert can't do all this alone when confronted with a new problem (this is a reason why many AI startups fail).  You need somebody in the room who understands this data and can tell you what kinds of things are likely important, so you can turn them into features your model can effectively learn on.

Domain expertise is best.  But, when you don't have domain expertise, you're not totally hosed.  You can instead focus on changing the vector space of your model.  If even after a regularization parameter search, your model sucks, you can focus on widening the span (vector space) of your features, to make it more likely your target vector is close to that span. 

### Dimensionality Reduction

Let's first dispense with the problem of the span of $X$ being *too* expressive.  In this case, we can either add regularization, or we can decrease the expressiveness by using just a few features that capture most of the important information about the data - presumably what's lost is just noise that we don't want to fit anyway.

This is exactly what PCA does for us.  We calculate $\Phi(x_i)$ by projecting $x_i$ onto the first $k$ principal components.  We know these capture most of the important information, and discard the random noise.

Also interesting and truly bananas: [Random projections](https://en.wikipedia.org/wiki/Random_projection). [Random Projections vs PCA](https://stats.stackexchange.com/questions/235632/pca-vs-random-projection).

### Polynomial Features

It may be that your target function isn't linear on your observations.  For example, if your target function looks like $y=x^2$, you're not going to be able to match that very well with a linear function on $x$.  As a result, it's common to try features that consist of monomials constructed from your observations.  For example, if you've observed $[x~y]$, then maybe you want to try $[x^2~y^2~xy~x~y~1]$.  This can add a lot of useful expressiveness.  As stated in your reading, you don't want to take this to too high of a degree, or your function can get unplausibly weirdly shaped.

### Radial Basis Functions (RBFs)

It may be that similarity to certain locations in the input space is a useful feature (over here, it's high; over there, it's low, etc.).  The idea here is to choose $k$ significant locations in the original observation space, and then $\phi_i(x)$ is the distance between $x$ and the $i$th significant location.  "Distance," as usual, can mean a lot of things - most common is Euclidean distance, or the Gaussian distance ($e^{-(\epsilon ||x-x_c||)^2}$, where $x_c$ is the significant location, and $\epsilon$ is a chosen width parameter that determines how far away a point can be before its Gaussian similarity is essentially zero.

These significant locations can be chosen either intentionally based on domain knowledge, or evenly spaced through the domain, or at sampled points.

# [Code from today's lecture](showFeatures.html)
