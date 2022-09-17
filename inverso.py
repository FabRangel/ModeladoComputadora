import numpy as np
import cv2
#Operadores básicos
#Operador inverso o negativo
img = cv2.imread('parcial.jpeg')
nueva_imagen = np.zeros((img.shape),np.uint8)

#copiamos la imagen
filas,colums,can = img.shape
for i in range(filas):
    for j in range(colums):
        nueva_imagen[i,j] = img[i,j]


#q(x,y) = 255-p(x,y)
for i in range(filas):
    for j in range(colums):
        R,G,B=img[i,j]
        nueva_imagen[i,j,0] = 255 - R
        nueva_imagen[i,j,1] = 255 - G
        nueva_imagen[i,j,2] = 255 - B


cv2.imshow('Original',img)
cv2.imshow('Negativo', nueva_imagen)
cv2.waitKey(0)
cv2.destroyAllWindows()
