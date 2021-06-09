# Color Detection

import cv2
import numpy as np

def empty(a):
    pass


def stackImages(scale,imgArray):
    rows = len(imgArray)
    cols = len(imgArray[0])
    rowsAvailable = isinstance(imgArray[0], list)
    width = imgArray[0][0].shape[1]
    height = imgArray[0][0].shape[0]
    if rowsAvailable:
        for x in range ( 0, rows):
            for y in range(0, cols):
                if imgArray[x][y].shape[:2] == imgArray[0][0].shape [:2]:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (0, 0), None, scale, scale)
                else:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (imgArray[0][0].shape[1], imgArray[0][0].shape[0]), None, scale, scale)
                if len(imgArray[x][y].shape) == 2: imgArray[x][y]= cv2.cvtColor( imgArray[x][y], cv2.COLOR_GRAY2BGR)
        imageBlank = np.zeros((height, width, 3), np.uint8)
        hor = [imageBlank]*rows
        hor_con = [imageBlank]*rows
        for x in range(0, rows):
            hor[x] = np.hstack(imgArray[x])
        ver = np.vstack(hor)
    else:
        for x in range(0, rows):
            if imgArray[x].shape[:2] == imgArray[0].shape[:2]:
                imgArray[x] = cv2.resize(imgArray[x], (0, 0), None, scale, scale)
            else:
                imgArray[x] = cv2.resize(imgArray[x], (imgArray[0].shape[1], imgArray[0].shape[0]), None,scale, scale)
            if len(imgArray[x].shape) == 2: imgArray[x] = cv2.cvtColor(imgArray[x], cv2.COLOR_GRAY2BGR)
        hor= np.hstack(imgArray)
        ver = hor
    return ver

path = 'resources\doraemon.png'

cv2.namedWindow("Trackbars")
cv2.resizeWindow("Trackbars",640,240)

cv2.createTrackbar("Hue Min","Trackbars",26,179,empty)
cv2.createTrackbar("Hue Max","Trackbars",173,179,empty)

cv2.createTrackbar("Sat Min","Trackbars",1,255,empty)
cv2.createTrackbar("Sat Max","Trackbars",255,255,empty)

cv2.createTrackbar("Val Min","Trackbars",0,255,empty)
cv2.createTrackbar("Val Max","Trackbars",255,255,empty)

while True:
    img = cv2.imread(path)

    imgHSV = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

    hmin = cv2.getTrackbarPos("Hue Min","Trackbars")
    hmax = cv2.getTrackbarPos("Hue Max","Trackbars")
    smin = cv2.getTrackbarPos("Sat Min","Trackbars")
    smax = cv2.getTrackbarPos("Sat Max","Trackbars")
    vmin = cv2.getTrackbarPos("Val Min","Trackbars")
    vmax = cv2.getTrackbarPos("Val Max","Trackbars")

    print(hmin,hmax,smin,smax,vmin,vmax)
    upper = np.array([hmax,smax,vmax])
    lower = np.array([hmin,smin,vmin])
    mask = cv2.inRange(imgHSV,lower,upper)

    imgResult = cv2.bitwise_and(img,img,mask=mask)

    
    # cv2.imshow("original",img)
    # cv2.imshow("HSV img",imgHSV)
    # cv2.imshow("Mask",mask)
    # cv2.imshow("Result",imgResult)

    imgStack = stackImages(1,([img,imgHSV],[mask,imgResult]))
    cv2.imshow("Stacked images",imgStack)

    

    cv2.waitKey(1)