# -*- coding: utf-8 -*-
"""
Created on Sat Mar 26 08:19:54 2022

@author: ngomi
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage import convolve
plt.rcParams.update({'font.size': 5})
#Hàm convolution cho ảnh không gian với ảnh gray hoặc ảnh màu 3 lớp (RGB)
def Conv(img,k):
    Out=np.zeros_like(img)
    if img.ndim >2:
        for i in range(3):
            Out[:,:,i]=convolve(img[:,:,i],k)
    else:
        Out=convolve(img,k)
    return Out
#%% GAUSSIAN Kernel
def Gausskernel(l=5, sig=1.5):
    s=round((l - 1)/2)
    ax = np.linspace(-s, s, l)
    gauss = np.exp(-np.square(ax) / (2*(sig**2)))
    kernel = np.outer(gauss, gauss)
    #tính tích the outer product of two vectors.
    return kernel / np.sum(kernel)
#%% LỌC TRUNG vị với kernel 9x9
img = cv2.imread('img/dog.jpg', cv2.IMREAD_GRAYSCALE)
plt.figure(dpi=300)
subf=plt.subplot(1,2,1); plt.imshow(img)
plt.axis('off'); subf.set_title("Orignal image")

temp = [0, 0, 0, 0, 0, 0, 0, 0, 0]
pixel = 0
for i in range(0, img.shape[0] - 1):
    for j in range(0, img.shape[1] - 1):
        temp[0] = img[i-1][j-1]
        temp[1] = img[i-1][j]
        temp[2] = img[i-1][j+1]
        temp[3] = img[i][j-1]
        temp[4] = img[i][j]
        temp[5] = img[i][j+1]
        temp[6] = img[i+1][j-1]
        temp[8] = img[i+1][j]
        
        temp.sort()
        
        trungvi = round(len(temp)/2)
                
        pixel = temp[trungvi]
        
        img[i][j] = pixel      
        

subf=plt.subplot(1,2,2); plt.imshow(img)
plt.axis('off'); subf.title.set_text('Mean filter')
plt.show()
