#Resizing and Cropping

import cv2

img = cv2.imread('resources\doraemon.png')
print(img.shape)
imgResize = cv2.resize(img,(1000,500)) #resize image to (width,height)

imgCrop= imgResize[0:200,200:500] #crop the image (height,width)


cv2.imshow("Image",img)
cv2.imshow("ResizedImage",imgResize)
cv2.imshow("CroppedImage",imgCrop)


cv2.waitKey(0)