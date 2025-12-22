---
title: Hoeffding Inequality
---

A core assumption in machine learning is "if it works on the data I've seen, it will probably work on data I haven't seen."  This is a BIG assumption!  And, of course, machine learning gets things wrong all the time, so it's obviously not ironclad.  Is there a reason we can believe this might be true sometimes? Or at least enough to believe we're not all wasting our time?

To understand one approach to this assumption, we turn to probability.  Suppose we have a large urn full of many, many red and blue balls.  We would like to understand what proportion of the balls are red (call this unknown proportion $\mu$), but the urn is far too large to count them all.  (*Note: you can replace this scenario with one of many real-world scenarios. What proportion of midshipmen at the Academy have covid? How many Iowans favor a specific political candidate?*)  All we can do is look at a sampling of the balls, and then make general conclusions from our sampling.

Suppose, for instance, we drew ten balls from the urn, and observed that seven of them were red, and three of them were blue. So, the percentage red in the sampling (which we'll call $\nu$) is 70%. You would likely feel comfortable saying that evidence suggests ~70% of the balls are therefore red, or that $\nu$ is close to $\mu$. But, isn't it possible that you pulled the only seven red balls from the urn, and so $\nu$ is not representative at all?  It absolutely is. It's possible our conclusions are very wrong. But, it's unlikely.  We are going to hang our machine learning generalization assumption on that probability.

---

### Probability exercise

Let's pause here to consider the unlikelihood of $\mu$ and $\nu$ being very different with an example.  Suppose $\mu$ (the true percentage of red balls) was .7.  What is the likelihood of pulling ten balls and getting a $\nu$ of .1 or less?

We can do this with the binomial distribution, which I'm sure you've seen from your probability and statistics course.  Define $N$ to be the number of balls drawn and $x$ to be the number of red balls drawn.  The binomial distribution is:

$$
p(x)={n \choose x}\mu^x(1-\mu)^{n-x}
$$

In this case, the probability of drawing 1 or 0 red balls is

$$
\begin{aligned}
p(\nu\leq.1)=&p(0)+p(1)\\
=&{10 \choose 0}.7^0(1-.7)^{10-0}+{10 \choose 1}.7^1(1-.7)^{10-1}\\
=&5.9\times10^{-6}+1.3\times10^{-4}.
\end{aligned}
$$

This is a nonzero (ie, technically possible) but very very small probability!  We can feel comortable that if we draw 1 or 0 red balls out of ten, there are almost certainly not 70% red balls.

---

We can quantify this relationship between $\mu$ and $\nu$ with the Hoeffding inequality.  The Hoeffding inequality states that for a random sample of size $N$, we can give an upper bound on the probability of drawing a proportion $\nu$ which differs from the true proportion $\mu$ by more than some number $\epsilon$: $P[\left|\nu-\mu\right|\gt\epsilon]\leq2e^{-2\epsilon^2N}$.

An important takeaway from this is that as your sample size $N$ increases, the likelihood of $\mu$ and $\nu$ being meaningfully different shrinks.  That makes sense!  And, the smaller you want $\epsilon$ to be (ie, the more accurate you want your sample to be), the larger $N$ needs to be in order to obtain that accuracy.

This bound is used to justify all sorts of conclusions from sampling. As mentioned above, political polling is a good example.  Of course, sometimes polls are wrong! It's worth noting that the assumption underlying the Hoeffding inequality is that the $N$ samples are truly random, which in practice can be hard to achieve.  Perhaps, for instance, you're polling by phone, and certain kinds of people are more likely to answer the phone ([this, by the way, is true](https://www.pbs.org/publiceditor/blogs/pbs-public-editor/the-problem-with-polls/)). In that case, the Hoeffding inequality does not apply, and you can be wrong in all sorts of meaningful and deceptive ways.

Fine!  What does this have to do with machine learning?  Well, suppose each ball in the urn represents a data point for your ML classification agent, where red balls are examples your model gets correct, and blue balls are examples your model gets incorrect.  Now, perhaps you see the analogy!  In our random samples (the training set), we're getting some percentage $\nu$ correct.  It seems, the Hoeffding inequality assures us that there will be a similar percentage of red balls in the rest of the urn (ie, $\mu$, or the test set). We can expect similar performance!

...only it's not that easy.  This would be true for an arbitrary, random ML model with random parameters.  But, we don't have an arbitrary, random ML model with random parameters, we have a model that has been chosen specifically because it does well on the training set - that is, it is chosen specifically because it makes training set balls red. Obviously, that skews the underlying assumptions that make the Hoeffding inequality valid.

So the question is no longer what is the probability a random model behaves differently on the training and testing sets, but instead, what is the likelihood that we can find a version of an ML model that performs differently on the training set than on the testing set (for example, if we've decided to use a logistic regressor, we can consider each possible setting of the parameters to be a different "version" that we are selecting from a set of all possible logistic regressors)? This probability is much higher.

We can add this to our inequality by considering a case where we have $M$ possible versions of our model, and ask what is the probability that at least one of them violates our "$\nu$ and $\mu$ may not differ by more than $\epsilon$" restriction.  Well, it's the probability that the first one does, plus the probability that the second one does, plus the probability that the third one does, and so on, until we get to:

$$
p(\left|\textrm{training error}-\textrm{testing error}\right|>\epsilon)\leq 2M\epsilon^{-2\epsilon^2N}.
$$

This bound is a very loose bound, and using it to create actual numbers is silly, since $M$ is nearly always large enough to get a right hand side larger than 1 (which, there are easier ways to show that a probability is less than 1).  And, in fact, $M$ is nearly always infinite, making it truly silly.

However, it does provide useful and true intuition.  As $N$ increases, the probability of overfitting drops.  As $M$, the complexity of the model, increases, the probability of overfitting increases.  In other words, no, the assumption that training and testing sets will behave similarly is a bad one, unless $N$ is large enough, or the model is not very complex.  These are useful guidelines and intuitions!  If our model is overfitting, we need either more data, or a more simple model (by either removing parameters or increasing regularization).

*Aside*: There are bounds on the amount of overfitting that are tighter and more usable than the Hoeffding inequality.  The concept of $M$ is replaced with a measure of the complexity of the model called the model's VC dimension.  We have chosen not to dive into these complexities because after considerably more work, the intuition comes out the same.
