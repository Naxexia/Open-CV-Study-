# coding=UTF-8+-
'''
Created on 2016年10月24日

@author: dmnnaxxi
Detecting and tracking faces
We need a classifier model that can be used to 
detect the faces in an image. OpenCV provides 
an xml file that can be used for this purpose. 
We use the function CascadeClassifier to load 
the xml file. Once we start capturing the input 
frames from the webcam, we convert it to grayscale 
and use the function detectMultiScale to get the 
bounding boxes for all the faces in the current 
image. The second argument in this function 
specifies the jump in the scaling factor. 
As in, if we don’t find an image in the current 
scale, the next size to check will be, in our case, 
1.3 times bigger than the current size. The last 
parameter is a threshold that specifies the number 
of adjacent rectangles needed to keep the current 
rectangle. It can be used to increase the robustness 
of the face detector.
'''
import cv2
import numpy as np

face_cascade = cv2.CascadeClassifier('../../haarcascades/haarcascade_frontalface_alt.xml')

cap = cv2.VideoCapture(0)
scalling_factor = 0.5

while True:
    ret,frame = cap.read()
    frame = cv2.resize(frame,None,fx=scalling_factor,fy=scalling_factor,interpolation=cv2.INTER_AREA)
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    
    face_rects = face_cascade.detectMultiScale(gray,1.3,5)
    for (x,y,w,h) in face_rects:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),3)
        
    cv2.imshow('Face Detector',frame)
    
    c = cv2.waitKey(1)
    if c == 27:
        break
    
cap.release()
cv2.destroyAllWindows()
