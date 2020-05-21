# -*- coding: utf-8 -*-
"""Replay.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1gE1OGk4fA1m1yDqPfnqv60NKxW8LzdkH
"""

import tensorflow as tf
from tensorflow.keras.applications.vgg19 import preprocess_input
from tensorflow.keras.applications import VGG19
from tensorflow.keras.models import Model
from tensorflow.keras.preprocessing.image import img_to_array, load_img
from tensorflow.keras.utils import plot_model
import numpy as np
import joblib


vgg_base_model = VGG19(weights='imagenet')
vgg19_model = Model(vgg_base_model.input, vgg_base_model.layers[-2].output)
 
def get_img_vec(img_path):
    img = load_img(img_path, target_size=(224, 224))
    img = img_to_array(img)
    img = np.expand_dims(img, axis=0)
    img = preprocess_input(img)
    img_vec = np.zeros((1, 4096))
    img_vec[0,:] = vgg19_model.predict(img)[0]
    return img_vec

def replay_predictions(img_path):
  filename = 'drive/My Drive/Processedvideo/replay_model.sav'
  loaded_model = joblib.load(filename)
  img_vec=get_img_vec(img_path)
  prediction=loaded_model.predict(img_vec)
  return prediction