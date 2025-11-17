import gymnasium as gym
import numpy as np
import numpy.random
import torch
import torch.nn as nn
import torch.optim as optim
from collections import deque, namedtuple
import random
import plotly.graph_objects as go
from tqdm import tqdm
import matplotlib.pyplot as plt
import torchvision
import torchvision.tv_tensors
from torchvision.transforms.v2.functional import to_grayscale, to_dtype

class DQN(nn.Module):

    def __init__(self, n_actions):
        super(DQN, self).__init__()
        self.conv1 = nn.Sequential(
            nn.Conv2d(in_channels=1,
                      out_channels=16,
                      kernel_size=8,
                      stride=4),
            nn.ReLU()
        )
        self.conv2 = nn.Sequential(
            nn.Conv2d(in_channels=16,
                      out_channels=32,
                      kernel_size=4,
                      stride=2),
            nn.ReLU()
        )
        self.fc = nn.Sequential(
            nn.Linear(3200, 256),
            nn.ReLU(),
            nn.Linear(256, 5)
        )

    # Called with either one element to determine next action, or a batch
    # during optimization. Returns tensor([[left0exp,right0exp]...]).
    def forward(self, x):
        x = self.conv1(x)
        x = self.conv2(x)
        x = x.view(x.size(0), -1)
        return self.fc(x)

def state_to_tensor(state):
    '''
    state is assumed to be 96x96x3
    '''
    img = torchvision.tv_tensors.Image(np.transpose(state,(2,0,1)))
    img = to_dtype(to_grayscale(img), torch.float32)
    return img

def greedy_policy(network, states):
    '''
    Returns a tuple
    index 0 contains the Q-value of the best action for all states
    index 1 contains the index of the best action for all states
    '''
    with torch.no_grad():
        if states.dim()==3:
            states = states.unsqueeze(0)
        qs = network(states) # Get the q-values
        if qs.dim() == 1:   # Make it work even when applied to a single state, rather than a batch
            qs = qs.unsqueeze(0)
        return torch.max(qs, dim=1) # Return the tuple of max information

#network = torch.load('good_cartpole')
network = DQN(5)
network.load_state_dict(torch.load('car_model'))
network = network.to('cuda')
network.eval()

env = gym.make('CarRacing-v2', domain_randomize=False, continuous=False, render_mode='human')
for trial in range(1000):
    step=0
    state, info = env.reset(options={'randomize': False})
    for _ in range(50):
        state,r,terminated,truncated,info = env.step(0)
    terminated = truncated = False
    state = state_to_tensor(state)
    while not (truncated or terminated) and step < 500:
        action = greedy_policy(network, state.to('cuda'))[1].item()
        next_state, reward, terminated, truncated, _ = env.step(action)
        next_state = state_to_tensor(next_state)
        state = next_state
        step+=1
