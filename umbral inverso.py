import numpy as np
import cv2
#umbral inverso
img = cv2.imread('parcial.jpeg')
nueva_imagen = np.zeros((img.shape),np.uint8)

#pasamos la imagen a grises
filas,colums,can = img.shape
for i in range(filas):
    for j in range(colums):
        r,g,b = img[i,j]
        gris = 0.299*r + 0.587*g + 0.114*b
        img[i,j] = [gris,gris,gris]

nivelGris = int(input('Ingrese el nivel de gris deseado: '))


for i in range(filas):
    for j in range(colums):
        if img.item(i,j,0)< nivelGris:
            nueva_imagen[i,j] = [255]
            continue
        nueva_imagen[i,j] = [0]

cv2.imshow('Escala de grises',img)        
cv2.imshow('umbral inverso', nueva_imagen)
cv2.waitKey(0)
cv2.destroyAllWindows()
