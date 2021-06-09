#Read images - videos and webcam
import cv2
"""
# How to display images

img = cv2.imread('resources\doraemon.png')

cv2.imshow('output',img)

cv2.waitKey(0)
"""
"""
# How to run a video

cap = cv2.VideoCapture('test.mp4')

while True:
    success,img = cap.read()
    cv2.imshow("Video",img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
"""  
#how to use webcam
cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4,480)
cap.set(10,100)

while True:
    success,img = cap.read()
    cv2.imshow("Video",img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
