---
title: Policy Networks
---

So far, we've gone from small numbers of states and small numbers of actions (Tabular Q-learning), to large numbers of states, and small numbers of actions (Deep Q-Learning).  Today, in the brief time we have left, we'll have a very quick introduction to how we can fix some of the problems that come from Deep Q-Learning, while handling large numbers of states *and* large numbers of actions.

In Q-functions, the "max" operator that comes into play in choosing an action causes a lot of problems.  If we have two almost-equally-good actions, always choosing one can cause problems.  For example, suppose we're in a cartpole state where the stick is nearly upright.  We don't care much if we take our cart left or right - but we probably would do better randomly switching between the two, rather than having a bias toward letting it fall in a certain direction.  The max operator can cause this type of long-term problem, and also causes policies to be erratic during training.

We're instead going to build a system that allows for *stochastic* policies - that is, we'll take each action with some probability.  In cases where the choice is clear-cut, we can still push that probability strongly towards the favored action.  Where it's not, we can allow for some probability density on each of the about-as-good-as-each-other choices.

The networks we've build for Deep Q-Learning are often called *value networks* - it's a good name, because their output is an approximation to the value.  To handle large numbers of actions, we're instead going to build a *policy network* - this is also a good name, because the network will directly output a policy.

Let's first think about a policy network for small numbers of actions, and then we'll tweak it to allow large numbers of actions.

Suppose we have an MDP with three actions.  Our policy network would take in a state, and have four output nodes.  Three of those nodes output logits for the three actions, allowing you to compute with what probability the policy believes you should take that action; denote the probability of taking action $a$ $\pi(a|s)$.  The fourth outputs a value for that input state - that is, what it believes the expected return will be if you follow the policy it's laying out for you.  Call the output from that node $\hat V(s)$.

When exploring, we choose an action randomly from the distribution prescribed by the network.  This gives us an $(s,a,r,s')$ sample.  We can use the output of the value node after doing a forward pass with $s'$ to compute $r+\gamma \hat V(s')$.  Naturally, we can now train our value node to be a bit more accurate with the Bellman error: $BE(s,a) = (\hat V(s) - (r+\gamma \hat V(s')))^2$.

Now, suppose we have two actions that are currently equally weighted by our policy for some state.  One action tends to overperform expectations - that is, the actual received value tends to be higher than $\hat V(s)$.  The other underperforms expectations.  Naturally, we'd like to adjust our distribution so that the first action happens more often, and the second happens less often. We can quantify this over- or under-performance with something called *advantage*.  We compare what actually happened $(r+\gamma \hat V(s'))$ to what we expected to have happen ($\hat V(s)$), and see if we were pleasantly or unpleasantly surprised: $A(s,a) = r+\gamma \hat V(s') - \hat V(s)$.  Note unlike Bellman error, this is signed - that is, we prefer the advantage to be as large as possible, not that the two elements be close.

Now, if $A(s,a)$ is large, we'd like to increase $\pi(a|s)$ (similarly, if $A(s,a)$ is negative, we'd like to decrease $\pi(a|s)$). So, we can think of this as maximizing $A(s,a)\pi(a|s)$, or, because maximizing $x$ and maximizing $\log(x)$ is the same thing, we can maximize $A(s,a)\log(pi(a|s))$, or minimize $-A(s,a)\log(pi(a|s))$.  This latter choice is preferred for a few reasons, one of which is that the log of the probability is just the logit, which is the actual value we're outputting anyway.

This makes our total loss function for a given $(s,a,r,s')$ to have two portions: $(r+\gamma \hat V(s')-\hat V(s))^2 - A(s,a)\log(\pi(a|s))$.  Minimize that, and you're simultaneously making your prediction of $\hat V(s)$ more accurate, and changing the output probability distribution to prefer actions that perform well.

This procedure already greatly outperformed Deep Q Learning, even as it still only works on finite action spaces.

To make this work on infinite action spaces, (here's where Taylor stopped, because we're not going to teach it anyway)
