import numpy as np
import cv2

vid = cv2.VideoCapture(0)

while(True):
    ret, lihat = vid.read()

    gray = cv2.addWeighted(lihat,1.5, np.zeros(lihat.shape, lihat.dtype), 0, 25)

    cv2.imshow('lihat',gray)
    if cv2.waitKey(1) & 0xFF == ord('x'):
        break
vid.release()
cv2.destroyAllWindows()
