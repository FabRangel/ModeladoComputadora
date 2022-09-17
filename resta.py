import cv2
import numpy as np
img1 = cv2.imread('parcial.jpeg')
img2 = cv2.imread('parcial2.jpeg')

def imagenGrande(img1,img2):
    if (img1.size>img2.size):
        return img1
    if (img2.size>img1.size):
        return img2
    if (img1.size==img2.size):
        return img1

img_nueva = np.zeros((imagenGrande(img1,img2).shape),np.uint8)
f,c,can = imagenGrande(img1,img2).shape

for i in range(f):
    for j in range(c):
        img_nueva[i,j] = abs(img1[i,j] - img2[i,j])

cv2.imshow('Original',img1)
cv2.imshow('Suma', img_nueva)
cv2.waitKey(0)
cv2.destroyAllWindows()
