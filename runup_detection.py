# -*- coding: utf-8 -*-
"""Runup_detection.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1w0-Qgs2sXY1hPFPwK8Vp62ax8EmGoLUT
"""

import tensorflow as tf
import imageai.Detection
from imageai.Detection import ObjectDetection
import os
from google.colab.patches import cv2_imshow
import tensorflow as tf
import cv2
detector = ObjectDetection()
detector.setModelTypeAsYOLOv3()
detector.setModelPath("drive/My Drive/Processedvideo/yolo.h5")
detector.loadModel()

def get_players_count(filename):
    detections = detector.detectObjectsFromImage(input_image=filename, output_image_path="abc.jpg", minimum_percentage_probability=30)
    count=0
    i=0
    img=cv2.imread('abc.jpg')
    img=cv2.resize(img,(200,200))
    cv2_imshow(img)
    while i<len(detections):
      if detections[i]['name']=='person':
        count=count+1
      i=i+1
    return count