# FACE Detection

#viola and jones method

import cv2

faceCascade= cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml') #(data haarcascade + name of the cascade which we are using
img = cv2.imread('Resources/faces.jpg')
imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

faces = faceCascade.detectMultiScale(imgGray,1.1,4) #image, scale,minimum neighbors

for (x,y,w,h) in faces: #loop through x,y initial points w- width and h-height
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2) #draw rectangle around the faces detected.
                    # (x,y)=initial point (x+w,y+h)=final diagonal point, color and thickness.

cv2.imshow("Result", img)
cv2.waitKey(0)
