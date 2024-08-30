import cv2
import numpy as np
img = cv2.imread('RGB.jpg')
cv2.imshow('Imagen original',img)
cv2.waitKey(0)
umbral_bajo = np.array([0,120,0])
umbral_alto = np.array([160,255,160])
verde = cv2.inRange(img, umbral_bajo, umbral_alto)
cv2.imwrite('dVerde.jpg', verde)
cv2.imshow('Máscara Verde', verde)
cv2.waitKey(0)
cv2.destroyAllWindows()