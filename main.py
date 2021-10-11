import cv2
import numpy as np

camera = cv2.VideoCapture(0)

eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

while True:
    ret, frame = camera.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    eyes = eye_cascade.detectMultiScale(gray, 1.2, 5, minSize=(15, 15), flags=cv2.CASCADE_SCALE_IMAGE)

    for (x, y, w, h) in eyes:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (240, 211, 34), 2)

    cv2.imshow('Video Frame', frame)
    if cv2.waitKey(1) == ord('q'):
        break


camera.release()
cv2.destroyAllWindows()