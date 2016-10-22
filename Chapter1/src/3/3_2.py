# coding=UTF-8
'''
Created on 2016年10月22日

@author: dmnnaxxi
Keyboard Input
'''
import argparse
import cv2
from argparse import PARSER

def argument_parser():
    parser =argparse.ArgumentParser(description="Change color space of the \
             input video stream using keyboard controls.The control keys \
            are: Grayscale = 'g', YUV -'y', HSV - 'h'")
    return parser

if __name__ == '__main__':
    
        
