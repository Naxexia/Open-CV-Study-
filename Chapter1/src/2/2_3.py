# coding=UTF-8
'''
Created on 2016年10月17日

@author: dmnnaxxi
'''
import cv2
import numpy as np


img = cv2.imread("E:\phonePhotos\\1449641309308.jpg" ,cv2.IMREAD_GRAYSCALE)
num_rows, num_cols = img.shape[:2]

sobel_horizontal = cv2.Sobel(img,cv2.CV_64F,1,0,ksize=5)
sobel_vertical = cv2.Sobel(img,cv2.CV_64F,0,1,ksize=5)

laplacian = cv2.Laplacian(img,cv2.CV_64F)

cv2.imshow('Original',img)
cv2.imshow('Sobel horizontal',sobel_horizontal)
cv2.imshow('Sobel Vertical',sobel_vertical)
cv2.imshow('laplacian',laplacian)

cv2.waitKey()