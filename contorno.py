from cv2 import cv2

# es posible que el openCV no tome bien la ruta es por eso que la ingresamos manual con un path
path = r'C:\Users\nanel\OneDrive\Escritorio\RF\monedascontorno\contorno.jpg'
imagen=cv2.imread(path)

# convertimos la imagen a blanco y negro
gris=cv2.cvtColor(imagen,cv2.COLOR_BGR2GRAY)

# el codigo a continuacion muestra la imagen
cv2.imshow('imagen',gris)

#esto evita que se cierre de inmediato
cv2.waitKey(0)
cv2.destroyAllWindows()