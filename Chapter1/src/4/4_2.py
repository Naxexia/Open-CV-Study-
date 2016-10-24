# coding=UTF-8+-
'''
Created on 2016年10月24日

@author: dmnnaxxi
Detecting and tracking faces
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
