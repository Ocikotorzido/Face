import cv2 as cv 
capturaVideo=cv.VideoCapture(1)
if not capturaVideo.isOpened():
    print('no se encuentra una camara')
    exit()

while True:
    tipocamara,camara=capturaVideo.read()
    gris= cv.cvtColor(camara, cv.COLOR_BGR2GRAY)

    cv.imshow("Camara",gris)

    # si lo siguiente no esta se quedara en bucle y no podras detener hasta reiniciar el pc
    if cv.waitKey(1)==ord("q"):
        break

capturaVideo.release()
cv.destroyAllWindows()