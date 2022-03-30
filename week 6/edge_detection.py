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
#%%Lọc Sobel theo 2 hướng x và y sau đó tính tổng độ lớn theo x và y
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

Out=Gm>130 # Thiết lập ngưỡng đơn lọc edge candidate
plt.imshow(Out,cmap='gray'); plt.axis('off')
plt.title("Egde filter"); plt.show()