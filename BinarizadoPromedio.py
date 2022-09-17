from PIL import Image
import numpy as np
import cv2
#binarizado con promedio
img = cv2.imread('foto.jpeg')
nueva_imagen = np.zeros((600,600,3),np.uint8)

#pasamos la imagen a grises
filas,colums,can = img.shape
for i in range(filas):
    for j in range(colums):
        r,g,b = img[i,j]
        gris = 0.299*r + 0.587*g + 0.114*b
        img[i,j] = [gris,gris,gris]


#Promedio de gris
temp = 0
for i in range(filas):
    for j in range(colums):
        temp = img.item(i,j,0) + temp

nivelGris = temp/img.size

print(img[50,50])
#binarizamos
for i in range(filas):
    for j in range(colums):
        if img.item(i,j,0)< nivelGris:
            nueva_imagen[i,j] = [0,0,0]
            continue
    #si es mayor o igual a nivel de gris se agrega 1 en ves de 0
    #podria hacerse con 255 en ves de 1
        nueva_imagen[i,j] = [255,255,255]

cv2.imshow('Escala de grises',img)
cv2.imshow('Binarizado', nueva_imagen)
cv2.waitKey(0)
cv2.destroyAllWindows()
