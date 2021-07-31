from cv2 import cv2

# es posible que el openCV no tome bien la ruta es por eso que la ingresamos manual con un path
path = r'C:\Users\nanel\OneDrive\Escritorio\RF\monedascontorno\contorno.jpg'
imagen=cv2.imread(path)

# convertimos la imagen a blanco y negro
gris=cv2.cvtColor(imagen,cv2.COLOR_BGR2GRAY)

# en este punto se genera un error ya que el threshold genera 2 salidas es por eso 
#que se debe usar una funcion _, o puede agregarse un segundo parametro para recibir el otro valor (otro, umbral)
# el otro valor nos devuelve el valor del umbral
_,umbral=cv2.threshold(gris,100,255,cv2.THRESH_BINARY)

# contorno y jerarquia, marcado de contorno y funcion de findContours
contorno,jerarquia = cv2.findContours(umbral,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)


# el codigo a continuacion muestra la imagen
cv2.imshow('imagen',umbral)
cv2.imshow('imagen2',gris)

#esto evita que se cierre de inmediato
cv2.waitKey(0)
cv2.destroyAllWindows()