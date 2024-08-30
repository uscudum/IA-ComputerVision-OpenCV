import cv2
import numpy as np
umbral_bajo = np.array([0,120,0])
umbral_alto = np.array([120,255,120])
cap = cv2.VideoCapture(0)

while True:
  ret, frame = cap.read()
  if ret==True:
    mask_verde = cv2.inRange(frame, umbral_bajo, umbral_alto)
    verde = cv2.bitwise_and(frame, frame, mask=mask_verde)
    cv2.imshow('Detección del verde', verde)
    cv2.imshow('Original', frame)
    if cv2.waitKey(1) & 0xFF == ord('s'):
        break
cap.relase()
cv2.destroyAllWindows()
