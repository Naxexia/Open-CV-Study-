# coding=UTF-8
'''
Created on 2016年10月18日

@author: dmnnaxxi
Embossing
'''
import cv2
import numpy as np



img = cv2.imread("E:\phonePhotos\\1449641309308.jpg")


# Generating the kernels
kernel_emboss_1 = np.array([[0,-1,-1],[1,0,-1],[1,1,0]])
kernel_emboss_2 = np.array([[-1,-1,0],[-1,0,1],[0,1,1]])
kernel_emboss_3 = np.array([[1,0,0],[0,0,0],[0,0,-1]])
                             
#applying different kernels to the input image
gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

#applying the kernels to the grayscale imge and adding the offset
output_1 = cv2.filter2D(gray_img,-1,kernel_emboss_1) + 128
output_2 = cv2.filter2D(gray_img,-1,kernel_emboss_2) + 128
output_3 = cv2.filter2D(gray_img,-1,kernel_emboss_3) + 128

cv2.imshow('Input',img)
cv2.imshow('Embossing - South West',output_1)
cv2.imshow('Embossing - South East',output_2)
cv2.imshow('Embossing - North West',output_3)

cv2.waitKey()