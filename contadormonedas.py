from cv2 import cv2
import numpy as np

path = r'C:\Users\nanel\OneDrive\Escritorio\RF\monedascontorno\monedas.jpg'
imagen=cv2.imread(path)
gris=cv2.cvtColor(imagen,cv2.COLOR_BGR2GRAY)

# mostrar resultado

cv2.imshow('grises',gris)
cv2.waitKey(0)
cv2.destroyAllWindows()