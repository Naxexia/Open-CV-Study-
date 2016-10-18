# coding=UTF-8
'''
Created on 2016年10月17日

@author: dmnnaxxi
'''
import cv2
import numpy as np

img = cv2.imread("E:\phonePhotos\\1449641309308.jpg")
img_scaled = cv2.resize(img,None,fx=1.2,fy=1.2,interpolation = cv2.INTER_LINEAR)
cv2.imshow('Scaling - Linear Interpolation' ,img_scaled)
img_scaled = cv2.resize(img,None,fx=1.2,fy=1.2,interpolation = cv2.INTER_CUBIC)
cv2.imshow('Scaling - Cubic Interpolation',img_scaled)
img_scaled = cv2.resize(img,(450,400),interpolation = cv2.INTER_AREA)
cv2.imshow('Scaling - Skewed Size',img_scaled)
cv2.waitKey()