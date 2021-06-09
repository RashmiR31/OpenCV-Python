# Project 1
# Virtual Paint

# import cv2
# import numpy as np

# framewidth = 640
# frameheight = 480
# cap = cv2.VideoCapture(0)
# cap.set(3, framewidth)
# cap.set(4,frameheight)
# cap.set(10,150)

# myColors = [[0,129,100,56,241,255], #RED
#         [40,92,41,96,255,255]     #green       
#         ]  

# myColorValues=[[26,26,255],[0,255,0]]  #BGR

# myPoints = [] #[x,y,colorID]

# def findColor(img,myColors,myColorValues):
#     imgHSV = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
#     count=0
#     newPoints=[]
#     for color in myColors:
#         lower = np.array(myColors[0][0:3])
#         upper = np.array(myColors[0][3:6])
#         mask = cv2.inRange(imgHSV,lower,upper)
#         #cv2.imshow("image",mask)
#         x,y = getContours(mask)
#         cv2.circle(imgResult,(x,y),10,myColorValues[count],cv2.FILLED)
#         if x!=0 and y!=0:
#             newPoints.append([x,y,count])
#         count+=1
#     return newPoints
    

# def getContours(img):
#     contours,hierarchy = cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
#     x,y,w,h =0,0,0,0
#     for cnt in contours:
#         area = cv2.contourArea(cnt)
#         #min threshold for area to detect less noise
#         if area>500:
#             #cv2.drawContours(imgResult,cnt,-1,(255,0,0),3) #draw the contour on a copy of the image. It takes argument (copy of image, contour,-1 means all contours,color,thickness)
#             #curve length
#             peri = cv2.arcLength(cnt,True)
#             approx = cv2.approxPolyDP(cnt,0.02*peri,True)
#             #
#             objCorner = len(approx) #number of corners the shape has
#             x, y, w, h = cv2.boundingRect(approx) # form a ractangle box suurounding it - x=point y=point w=width h=height
#     return x+w//2,y


# def drawOnCanvas(myPoints,myColorValues):
#     for point in myPoints:
#         cv2.circle(imgResult,(point[0],point[1]),20,myColorValues[point[2]],cv2.FILLED)


# while True:
#     success,img = cap.read()
#     imgResult = img.copy()
#     newPoints = findColor(img,myColors,myColorValues)
#     if len(newPoints)!=0:
#         for newP in newPoints:
#             myPoints.append(newP)

#     if len(myPoints)!=0:
#         drawOnCanvas(myPoints,myColorValues)
#     cv2.imshow("Result",imgResult)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break


################################################################################################
import cv2
import numpy as np
frameWidth = 640
frameHeight = 480
cap = cv2.VideoCapture(0)
cap.set(3, frameWidth)
cap.set(4, frameHeight)
cap.set(10,150)

myColors = [[0,129,100,56,241,255],[40,92,41,96,255,255]]
myColorValues = [[26,26,255],[0,255,0]]

myPoints =  []  ## [x , y , colorId ]

def findColor(img,myColors,myColorValues):
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    count = 0
    newPoints=[]
    for color in myColors:
        lower = np.array(color[0:3])
        upper = np.array(color[3:6])
        mask = cv2.inRange(imgHSV,lower,upper)
        x,y=getContours(mask)
        cv2.circle(imgResult,(x,y),15,myColorValues[count],cv2.FILLED)
        if x!=0 and y!=0:
            newPoints.append([x,y,count])
        count +=1
        #cv2.imshow(str(color[0]),mask)
    return newPoints

def getContours(img):
    contours,hierarchy = cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    x,y,w,h = 0,0,0,0
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area>500:
            #cv2.drawContours(imgResult, cnt, -1, (255, 0, 0), 3)
            peri = cv2.arcLength(cnt,True)
            approx = cv2.approxPolyDP(cnt,0.02*peri,True)
            x, y, w, h = cv2.boundingRect(approx)
    return x+w//2,y

def drawOnCanvas(myPoints,myColorValues):
    for point in myPoints:
        cv2.circle(imgResult, (point[0], point[1]), 10, myColorValues[point[2]], cv2.FILLED)


while True:
    success, img = cap.read()
    imgResult = img.copy()
    newPoints = findColor(img, myColors,myColorValues)
    if len(newPoints)!=0:
        for newP in newPoints:
            myPoints.append(newP)
    if len(myPoints)!=0:
        drawOnCanvas(myPoints,myColorValues)


    cv2.imshow("Result", imgResult)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break