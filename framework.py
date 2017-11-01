import numpy as np
import tflearn
import tensorflow as tf
import random

import pickle
import json

# restore all of our data structures
data = pickle.load(open("training_data", "rb"))
words = data['words']
classes = data['classes']
train_x = data['train_x']
train_y = data['train_y']

# import our chat-bot intents file


with open('intents.json') as json_data:
    intents = json.load(json_data)

# Define model and setup tensorboard
model = tflearn.DNN(data, tensorboard_dir='tflearn_logs')

# load our saved model
model.load('./model.tflearn')
