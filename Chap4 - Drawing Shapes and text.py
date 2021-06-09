# Shapes and texts
import cv2
import numpy as np

img = np.zeros((512,512,3),np.uint8)

#img[:]=255,0,0
#lines
cv2.line(img,(0,0),(img.shape[1],img.shape[0]),(0,255,0),3) # draw a line (image,start point,end point,color,thickness)

#rectangle
cv2.rectangle(img,(0,0),(250,350),(255,0,0),cv2.FILLED)

#circle
cv2.circle(img,(400,50),30,(0,0,255),cv2.FILLED)

#text
cv2.putText(img,"OpenCV",(300,150),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,150,0),1)

cv2.imshow("Image",img)
cv2.waitKey(0)
