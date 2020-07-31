import cv2
import numpy as np
import stackimages


def getCountour(img):
    countours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    for cnt in countours:
        area = cv2.contourArea(cnt)
        print(area)
        if (area>500):
            cv2.drawContours(blank, cnt, -1, (255, 0, 0), 3)
            perimetre = cv2.arcLength(cnt, True)
            # print(perimetre)
            allPoints = cv2.approxPolyDP(cnt, 0.04 * perimetre, True)
            print(len(allPoints))
            x, y, w, h = cv2.boundingRect(allPoints)

            if (len(allPoints) == 4):
                asp = w/float(h)
                if asp >=1 and asp<=1.02 :
                    objType = "sq"

                else:
                    objType = "rec"
            else:
                objType = str(len(allPoints))
            cv2.rectangle(blank, (x, y), (x + w, y + h), (0, 255, 0), 5)
            cv2.putText(blank, objType, (x + w // 2 - 10, y + h // 2 - 10), cv2.FONT_HERSHEY_COMPLEX, 2, (225, 225, 225))


originalImg = cv2.imread('./resources/shapes.png')
grey = cv2.cvtColor(originalImg, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(grey, (7, 7), 1)
canny = cv2.Canny(blur, 50, 50)
blank = np.zeros_like(originalImg)

getCountour(canny)

img_stack = stackimages.stackImages(0.7, ([originalImg, grey, blur], [canny, blank, blank]))

cv2.imshow('stack', img_stack)
cv2.waitKey(0)
