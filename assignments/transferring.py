from __future__ import print_function, division

import torch
import torch.nn as nn
import torch.optim as optim
from torch.optim import lr_scheduler
import numpy as np
import torchvision
from torchvision import datasets, models, transforms
import matplotlib.pyplot as plt
import time
import os
import copy
import warnings
warnings.filterwarnings("ignore")

import argparse
parser=argparse.ArgumentParser()
parser.add_argument("gpu",type=int)
args=parser.parse_args()
gpu=args.gpu
assert gpu>=0 and gpu<4
os.environ["CUDA_VISIBLE_DEVICES"]=str(gpu)

'''
Unlike with your previous project, here it's not possible to store all the data examples in memory, because images are too big.  This requires an infrastructure to load datapoints from the hard disk on the fly, during training.  This next block sets up that procedure.
'''

#Defines the transformations to do to the dataset, either for size standardization purposes, or for data augmentation purposes
#training is currently getting a random chunk cropped out to be used, and is randomly flipped.  Additionally, it gets turned into a tensor, and normalized
#testing is getting the very center cropped out, and normalized
#More transforms can be seen here: https://pytorch.org/docs/stable/torchvision/transforms.html
data_transforms = {
    'train': transforms.Compose([
      transforms.RandomResizedCrop(224),
      transforms.RandomHorizontalFlip(),
      transforms.ToTensor(),
      transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
      ]),
    'val': transforms.Compose([
      transforms.Resize(256),
      transforms.CenterCrop(224),
      transforms.ToTensor(),
      transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
      ]),
    }

data_dir = '.' #this is set up to run in the same directory as the train and val directories, you can change this
image_datasets = {x: datasets.ImageFolder(os.path.join(data_dir, x),   
                     data_transforms[x]) for x in ['train', 'val']}
dataloaders = {x: torch.utils.data.DataLoader(image_datasets[x],
                  batch_size=4, shuffle=True, num_workers=4)
                  for x in ['train', 'val']}
dataset_sizes = {x: len(image_datasets[x]) for x in ['train', 'val']}

#print out `class_names`, and you'll see it's identified them from the directory names
class_names = image_datasets['train'].classes

device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")

#this function trains a model for the given number of epochs, and returns the model which was best on the test set
def train_model(model, criterion, optimizer, scheduler, num_epochs=25):
    since = time.time()

    best_model_wts = copy.deepcopy(model.state_dict())
    best_acc = 0.0

    for epoch in range(num_epochs):
        print('Epoch {}/{}'.format(epoch, num_epochs - 1))
        print('-' * 10)

        # Each epoch has a training and validation phase
        for phase in ['train', 'val']:
            if phase == 'train':
                model.train()  # Set model to training mode
            else:
                model.eval()   # Set model to evaluate mode

            running_loss = 0.0
            running_corrects = 0

            # Iterate over data.
            for inputs, labels in dataloaders[phase]:
                inputs = inputs.to(device)
                labels = labels.to(device)

                # zero the parameter gradients
                optimizer.zero_grad()

                # forward
                # track history if only in train
                with torch.set_grad_enabled(phase == 'train'):
                    outputs = model(inputs)
                    _, preds = torch.max(outputs, 1)
                    loss = criterion(outputs, labels)

                    # backward + optimize only if in training phase
                    if phase == 'train':
                        loss.backward()
                        optimizer.step()

                # statistics
                running_loss += loss.item() * inputs.size(0)
                running_corrects += torch.sum(preds == labels.data)
            #if phase == 'train':
                #scheduler.step()

            epoch_loss = running_loss / dataset_sizes[phase]
            epoch_acc = running_corrects.double() / dataset_sizes[phase]

            print('{} Loss: {:.4f} Acc: {:.4f}'.format(
                phase, epoch_loss, epoch_acc))

            # deep copy the model if it's the best seen so far
            if phase == 'val' and epoch_acc > best_acc:
                best_acc = epoch_acc
                best_model_wts = copy.deepcopy(model.state_dict())

        print()

    time_elapsed = time.time() - since
    print('Training complete in {:.0f}m {:.0f}s'.format(
        time_elapsed // 60, time_elapsed % 60))
    print('Best val Acc: {:4f}'.format(best_acc))

    # load best model weights
    model.load_state_dict(best_model_wts)
    return model

#get a pretrained resnet-18 network
model_conv = torchvision.models.resnet18(pretrained=True)
#set all the parameters to NOT be modified during training
for param in model_conv.parameters():
    param.requires_grad = False

num_ftrs = model_conv.fc.in_features
#model_conv.fc is the "fully connected (fc)" part at the end of the network
#num_ftrs is the size of the vector being fed into the fully-connected part

#now we're going to replace the fully-connected part with our own.
#This needs to be a nn.Sequential, like in your last project, which ultimately
#goes from num_ftrs elements to "number of classes" elements.  In between you
#can have linear layers, activation functions, hidden layers, whatever.
#You should output with a Linear, with no activation function
model_conv.fc = #TODO


model_conv = model_conv.to(device)

criterion = nn.CrossEntropyLoss()

# Observe that only parameters of final layer are being optimized as
# opposed to before.
optimizer_conv = optim.Adam(model_conv.fc.parameters(), lr=0.001)
model_conv = train_model(model_conv, criterion, optimizer_conv,
                         None, num_epochs=50)
