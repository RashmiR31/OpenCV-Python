#Contours / Shape Detection
import cv2
import numpy as np

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


def getContours(img):
    contours,hierarchy = cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        area = cv2.contourArea(cnt)
        print(area)
        #cv2.drawContours(imgcontour,cnt,-1,(255,0,0),3) #draw the contour on a copy of the image. It takes argument (copy of image, contour,-1 means all contours,color,thickness)

        #min threshold for area to detect less noise
        if area>500:
            cv2.drawContours(imgcontour,cnt,-1,(255,0,0),3) #draw the contour on a copy of the image. It takes argument (copy of image, contour,-1 means all contours,color,thickness)
            #curve length
            peri = cv2.arcLength(cnt,True)
            #print(peri)
            #approximate corner points
            approx = cv2.approxPolyDP(cnt,0.02*peri,True)
            print(len(approx))

            #
            objCorner = len(approx) #number of corners the shape has
            x, y, w, h = cv2.boundingRect(approx) # form a ractangle box suurounding it - x=point y=point w=width h=height
            #categorize
            if objCorner==3:
                objectType = "Tri"
            elif objCorner == 4:
                aspRatio = w/float(h)
                if aspRatio >0.95 and aspRatio<1.05:
                    objectType="Square"
                else:
                    objectType="Rect"
            elif objCorner>4:
                objectType = "circle"
            else:
                objectType = None
            
            
            cv2.rectangle(imgcontour,(x,y),(x+w,y+h),(0,255,0),2) # form a rectangle box suurounding it - (image to b drawn on,points,(x+width,y+height),color,thickness)
            cv2.putText(imgcontour,objectType,
            (x+(w//2)-10,y+(h//2)-10), #near to center of obj
            cv2.FONT_HERSHEY_COMPLEX,
            0.7,
            (0,0,0),2)
            
            

img = cv2.imread('resources\shapes.png')

imgcontour = img.copy()
imgGray= cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray,(7,7),1)
imgCanny = cv2.Canny(imgBlur,50,50)

getContours(imgCanny)

imgBlank = np.zeros_like(img)


imgStack =stackImages(0.4,([img,imgGray,imgBlur],[imgCanny,imgcontour,imgBlank]))

cv2.imshow("Stack",imgStack)
cv2.waitKey(0)
