from cv2 import cv2
import numpy as np

valorGauss=3
valorKernel=3

path = r'C:\Users\nanel\OneDrive\Escritorio\RF\monedascontorno\monedas.jpg'
imagen=cv2.imread(path)
gris=cv2.cvtColor(imagen,cv2.COLOR_BGR2GRAY)

# desenfoque gaussiano, para eliminar ruido de imagenes
gauss = cv2.GaussianBlur(gris,(valorGauss,valorKernel),0)

# segundo desenfoque de ruido
canny=cv2.Canny(gauss,60,100)

# 
kernel = np.ones((valorKernel,valorKernel),np.uint8)
cierre = cv2.morphologyEx(canny,cv2.MORPH_CLOSE,kernel)
contorno, jerarquia=cv2.findContours(cierre.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)


print("monedas encontradas: {}".format(len(contorno)))

# mostrar resultado
cv2.imshow('grises',gris)
cv2.imshow('guss',gauss)
cv2.imshow('canny',canny)
cv2.imshow('cierre',cierre)

cv2.waitKey(0)
cv2.destroyAllWindows()