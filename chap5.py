# Warp Perspective

import cv2
import numpy as np

img= cv2.imread('resources\card1.jpg')

width,height = 250,350  #can specify widthand height of the output image
pts1 = np.float32([[224,90],[433,135],[162,383],[370,428]]) # a numpy array of the four points of the card # find the points in paint
pts2 = np.float32([[0,0],[width,0],[0,height],[width,height]]) # specifying which point is what
matrix = cv2.getPerspectiveTransform(pts1,pts2) #defining a matrix with the points
imgOutput = cv2.warpPerspective(img,matrix,(width,height)) #warpPerspective function to crop and make the image as flat as possible

cv2.imshow("Image",img)
cv2.imshow("Output",imgOutput)

cv2.waitKey(0)