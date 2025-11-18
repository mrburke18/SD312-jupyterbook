#!/usr/bin/env python

import gymnasium as gym
import numpy as np
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('file', help="filename of saved numpy array of Q values")
parser.add_argument('--size',
    help='4x4 or 8x8',
    choices={'4x4','8x8'},
    default='4x4')
parser.add_argument('--is_slippery',
    help='include if is_slippery should be True',
    action='store_true')
args = parser.parse_args()
print(args)

Qs = np.load(args.file)
env = gym.make('FrozenLake-v1', desc=None, map_name=args.size,
    is_slippery=args.is_slippery, render_mode='human')
observation, info = env.reset()
for _ in range(20):
    old_observation = observation
    action = np.argmax(Qs[observation,:])
    observation, reward, terminated, truncated, info = env.step(action)
    
    if terminated or truncated:
        observation, info = env.reset()

env.close()
