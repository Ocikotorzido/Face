from cv2 import cv2
import numpy as np

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