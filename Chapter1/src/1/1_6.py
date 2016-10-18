# coding=UTF-8
'''
Created on 2016年10月17日

@author: dmnnaxxi
'''
import cv2
img = cv2.imread("E:\phonePhotos\\1449641309308.jpg")
yuv_img = cv2.cvtColor(img,cv2.COLOR_BGR2YUV)
cv2.imshow('Grayscale image', yuv_img)
cv2.imshow('Y Channel' , yuv_img[:,:,0])
cv2.imshow('U Channel' , yuv_img[:,:,1])
cv2.imshow('V Channel' , yuv_img[:,:,2])
cv2.waitKey()