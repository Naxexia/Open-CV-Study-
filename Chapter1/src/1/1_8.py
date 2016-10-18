# coding=UTF-8
'''
Created on 2016年10月17日

@author: dmnnaxxi
'''
import cv2
img = cv2.imread("E:\phonePhotos\\1449641309308.jpg")
hsv_img = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
cv2.imshow('HSV image', hsv_img)
cv2.imshow('H Channel' , hsv_img[:,:,0])
cv2.imshow('S Channel' , hsv_img[:,:,1])
cv2.imshow('V Channel' , hsv_img[:,:,2])
cv2.waitKey()