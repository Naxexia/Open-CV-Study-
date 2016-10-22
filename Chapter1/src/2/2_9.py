# coding=UTF-8
'''
Created on 2016年10月18日

@author: dmnnaxxi
Enhancing the contrast in an image

Now that we know how to equalize the histogram of 
a grayscale image, you might be wondering how to 
handle color images. The thing about histogram 
equalization is that it’s a nonlinear process. 
So, we cannot just separate out the three channels
 in an RGB image, equalize the histogram separately,
and combine them later to form the output image. 
The concept of histogram equalization is only 
applicable to the intensity values in the image. 
So, we have to make sure not to modify the color 
information when we do this. In order to handle 
the histogram equalization of color images, 
we need to convert it to a color space where 
intensity is separated from the color information. 
YUV is a good example of such a color space. 
Once we convert it to YUV , we just need to equalize 
the Ychannel and combine it with the other two channels 
to get the output image
'''
import cv2
import numpy as np

img = cv2.imread('pics\darkImg.PNG')

img_yuv = cv2.cvtColor(img , cv2.COLOR_BGR2YUV)

#equalize the histogram of the Y channel
img_yuv[:,:,0] = cv2.equalizeHist(img_yuv[:,:,0])

#convert the YUV image back to RGB format
img_output = cv2.cvtColor(img_yuv,cv2.COLOR_YUV2BGR)

cv2.imshow('Color input image', img)
cv2.imshow('Histogram equalized', img_output)

cv2.waitKey()