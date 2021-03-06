# coding=UTF-8
'''
Created on 2016年10月17日

@author: dmnnaxxi
'''
import cv2
import numpy as np

img = cv2.imread("E:\phonePhotos\\1449641309308.jpg")
num_rows, num_cols = img.shape[:2]

translation_matrix = np.float32([[1,0,70],[0,1,110]])
img_translation = cv2.warpAffine(img,translation_matrix,(num_cols +70 ,num_rows + 110))
translation_matrix = np.float32([[1,0,-30],[0,1,-50]])
img_translation = cv2.warpAffine(img,translation_matrix,(num_cols +70 +30,num_rows + 110 +50))
cv2.imshow('Translation',img_translation)
cv2.waitKey()