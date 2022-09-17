import numpy as np
from matplotlib import pyplot as plt
import cv2

img = cv2.imread('parcial1.jpeg')
f,c,can = img.shape
colorOrig = 0
suma = 0
altura = np.zeros((256,))
arregloSuma = np.zeros((256,))
#Pasamos la imagen a grises
def escalaGris(img,f,c):
    grises = np.zeros((f,c,1),np.uint8)
    for i in range(f):
        for j in range(c):
            r,g,b = img[i,j]
            gris = 0.299*r + 0.587*g + 0.114*b
            grises[i,j] = [gris]
    return grises

gris = escalaGris(img,f,c)

#Creamos el histograma
colores=256
for i in range(f):
    for j in range(c):
        color = img[i,j]
        altura[color] = altura[color]+1
    plt.plot(range(colores),altura[0:colores])
    
cons = 255/(f*c)
res = np.zeros((f,c,1),np.uint8)
for i in range(f):
    for j in range(c):
        for h in range(gris[i,j,0]):
            suma = suma + altura[h]
            k = cons*suma
        res[i,j] = [k]
        suma = 0
        

cv2.imshow('Escala Grises', gris)
cv2.imshow('Ecualizacion',res)
cv2.waitKey(0)
cv2.destroyAllWindows()
