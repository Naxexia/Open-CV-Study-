# coding=UTF-8
'''
Created on 2016年10月23日

@author: dmnnaxxi

Median filter example
As we see in the input image, there are a lot of 
isolated green pixels. They are lowering the quality 
of the image and we need to get rid of them. This is 
where the median filter comes in handy. We just look 
at the NxN neighborhood around each pixel and pick the 
median value of those numbers. Since the isolated pixels 
in this case have high values, taking the median value 
will get rid of these values and also smoothen the image. 
As you can see in the output image, the median filter got 
rid of all those isolated pixels and the image looks 
clean.
'''
import cv2
import numpy as np

img = cv2.imread('pics/medianFilter.PNG')
output = cv2.medianBlur(img,7)
cv2.imshow('Input',img)
cv2.imshow('Median filter',output)
cv2.waitKey()
