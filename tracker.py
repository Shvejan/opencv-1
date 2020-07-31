import cv2
import numpy as np

def empty(a):
    pass

img=cv2.imread('./resources/car2.jpg')
cv2.namedWindow('tracker')
cv2.resizeWindow('tracker',640,280)

cv2.createTrackbar("Hue min",'tracker',1,179,empty)
cv2.createTrackbar("Hue max",'tracker',155,179,empty)
cv2.createTrackbar("sat min",'tracker',4,255,empty)
cv2.createTrackbar("sat max",'tracker',212,255,empty)
cv2.createTrackbar("val min",'tracker',20,255,empty)
cv2.createTrackbar("val max",'tracker',215,255,empty)

hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

while True:

    # cv2.imshow('original',hsv)
    hmin = cv2.getTrackbarPos("Hue min",'tracker')
    hmax = cv2.getTrackbarPos("Hue max",'tracker')
    smin = cv2.getTrackbarPos("sat min",'tracker')
    smax = cv2.getTrackbarPos("sat max",'tracker')
    vmin = cv2.getTrackbarPos("val min",'tracker')
    vmax = cv2.getTrackbarPos("val max",'tracker')
    print(hmin,hmax,smin,smax,vmin,vmax)
    mask = cv2.inRange(hsv,(hmin,smin,vmin),(hmax,smax,vmax))
    cv2.imshow('mask',mask)
    final=cv2.bitwise_and(img,img,mask=mask)
    cv2.imshow('final',final)

    cv2.waitKey(1)