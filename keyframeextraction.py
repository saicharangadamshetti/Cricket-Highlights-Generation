# -*- coding: utf-8 -*-
"""keyframeextraction.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/12pRlWPiwFgiem3S7Goec2iz98JIkZrf-
"""

import pathlib
import glob
import os
import cv2
import moviepy.editor as mp
from google.colab.patches import cv2_imshow
from moviepy.editor import VideoFileClip, concatenate_videoclips

def keyframe_extraction(foldername,filename,time,count):
  vidcap=cv2.VideoCapture(filename)
  vidcap.set(cv2.CAP_PROP_POS_MSEC,time)
  success,image=vidcap.read()
  if success:
    targetname=foldername+'/frame'+str(count)+'.jpg'
    cv2.imwrite(targetname,image)
    print(targetname)
    cv2_imshow(image)
    cv2.waitKey()

def clip_extraction(filename,foldername):
  video = VideoFileClip(filename)
  duration=int(video.duration)
  duration=duration*1000
  i=0
  count=0
  while i<=duration:
    count=count+1
    keyframe_extraction(foldername,filename,i,count)
    i=i+1000

if __name__ == '__main__':
  count=1
  for filename in glob.glob("drive/My Drive/Processedvideo/highlights_without_replay/*.mp4"):
    foldername='drive/My Drive/Processedvideo/keyframe/clip'+str(count)
    if not os.path.exists(foldername):
      os.makedirs(foldername)
    print(foldername)
    filename='drive/My Drive/Processedvideo/highlights_without_replay/clip'+str(count)+'.mp4'
    clip_extraction(filename,foldername)
    count=count+1

from Katna.video import Video
import os
import cv2
vd = Video()
clip_name = os.listdir('drive/My Drive/Processedvideo/highlights')
count1=0
for name in clip_name:
    count1=count1+1
    filename='drive/My Drive/Processedvideo/highlights/'+name
    imgs = vd.extract_frames_as_images(no_of_frames = 30, file_path=filename)
    foldername='drive/My Drive/Processedvideo/KeyFrames/clip'+str(count1)
    if not os.path.exists(foldername):
      os.makedirs(foldername)
    count2=1
    for img in imgs:
      img_name=foldername+'/'+str(count2)+'.jpg'
      print(img_name)
      cv2.imwrite(img_name,img)
      count2=count2+1

from google.colab.patches import cv2_imshow
for img in imgs:
  resized = cv2.resize(img, (500,500), interpolation = cv2.INTER_AREA)
  cv2_imshow(resized)

from scoreboardextraction import get_wickets_and_score
a=get_wickets_and_score('frame4.jpg')