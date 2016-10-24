# coding=UTF-8
'''
Created on 2016年10月24日

@author: dmnnaxxi

Gaussian filter & Bilateral filter
If you closely observe the two outputs, you can see 
that the edges in the Gaussian filtered image look blurred. 
Usually, we just want to smoothen the rough areas in the 
image and keep the edges intact. This is where the bilateral 
filter comes in handy. The Gaussian filter just looks at the 
immediate neighborhood and averages the pixel values using a 
Gaussian kernel. The bilateral filter takes this concept to 
the next level by averaging only those pixels that are similar 
to each other in intensity. It also takes a color neighborhood 
metric to see if it can replace the current pixel that is similar 
in intensity as well. If you look the function call:
img_small = cv2.bilateralFilter(img_small, size, sigma_color, sigma_space) 
The last two arguments here specify the color and space neighborhood. 
This is the reason the edges look crisp in the output of the bilateral filter. 
We run this filter multiple times on the image to smoothen it out, 
to make it look like a cartoon. We then superimpose the pencil-like 
mask on top of this color image to create a cartoon-like effect.
'''
import cv2
import numpy as np

img = cv2.imread('pics/CaptureBilateralFilter.PNG')

img_gaussian = cv2.GaussianBlur(img,(13,13),0)
img_bilateral = cv2.bilateralFilter(img,13,70,50)

cv2.imshow('Input',img)
cv2.imshow('Gaussian filter',img_gaussian)
cv2.imshow('Bilateral filter',img_bilateral)
cv2.waitKey()