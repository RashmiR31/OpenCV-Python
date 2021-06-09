#Basic Functions

import cv2
import numpy as np

#read the image
img = cv2.imread('resources\doraemon.png')
kernel=np.ones((5,5),np.uint8)

imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) #turn a colored image into gray scale
imgBlur = cv2.GaussianBlur(imgGray,(7,7),0) # Blur the image
imgCanny = cv2.Canny(img,150,200) # detect the edges of the image
imgDilation = cv2.dilate(imgCanny,kernel,iterations=1) #dilate the edges of the image 
imgErroded = cv2.erode(imgDilation,kernel,iterations=1) # thin/errode the dilated image


cv2.imshow('GrayImage',imgGray)
cv2.imshow('BlurImage',imgBlur)
cv2.imshow('CannyImage',imgCanny)
cv2.imshow('DilationImage',imgDilation)
cv2.imshow('ErrodedImage',imgErroded)




cv2.waitKey(0)