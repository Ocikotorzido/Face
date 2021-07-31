from cv2 import cv2
import numpy as np

valorGauss=3
valorKernel=3

path = r'C:\Users\nanel\OneDrive\Escritorio\RF\monedascontorno\monedas.jpg'
imagen=cv2.imread(path)
gris=cv2.cvtColor(imagen,cv2.COLOR_BGR2GRAY)

# desenfoque gaussiano, par eliminar ruido de imagenes
gauss = cv2.GaussianBlur(gris,(valorGauss,valorKernel),0)

# mostrar resultado

cv2.imshow('grises',gris)
cv2.imshow('guss',gauss)
cv2.waitKey(0)
cv2.destroyAllWindows()