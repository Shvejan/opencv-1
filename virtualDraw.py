import cv2
import numpy as np

import stackimages

vdo = cv2.VideoCapture(0)
#rubicsCube
#colors = [[87 ,97, 125, 249, 148, 204], [5, 10, 148, 222, 191, 255], [102 ,111 ,148 ,224 ,159,  225]]

colors = [[105 ,115, 142 ,201, 164, 239], [83 ,95 ,156 ,252, 122 ,208], [119, 178 ,59, 229, 255, 255]]
color_value = [(255,0,0),(0,255,0),(0,0,255)]
#markers
allPoints = []


def getCountour(img):
    countours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    for cnt in countours:
        area = cv2.contourArea(cnt)
        if (area>50):
            x,y=0,0
            #cv2.drawContours(blank, cnt, -1, (255, 0, 0), 3)
            perimetre = cv2.arcLength(cnt, True)
            allPoints = cv2.approxPolyDP(cnt, 0.04 * perimetre, True)
            x, y, w, h = cv2.boundingRect(allPoints)
            return (x+w//2,y)











def findColor(img):
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    masks = []
    new_points = []
    for i in range(len(colors)):
        masks.append(cv2.inRange(hsv, np.array((colors[i][0], colors[i][2], colors[i][4])), np.array((colors[i][1], colors[i][3], colors[i][5]))))
        a=getCountour(masks[i])
        cv2.circle(blank,a,9,color_value[i],-1)
        if(a!=None):
            if(a[0]!=0and a[1]!=0):
                new_points.append((a[0],a[1],i))
    img_stack = stackimages.stackImages(0.7, ([img, masks[0]], [masks[1], masks[2]]))
    cv2.imshow('frame', img_stack)
    return new_points


def drawPath(points):
    for p in points:
        cv2.circle(blank,(p[0],p[1]),9,color_value[p[2]],-1)



while True:
    _, frame = vdo.read()
    blank = frame.copy()
    points = findColor(frame)
    if(len(points)!=0):
        for p in points:
            allPoints.append(p)

    if(len(allPoints)!=0):
        #pass
        drawPath(allPoints)
    cv2.imshow("contoues drawm",blank)
    cv2.waitKey(1)
