import cv2

vdo = cv2.VideoCapture(0)
vdo.set(3,640)
vdo.set(4,480)
while True:

    _, img = vdo.read()
    cv2.imshow('image', img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
