import gymnasium as gym
import numpy as np
import numpy.random
import torch
import torch.nn as nn
from collections import deque, namedtuple
import random

class DQN(nn.Module):

    def __init__(self, n_observations, n_actions):
        super(DQN, self).__init__()
        self.layer1 = nn.Linear(n_observations, 64)
        self.layer2 = nn.Linear(64,64)
        self.layer3 = nn.Linear(64,64)
        self.layer4 = nn.Linear(64, n_actions)

    # Called with either one element to determine next action, or a batch
    # during optimization. Returns tensor([[left0exp,right0exp]...]).
    def forward(self, x):
        x = nn.ReLU()(self.layer1(x))
        x = nn.ReLU()(self.layer2(x))
        x = nn.ReLU()(self.layer3(x))
        return self.layer4(x)

def greedy_policy(network, state):
    '''
    Returns a tuple
    index 0 contains the Q-value of the best action
    index 1 contains the index of the best action
    '''
    with torch.no_grad():
        qs = network(state)
        if qs.dim() == 1:
            qs = qs.unsqueeze(0)
        return torch.max(qs, dim=1)

#network = torch.load('good_cartpole')
network = torch.load('run_500_1')

env = gym.make('CartPole-v1', render_mode='human')
steps=[]
for trial in range(1000):
    step=0
    state, info = env.reset()
    terminated = truncated = False
    while not (terminated or truncated):
        action = greedy_policy(network, torch.tensor(state).to('cuda'))[1].item()
        sp, r, terminated, truncated, _ = env.step(action)
        state = sp
        step+=1
    steps.append(step)
    print(step)
