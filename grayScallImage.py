# pip install opencv-contrib-python==4.5.5.62

import cv2
import numpy as numpy

# Setting up the Original Image
originalImage = cv2.imread('Class-65/img1.png')

grayImage = cv2.cvtColor(originalImage, cv2.COLOR_BGR2GRAY)

oilPainting = cv2.xphoto.oilPainting(originalImage,size=7,dynRatio=1)

invertedImg=255-grayImage
bluredImg = cv2.GaussianBlur(invertedImg,(21,21),0)

sketchImg = cv2.divide(grayImage,255-bluredImg,scale=256)

cv2.imshow('original', originalImage)
cv2.imshow('gray', grayImage)
cv2.imshow('oil', oilPainting)
cv2.imshow('blured', bluredImg)
cv2.imshow('sketch', sketchImg)
cv2.waitKey(0)