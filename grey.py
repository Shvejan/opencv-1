import cv2
import numpy as np

img = cv2.imread('./resources/img.jpg')

grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blurImg = cv2.GaussianBlur(grey, (7, 7), 0)
canny = cv2.Canny(img, 200, 150)
outline = cv2.dilate(canny, np.ones((5, 5), np.uint8), iterations=1)
erode = cv2.erode(outline, np.ones((5, 5), np.uint8), iterations=1)

cropped = img[0:500, 500:800]
cv2.imshow('grey', cropped)
print(img.shape)

cv2.waitKey(0)
