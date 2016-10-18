# coding=UTF-8
'''
Created on 2016年10月18日

@author: dmnnaxxi
Creating a vignette filter
'''
import cv2
import numpy as np



img = cv2.imread('pics\vignette.PNG')
rows, cols = img.shape[:2]


# Generating vignette mask using Gaussian kernels
kernel_x = cv2.getGaussianKernel(cols,200)
kernel_y = cv2.getGaussianKernel(rows,200)
kernel = kernel_y * kernel_x.T
mask = 255 * kernel / np.linalg.norm(kernel)
output = np.copy(img)

#applying the mask to each channel in the input image
for i in range(3):
    output[:,:,i] = output[:,:,i] * mask
    
cv2.imshow('Original', img)
cv2.imshow('Vignette', output)

cv2.waitKey()