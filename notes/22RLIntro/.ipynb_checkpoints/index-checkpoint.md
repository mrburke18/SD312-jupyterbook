---
title: Intro to RL
---

Another Machine Learning approach that has been and is continuing to be explored and leveraged is *Reinforcement Learning*.  In this paradigm, researchers are investigating how to get a model to perform a particular task - for example, given its understanding of the world, how should an autonomous vehicle respond with its wheel and accelerator in this moment?  There's no "right" answer that we can query at any given timestep; we only know if it's right later, when you either get into a car accident, or you're safely delivered to Chipotle.

Perhaps the most difficult part of RL is in mathematically defining what "good behavior" is from your autonomous system. What does it mean for one robot to "walk better" from point A to B?  Certainly, it avoids collisions, but is faster better?  Smoother, so as to not jostle payloads?  Most energy efficient? Some combination of the above?

### MDPs and Value

To help us do this, we create a mathematical structure called a *Markov decision process*, or MDP.  An MDP is defined by the following things:

- A *state space* $S$. A state is a complete description of the agent's current scenario (we call the autonomous thing the agent).  The state space is the set of all possible states.  This might be small and discrete, or large, multi-dimensional, and continuous.
- An *action space* $A$. At each timestep, the agent must choose an action to perform. The set of all possible actions is the action space.  Again, this might be small and discrete (to play Pong, you can go up, down, or stay where you are), or multidimensional and continuous (to walk a robot, we have to set actuator values for every joint in the robot's leg, each of which is a continuous value).
- *Transition probabilities* $P(s'|s,a)$. This is physics, or the rules of the game, which expresses how agents move through the space. $P(s' | s,a)$ is the probability of ending up at state $s'$ given that the agent was in state $s$ and took action $a$.
- The *reward function* $R(s)$. In order to communicate success to the model, we give every state a reward.  For example, a state where the agent has achieved its task might get a reward of 10, while a state where the agent has fallen off a cliff might get a reward of -100.
- The *discount value* $\gamma$ (that's the Greek letter gamma). In general, we prefer to get reward sooner than later.  The discount value is a number between 0 and 1 which quantifies this - values close to 0 express more impatience, and values close to 1 indicate more patience.

Our agent interacts with this MDP by observing its state, then choosing an action, and observing the next state and the reward of that next step.  It performs this loop over and over again until the interaction ends.

Our goal is to develop a *policy* $\pi$, which is a function that takes in a state and returns an action.  A good policy is one that chooses actions for each state, and ultimately achieves the task.  We quantify this as wanting to maximize experienced, discounted rewards; that is, if we call $R(s_t)$ the reward of the state experienced at state $t$, we want to maximize $\sum_t \gamma^t R(s_t)$.  This sum is known as the *value* of state $s_0$, which depends upon the state, and the policy which determines which following states are visited.

Consider, for example, this simple MDP.  There are 4 states (denoted $s0$, $s1$, etc.), each represented by a circle.  The reward of that state is represented by the value in the circle.  The action space at each state is to go either left or right.  We would like to identify a policy that results in a high value.  Suppose $\gamma=.9$.

![](mdp.png)

We can start by calculating the value, for each state, of always going left. If we start at $s0$, we receive a reward of 0, and then continually, forever, ending our transition at state $s0$, continually receiving a reward of 0, which is scaled by being multiplied by 0: $0+\gamma 0+\gamma^2 0+\gamma^3 0+\cdots$.  So, our value for state $s0$, with a policy of always going left, is 0.

From $s1$, we receive a reward of 1, followed by an infinite sum of 0s.  The value of state $s1$, under a policy of always going left, is 1.  It makes sense that $s1$'s value under this policy is higher than that of state $s0$.  Were this our policy, we would definitely prefer to get one reward than none at all, so the value is higher.

From $s2$, we receive a reward of 0, followed by a 1, followed by an infinite sum of 0s. The value of state $s2$ is $0 + \gamma 1 + \gamma^2 0 + \gamma ^3 0 + \cdots = .9$ (because $\gamma=.9$).  Again, this makes sense.  State $s2$ is preferable to state $s0$, but less preferred than state $s1$ (because in state $s1$ we get the reward faster).  So, it's value is higher than that of state $s0$ and lower than that of state $s1$.

The value of state $s3$ is .81 (see why?).  So, the values of all four are [0, 1, .9, .81].

<img src="leftValue.png" width="1000"/>

Now suppose our policy is to always go right.  We again calculate our values, and get [.9, 1, 0, 0]. We can plot these against each other.

<img src="leftRightValue.png" width="1000"/>

So which policy is better?  Well, our evidence so far is that it seems that going right is better in state $s0$, that left is better in states $s2$ and $s3$, and that it doesn't matter in state $s1$.  So, we can use *value* to compare the performance of two different policies, and possibly even update them: let's use this evidence and design a policy where we go right at state $s0$ and $s1$, and left at states $s2$ and $s3$.

This makes the infinite sum in the value a little more complex, in that rather than ending on this mathematically convenient infinite sum of 0s, we're going to infinitely end up bouncing back and forth between states $s1$ and $s2$.  We can turn to our study of infinite sums from Calculus class to calculate these.  It turns out these values are about [4.7, 5.3, 4.7, and 4.3].

It turns out for this MDP, this is the best possible policy, which makes the values as high as possible for every state.  We call this the *optimal* policy.

<img src="optimalValue.png" width="1000"/>

So, once we calculated value of a policy, we could use this in two ways.  One, it gives us an idea of which states are better to be in than others.  For example, $s2$ and $s3$ both have a reward of 0.  However, the value under our optimal policy of being in state $s2$ is higher than in $s3$.  So, we know that *something* is advantageous about being in state $s2$ than in $s3$. You can see how this can help us build better and better policies (get to $s2$, rather than $s3$).

Second, it gave us the ability to compare policies, decide which were better for which states, and then modify those policies to improve them.

This is great! However, in a more complex environment, we may not know the reward function or understand the effects of taking our actions (we have action 1 and action 2, they're not labeled "left" or "right," and in fact, may do something different at each state).  So, we need to do some learning of this system's behavior by exploring it - this is where the data and ML comes into play. To get us there, we need to expand our definition of "value" a bit further.

### Q-Functions

Given only these inputs, our goal at the end of this is to have a way of knowing what is a good action to take in each state.  One way of doing this is to expand the idea of value (where each state has a single value for a single policy) to *Q-functions*, where each state-action pair has a value calculated (under the current policy, if you go *left* here, you expect *this* value; however, if you go *right* here, you expect *that* value).  We usually denote this in function format as $Q(s,a)$. Note: It is important to remember here that this is the Q value under a particular policy.

For example, let's again consider our simple chain MDP, with a policy of "always go left."  Let's temporarily assume we have access to $R$ and the effects of our actions, and compute the *correct* values of these Q-functions, before discussing what this gives us, and then how we can approximate these Q-functions from our agent's samples.

In state $s0$, we need to compute two Q-functions - $Q(s0,left)$ and $Q(s0,right)$.  If we go left, and then follow the policy "always go left," then we'll only receive a reward of 0 forever, so $Q(s0,left)=0$.  If we go right, and then follow the policy, then we'll receive a reward of 0 from being in state $s0$, followed by $\gamma 1$ from state $s1$, followed by a reward of 0 forever as we go left forevermore.  So, $Q(s0,right)$ is .9.

In state $s1$, we need to compute $Q(s1,left)$ and $Q(s1,right)$.  $Q(s1,left)=1$, and $Q(s1,right)=1+\gamma 0+\gamma^2 1 + 0 + \cdots=1.81$.

The full table for the **always left policy** looks like this:

|    | Left | Right |
| -- | ---- | ----- |
| s0 | 0    | 0.9   |
| s1 | 1    | 1.81  |
| s2 | .9   | .73   |
| s3 | .81  | .73   |

The table for the optimal policy is:

|    | Left | Right |
| -- | ---- | ----- |
| s0 | 4.26 | 4.74  |
| s1 | 5.26 | 5.26  |
| s2 | 4.74 | 3.84  |
| s3 | 4.26 | 3.84  |

If we have this, it's super easy to know our policy - clearly at state $s0$, we should go right - we expect more value!  In fact, always, we should choose the action that has the largest value at our current state: $\pi(s) = \argmax_a Q(s,a)$.  Making that change would result in increasing values elsewhere in the table due to smarter decisions later down the line, but (if the MDP is small enough, and we know $R$, and we know $P$) we could recompute this whole table every time we decide to change our policy at any state.

### Bellman equation and Bellman error

First, an observation.  For the optimal policy $\pi^*$,

$$
\begin{equation*}
Q_{\pi^*}(s,a) = \mathbb{E}_{P(s'|s,a)}\left[ r + \gamma \max_{a'}Q_{\pi^*}(s',a')\right].
\end{equation*}
$$

That equation is known as the *Bellman equation*, and is not so ugly as it looks.  First, the $\mathbb{E}_{P(s'|s,a)}$ refers to the expectation.  That is, if our MDP is not deterministic, then taking action $a$ from action $s$ does not always have the same effect - there's a little bit of randomness in the world, so we can't predict exactly what will happen.  That expectation notation just says, "on average, where state $s'$ is drawn from the probability distribution of places that we might end up in after taking $a$ from $s$.

Second, in an optimal policy $\pi^*$, we naturally assume we are going to take the action at state $s'$ which gives us the highest value.  So, that's the only part we care about, giving us the max term over all actions available in state $s'$.

All this is to say, that when we collect a sample $(s,a,r,s')$, and refer to our table for our approximations of $Q(s,a)$ and $Q(s',a')$, if those approximations are good, then the entry for $Q(s,a)$ should be close to $r+\gamma \max_{a'}Q(s',a')$.  The difference between those two elements is called the *Bellman error*, and is the only way we know if we're doing well or poorly in approximating these values.

### Tabular Q-Learning

For the purposes of this section, we'll assume a small, discrete number of states, and a small, discrete number of actions.  We'll also assume that $R$ and $P$ exist, but we don't know what they are.  So, we cannot calculate value directly, and our only way of learning anything about this MDP is by exploring it - collecting samples where we start in some state $s$, receive reward $r$, take action $a$, and as a result of taking that action, end up in state $s'$. Given those $(s,a,r,s')$ samples, we would like to approximate that optimal Q function table, so we could decide which action was best at each step to achieve our goal.

We are going to build a table of Q-values like the ones above, which is $|S|$ rows tall and $|A|$ actions wide, and each element is our approximation to $Q(s,a)$ for some $s$ and some $a$ (call this approximation $\hat Q(s,a)$.  We're going to start with random values for the Q-functions (or zeros) in this table, and gradually make them better, as the agent explores the space and we learn about the consequences of its actions.

As we explore, we are going to improve these values of $\hat Q(s,a)$ in order to minimize Bellman error.

So, suppose you just were in state $s$, took action $a$, received reward $r$, and ended up in state $s'$. We can refer to our table as it is, and retrieve our approximation of $Q(s,a)$ (call it $\hat Q(s,a)$), as well as $\hat Q(s',a')$, for all $a'$. So, if all those approximations are good, $\hat Q(s,a)$ and $r+\gamma\max_{a'}Q(s',a')$ should be close.

We can therefore do an update, where we replace $\hat Q(s,a)$ with a weighted average of the old approximation and $r+\gamma\max_{a'}Q(s',a')$.  We define a learning rate $\alpha$, and for some sample $(s,a,r,s')$, we use the following update rule:

$$
\begin{equation*}
\hat Q(s,a) \leftarrow \alpha\left(r+\gamma\max_{a'}Q(s',a')\right) + (1-\alpha)\hat Q(s,a)
\end{equation*}
$$

So the only thing that's left is to decide how we're going to generate these samples.  We need to balance two things: (1) We primarily care about the Q-values of good actions, as we're not going to take bad actions anyway, and (2) we don't really know what a good action is, for a while, until our table updates quite a bit.  This is known as balancing *exploitation* and *exploration*.

One approach to this is $\epsilon$-greedy exploration, where we define some small value $\epsilon$ (like in the range of .1-.4, or so), and most of the time take what you believe to be the best action based on your current Q-function approximations, but $\epsilon$% of the time take a random action.  So, our algorithm (known as "tabular Q-learning") becomes this:

- Create an initial table of approximate Q-functions for every state-action pair. These can be random, or 0.
- Start at starting state $s$
- Lots of times:
  - If a random number is less than $\epsilon$,
    - $a\leftarrow$ a random action
  - Else (most of the time)
    - $a\leftarrow \argmax_{a'} Q(s,a')$
  - Receive back the results of taking that action, so you now have a $(s,a,r,s')$ tuple.
  - $\hat Q(s,a) \leftarrow\alpha\left(r+\gamma\max_{a'}Q(s',a')\right) + (1-\alpha)\hat Q(s,a)$
  - $s \leftarrow s'$

After enough training, our Q-function approximations will be accurate enough to define an effective policy for this relatively simple RL problem.
