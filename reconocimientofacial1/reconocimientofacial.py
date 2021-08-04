import cv2 as cv
import numpy as np
import os

id=0

modelo='fotosElon'
ruta1='C:/Users/nanel/OneDrive/Escritorio/RF/monedascontorno/reconocimientofacial1'
rutacompleta= ruta1 + '/' + modelo
if not os.path.exists(rutacompleta):
    os.makedirs(rutacompleta)





path = r'C:\Users\nanel\OneDrive\Escritorio\RF\monedascontorno\reconocimientofacial1\haarcascade_frontalface_default.xml'
ruidos=cv.CascadeClassifier(path)
camara=cv.VideoCapture(r'C:\Users\nanel\OneDrive\Escritorio\RF\monedascontorno\reconocimientofacial1\ElonMusk.mp4')

while True:
    respuesta,captura=camara.read()
    if respuesta==False:break
    
    gris = cv.cvtColor(captura,cv.COLOR_BGR2GRAY)
    
    idcaptura=captura.copy()


    cara=ruidos.detectMultiScale(gris,1.3,5)
    for(x,y,e1,e2) in cara:
        cv.rectangle(captura, (x,y), (x+e1,y+e2),(0,255,0),3)
        rostrocapturado=idcaptura[y:y+e1,x:x+e2]
        rostrocapturado=cv.resize(rostrocapturado,(160,160),interpolation=cv.INTER_CUBIC)
        cv.imwrite(rutacompleta + '/imagen_{}.jpg'.format(id),rostrocapturado)
        id=id+1

    cv.imshow("Resultado",captura)

    if id==101:
        break

camara.release()
cv.destroyAllWindows()