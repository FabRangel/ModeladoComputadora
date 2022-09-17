import cv2
import numpy as np
import matplotlib.pyplot as plt
np.seterr(over='ignore')
image = cv2.imread('milo.jpg')
k = np.zeros((600,600,3),np.uint8)
#obtener el num total de px que componen la imagen
print(image.size)
#obtener el num de filas, columnas y canales que componen la imagen
print(image.shape)
#rotando la imagen
filas,columnas,can = image.shape

for i in range(filas):
    for j in range(columnas):
        k[j][i]=image[i][j]
     
#Mostramos la imagen
cv2.imshow('Imagen original', image)        
cv2.imshow('Imagen rotada', k)
cv2.waitKey(0)
cv2.destroyAllWindows()
