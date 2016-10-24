# coding=UTF-8
'''
Created on 2016年10月22日

@author: dmnnaxxi

Interacting with a live video stream use mouse
How did we do it? As we can see in the main function 
of the program, we initialize a video capture object. 
We then bind the function draw_rectangle with the mouse 
callback in the following line: cv2.setMouseCallback
('Webcam', draw_rectangle) We then start an infinite 
loop and start capturing the video stream. Let’s see 
what is happening in the function draw_rectangle. 
Whenever we draw a rectangle using the mouse, we 
basically have to detect three types of mouse events: 
mouse click, mouse movement, and mouse button release. 
This is exactly what we do in this function. Whenever 
we detect a mouse click event, we initialize the top 
left point of the rectangle. As we move the mouse, we 
select the region of interest by keeping the current 
position as the bottom right point of the rectangle. 
Once we have the region of interest, we just invert 
the pixels to apply the “negative film” effect. We 
subtract the current pixel value from 255 and this 
gives us the desired effect. When the mouse movement 
stops and button-up event is detected, we stop updating 
the bottom right position of the rectangle. We just keep 
displaying this image until another mouse click event 
is detected
'''
import cv2
import numpy as np


def draw_rectangle(event, x,y,flags,params):
    global x_init,y_init,drawing,top_left_pt,bottom_right_pt
    
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        x_init,y_init = x,y
        
    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing:
            top_left_pt = (min(x_init,x),min(y_init,y))
            bottom_right_pt = (max(x_init,x),max(y_init,y))
            img[y_init:y,x_init:x] = 255 - img[y_init:y,x_init:x]
            
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        top_left_pt = (min(x_init,x),min(y_init,y))
        bottom_right_pt = (max(x_init,x),max(y_init,y))
        img[y_init:y,x_init:x] = 255 -img[y_init:y,x_init:x]
        
if __name__ == '__main__':
    drawing = False
    top_left_pt,bottom_right_pt = (-1,-1),(-1,-1)
    
    cap = cv2.VideoCapture(0)
    
    #Check if the webcam is opened correctly
    if not cap.isOpened():
        raise IOError("Cannot open webcam")
    
    cv2.namedWindow('Webcam')
    cv2.setMouseCallback('Webcam',draw_rectangle)
    
    while True:
        ret,frame = cap.read()
        img = cv2.resize(frame,None,fx=0.5,fy=0.5,interpolation=cv2.INTER_AREA)
        (x0,y0) ,(x1,y1) = top_left_pt,bottom_right_pt
        img[y0:y1,x0:x1] = 255 - img[y0:y1,x0:x1]
        cv2.imshow('Webcam',img)
        
        c = cv2.waitKey(1)
        if c == 27:
            break
    cap.release()
    cv2.destroyAllWindows()
    
    