# coding=UTF-8
'''
Created on 2016年10月14日

@author: dmnnaxxi
'''
import cv2
img = cv2.imread("E:\phonePhotos\\1449641309308.jpg",cv2.IMREAD_GRAYSCALE)
cv2.imshow('Grayscale image' , img)
cv2.waitKey()
cv2.imwrite('E:\phonePhotos\\1449641309308Output.jpg',img)
