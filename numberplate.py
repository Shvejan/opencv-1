import requests
import cv2
import numpy as np

url = 'http://192.168.29.39:8080/shot.jpg'
numberplate = cv2.CascadeClassifier('haarcascades/haarcascade_russian_plate_number.xml')

while True:

    imgResp = requests.get(url)
    imgNp = np.array(bytearray(imgResp.content), dtype=np.uint8)
    img = cv2.imdecode(imgNp, -1)
    img = cv2.resize(img, (480, 270))
    points = numberplate.detectMultiScale(img,1.1,4)
    for x,y,w,h in points:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),5)
        rio = img[y:y+h,x:x+w]
        cv2.imshow('roi',rio)
    cv2.imshow('image', img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
