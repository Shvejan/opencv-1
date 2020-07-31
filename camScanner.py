import requests
import cv2
import numpy as np

url = 'http://192.168.29.39:8080/shot.jpg'


def preprocess(img):
    grey = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(grey,(5,5),1)
    canney = cv2.Canny(blur,50,50)
    imdial = cv2.dilate(canney,(5,5),iterations=2)
    eroded = cv2.erode(imdial,(5,5),iterations=1)
    docpoints = getCountour(eroded)
    print(docpoints)
    if(isinstance(docpoints,int)):
        return
    warp(img,docpoints)


def getCountour(img):
    countours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    maxarea = 0
    docpoints = 0
    for cnt in countours:
        area = cv2.contourArea(cnt)
        if (area>5000):
            cv2.drawContours(blank, cnt, -1, (255, 0, 0), 3)
            perimetre = cv2.arcLength(cnt, True)
            allPoints = cv2.approxPolyDP(cnt, 0.04 * perimetre, True)
            if(len(allPoints)==4 and maxarea < area):
                docpoints = allPoints
                maxarea = area
    #cv2.drawContours(blank, docpoints, -1, (255, 0, 0), 3)
    cv2.imshow('op',blank)

    return docpoints


def srt(points):
    points  = points.reshape((4,2))
    sorted = np.zeros((4,1,2),np.int32)
    add = points.sum(1)

    sorted[0]=points[np.argmin(add)]
    sorted[3]=points[np.argmax(add)]
    diff = np.diff(points,axis=1)
    sorted[1] = points[np.argmin(diff)]
    sorted[2] = points[np.argmax(diff)]
    return sorted



def warp(img,docpoints):
    w, h = 360,480
    points = np.float32(srt(docpoints))
    points2 = np.float32([[0, 0], [w, 0], [0, h], [w, h]])

    matrix = cv2.getPerspectiveTransform(points, points2)
    op = cv2.warpPerspective(img, matrix, (w, h))
    cv2.imshow('warpp',op)






while True:

    imgResp = requests.get(url)
    imgNp = np.array(bytearray(imgResp.content), dtype=np.uint8)
    img = cv2.imdecode(imgNp, -1)
    img = cv2.resize(img,(480,270))
    blank = img.copy()
    preprocess(img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
