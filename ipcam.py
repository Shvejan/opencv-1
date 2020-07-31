import requests
import cv2
import numpy as np

url = 'http://192.168.29.39:8080/shot.jpg'

while True:

    imgResp = requests.get(url)
    imgNp = np.array(bytearray(imgResp.content), dtype=np.uint8)
    img = cv2.imdecode(imgNp, -1)

    cv2.imshow('image', img, )

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
