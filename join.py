import cv2
import numpy as np

img=cv2.imread('./resources/card.jpg')
img2=cv2.imread('./resources/img.jpg')
imm = np.hstack((img,img))
cv2.imshow("adff",imm)
cv2.waitKey(0)