from cv2 import cv2
import numpy as np
from numpy.core.records import array

def ordenarpuntos(puntos):
    n_puntos=np.concatenate(puntos[0],puntos[1],puntos[2],puntos[3]).tolist()
    # este toma el punto 0
    Y = sorted(n_puntos,key=lambda n_puntos:n_puntos[1])
    # este busca el punto 1
    X = Y[0:2]
    # este toma el punto 2
    X = sorted(X,key=lambda X:X[0])
    # aqui toma los 2 restantes
    X2 = Y[2:4]
    X2 = sorted(X2,key=lambda X2:X2[0])
    # con esto retornamos de forma ordenada los puntos
    return [X[0],X[1],X2[0],X2[1]]

def alineamiento(imagen,ancho,alto):
    imagen_alineada= None
    gris = cv2.cvtColor(imagen,cv2.COLOR_BGR2GRAY)
    tipoUmbral,umbral=cv2.threshold(gris,150,255,cv2.THRESH_BINARY)
    cv2.imshow("Umbral",umbral)

    # esto requiere la imagen umbralizada (findcontours) esto devuelve los puntos desordenados
    contorno,jerarquia = cv2.findContours(umbral,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)[0]

    # ordenamos los contornos -- reverse True ordena de menor a mayor
    contorno=sorted(contorno,key=cv2.contourArea,reverse=True)[:1]

    for c in contorno:
        epsilon = 0.01*cv2.arcLength(c,True)
        # esto requiere un parametro de proximado
        approx=cv2.approxPolyDP(c, epsilon,True)
        if len(approx)==4:
            puntos=ordenarpuntos(approx)
            puntos1=np.float32(puntos)
            puntos2=np.float32([[0,0],[ancho,0],[0,alto],[ancho,alto]])
            # si giras la camara no pasara nada
            M = cv2.getPerspectiveTransform(puntos1,puntos2)
            imagen_alineada=cv2.warpPerspective(imagen,M,(ancho,alto))

    return imagen_alineada

capturaVideo=cv2.VideoCapture(0)

while True:
    tipocamara,camara=capturaVideo.read()
    if tipocamara==False:
        break
    imagen_A6=alineamiento(camara,ancho=480,alto=677)
    if imagen_A6 is not None:
        puntos=[]
        gris=cv2.cvtColor(imagen_A6,cv2.COLOR_BGR2GRAY)
        blur=cv2.GaussianBlur(gris,(5,5),1)
        _,umbral2=cv2.threshold(blur,0,255,cv2.THRESH_OTSU+cv2.THRESH_BINARY_INV)
        cv2.imshow("umbral",umbral2)
        contorno2,jerarquia2=cv2.findContours(umbral2,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)[0]

        cv2.drawContours(imagen_A6,contorno2,-1,(255,0,0),2)
        suma1=0.0
        suma2=0.0

        for c2 in contorno2:
            area=cv2.contourArea(c2)
            Momentos = cv2.moments(c2)
            if(Momentos["m00"]==0):
                Momentos["m00"]=1.0
            x=int(Momentos["m10"]/Momentos["m00"])
            y=int(Momentos["m01"]/Momentos["m00"])

            if area<9500 and area>9000:
                font=cv2.FONT_HERSHEY_SIMPLEX
                cv2.putText(imagen_A6,"Moneda de 100",(x,y),font,0.75,(0,255,0),2)
                suma1=suma1+1.0

            if area<9600 and area>11000:
                font=cv2.FONT_HERSHEY_SIMPLEX
                cv2.putText(imagen_A6,"Moneda de 50",(x,y),font,0.75,(0,255,0),2)
                suma1=suma1+0.5

        total=suma1+suma2
        print("sumatoria total en pesos:",round(total,2))
        cv2.imshow("Imagen A6",imagen_A6)
        cv2.imshow("umbral",camara)

    if cv2.waitKey(1) == ord('q'):
        break

capturaVideo.release()
cv2.destroyAllWindows()