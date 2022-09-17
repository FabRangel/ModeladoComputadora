from PIL import Image
import numpy as np
import cv2

#Or
#binarizado con promedio
img = cv2.imread('parcial.jpeg')
nivelGris = 128

def binarizado(img,nivelGris):
    filas,colums, can = img.shape
    nueva_imagen = np.zeros((filas,colums,1),np.uint8)
    for i in range(filas):
        for j in range(colums):
            if img.item(i,j,0)< nivelGris:
                nueva_imagen[i,j] = [0]
                continue
            nueva_imagen[i,j] = [255]

    return nueva_imagen

nueva_imagen = binarizado(img,nivelGris)
img2 = cv2.imread('parcial2.jpeg')
nueva_imagen2 = binarizado(img2,nivelGris)

Xor = np.zeros((nueva_imagen2.shape),np.uint8)
filas,colums,can = Xor.shape

#Xor
for i in range(filas):
    for j in range(colums):
        if(nueva_imagen[i,j]==[255] and nueva_imagen2[i,j]==[255]):
            Xor[i,j]=[0]
        else:
            if (nueva_imagen[i,j]==[255] or nueva_imagen2[i,j]==[255]):
                Xor[i,j]=[255]
            else:
                Xor[i,j]=[0]
        

cv2.imshow('Original_1',nueva_imagen)
cv2.imshow('Original_2',nueva_imagen2) 
cv2.imshow('Xor', Xor)
cv2.waitKey(0)
cv2.destroyAllWindows()
