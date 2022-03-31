# -*- coding: utf-8 -*-
"""
Created on Sat Mar 26 08:51:18 2022

@author: ngomi
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage import convolve
plt.rcParams.update({'font.size': 5})
def Conv(img,k):
    Input=np.array(img,dtype='single')
    if Input.ndim >2:
        Out=np.zeros_like(Input)
        for i in range(3):
            Out[:,:,i]=np.convolve(Input[:,:,i],k)
    else:
        Out=convolve(Input,k)
    return Out

#%% Sobel 
img = cv2.imread('img/circuit.jpg', cv2.IMREAD_GRAYSCALE)
ky=np.array([[-1.0,-2,-1],[0,0,0],[1,2,1]])
kx=np.transpose(ky)
Gx=Conv(img,kx)
Gy=Conv(img,ky)
Gm=np.sqrt(Gx**2+Gy**2)

plt.figure(dpi=300)
subf=plt.subplot(2,2,1); subf.set_title("Orignal image")
plt.imshow(img,cmap='gray'); plt.axis('off') ;
subf=plt.subplot(2,2,2); subf.set_title("Gx")
plt.imshow(Gx,cmap='gray'); plt.axis('off')
subf=plt.subplot(2,2,3); subf.set_title("Gy")
plt.imshow(Gy,cmap='gray'); plt.axis('off')
subf=plt.subplot(2,2,4); subf.set_title("Sobel filter")
plt.imshow(Gm,cmap='gray'); plt.axis('off')
plt.show()

Out=Gm>130
plt.figure(dpi=300)
plt.imshow(Out,cmap='gray'); plt.axis('off')
plt.title("Egde filter"); plt.show()

#%% Laplacian
scale = 0.3 # percent of original size
width = int(img.shape[1] * scale)
height = int(img.shape[0] * scale)
dim = (width, height)
# resize image
img = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)

ksize = (11,11)
img = cv2.blur(img, ksize, cv2.BORDER_DEFAULT)
plt.figure(dpi=300)
subf=plt.subplot(2,2,1); subf.set_title("Orignal image")
plt.imshow(img,cmap='gray'); plt.axis('off') ;
# Tạo các kernal k1 4 hướng và k2 8 hướng
k1=np.array([[0,1,0],[1,-4,1],[0,1,0]])
k2=np.array([[1,1,1],[1,-8,1],[1,1,1]])

L1=Conv(img,k1)
subf=plt.subplot(2,2,2); subf.set_title("Laplacian with k1")
plt.imshow(L1,cmap='gray'); plt.axis('off')

L2=Conv(img,-k1)+img
subf=plt.subplot(2,2,3); subf.set_title("sharpening (Laplacian neg kernel)")
plt.imshow(L2,cmap='gray'); plt.axis('off') ;

L3=Conv(img,k2)+img
subf=plt.subplot(2,2,4); subf.set_title("sharpening (Laplacian k2)")
plt.imshow(L3,cmap='gray'); plt.axis('off') ;