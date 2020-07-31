import cv2
import numpy as np
img=cv2.imread('./resources/card.jpg')
w,h = 500,600
points = np.float32([[113,211],[30,142],[211,97],[126,34]])
points2 = np.float32([[0,0],[w,0],[0,h],[w,h]])

matrix = cv2.getPerspectiveTransform(points,points2)
op = cv2.warpPerspective(img,matrix,(w,h))
cv2.line(img,(0,h),(w,h),(0,0,0))
cv2.line(img,(w,0),(w,h),(200,0,0))

cv2.circle(img,(126,34),3,(0,0,0),-1)
cv2.circle(img,(30,142),3,(0,0,222),-1)
cv2.circle(img,(211,97),3,(0,0,0),-1)
cv2.circle(img,(113,211),3,(1,1,1),-1)


cv2.imshow('frame',op)
cv2.imshow('img',img)

cv2.waitKey(0)