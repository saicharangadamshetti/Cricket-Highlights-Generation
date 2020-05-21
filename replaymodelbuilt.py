# -*- coding: utf-8 -*-
"""Replaymodelbuilt.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/17dVX3KsQNCE-hXYPNoiO1FK6xMQ0S0AD
"""

import tensorflow as tf
from tensorflow.keras.applications.vgg19 import preprocess_input
from tensorflow.keras.applications import VGG19
from tensorflow.keras.models import Model
from tensorflow.keras.preprocessing.image import img_to_array, load_img
from tensorflow.keras.utils import plot_model
from sklearn.model_selection import train_test_split
from sklearn.svm import LinearSVC
from pathlib import Path
from sklearn.metrics import accuracy_score
import numpy as np
import os
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

def dataset_load():
  X = []
  y = []
  x = []
  container_path1='drive/My Drive/Dataset/small_dataset/Live'
  container_path2='drive/My Drive/Dataset/small_dataset/replay'
  directory1 = Path(container_path1)
  directory2 = Path(container_path2)
  for filename in os.listdir(container_path1):
    X.append(get_img_vec('drive/My Drive/Dataset/small_dataset/Live/'+ filename))
    print('success ' + filename)
    y.append(0)
  for filename in os.listdir(container_path2):
    X.append(get_img_vec('drive/My Drive/Dataset/small_dataset/replay/'+filename))
    print('success ' + filename)
    y.append(1)
  for temp in X:
    for element in temp:
      x.append(element)

if __name__ == '__main__':
    X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.30, random_state=42, stratify=y)
    clf = LinearSVC(random_state=0, tol=1e-5)
    clf.fit(X_train, y_train)
    predicted = clf.predict(X_test)
    print (accuracy_score(y_test, predicted))
    filename = 'drive/My Drive/Processedvideo/replay_model.sav'
    joblib.dump(clf, filename)
    loaded_model = joblib.load(filename)

"""# New Section"""