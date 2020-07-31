import cv2

faceCascade = cv2.CascadeClassifier('haarcascades/haarcascade_frontalface_default.xml')
eyeCascade = cv2.CascadeClassifier('haarcascades/haarcascade_eye.xml')
video = cv2.VideoCapture(0)

while True:
    _, frame = video.read()
    grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(frame, 1.1, 4)
    eyes = eyeCascade.detectMultiScale(frame,3,5)
    for (x, y, w, h) in faces:
        cv2.rectangle(grey, (x, y), (x + w, y + h), (0, 0, 0), 3)
        print(x,y)

    for (x, y, w, h) in eyes:
        cv2.rectangle(grey, (x, y), (x + w, y + h), (0, 0, 0), 3)
        print(x,y)

    cv2.imshow('grey', grey)
    cv2.waitKey(1)
