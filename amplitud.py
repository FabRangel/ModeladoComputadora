import numpy as np
import cv2
#Resolución
img = cv2.imread('parcial.jpeg')
nueva_imagen = np.zeros((img.shape),np.uint8)

amplitud = int(input('Cuántos bits requiere: '))
#pasamos la imagen a grises
filas,colums,can = img.shape
for i in range(filas):
    for j in range(colums):
        r,g,b = img[i,j]
        gris = 0.299*r + 0.587*g + 0.114*b
        img[i,j] = [gris,gris,gris]

canBits = 256/(2**amplitud)
cont = 0
colores = 2**amplitud

for i in range(filas):
    for j in range(colums):
        for b in range(0,255,colores):
            if(img[i,j,0]<= colores):
                img[i,j] = [cont]
        cont = cont + colores
            

cv2.imshow('Escala de grises',img)        
cv2.waitKey(0)
cv2.destroyAllWindows()
