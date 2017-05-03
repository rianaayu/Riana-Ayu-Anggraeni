import numpy as np
import cv2

vid = cv2.VideoCapture(0)

while(True):
    ret, lihat = vid.read()

    gray = cv2.cvtColor(lihat, cv2.COLOR_BGR2GRAY)

    cv2.imshow('lihat',255-gray)
    if cv2.waitKey(1) & 0xFF == ord('x'):
        break
vid.release()
cv2.destroyAllWindows()
