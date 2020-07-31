import cv2
import numpy as np

img = np.zeros((500, 500, 3)    , np.uint8)
cv2.line(img,(0,0),(500,500),(255,255,255))
cv2.rectangle(img,(20,20),(90,90),(0,44,88),-4)
cv2.circle(img,(200,200),100,(200,200,1),-1)
cv2.putText(img,'heyaaa',(300,350),cv2.FONT_HERSHEY_COMPLEX,1,(30,40,90),4)
cv2.imshow('frame', img)
cv2.waitKey(0)
