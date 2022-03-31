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

#%% Mean
img = cv2.imread('img/circuit.jpg', cv2.IMREAD_COLOR)
img= cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
plt.figure(dpi=300)
subf=plt.subplot(1,2,1); plt.imshow(img)
plt.axis('off'); subf.set_title("Orignal image")

k=np.ones((7,7))/(7*7)
imgOut=Conv(img,k)
subf=plt.subplot(1,2,2); plt.imshow(imgOut)
plt.axis('off'); subf.title.set_text('Mean filter')
plt.show()


#%% LỌC Gaussian
s=7;sig=3;
k=Gausskernel(s, sig)
imgOut=Conv(img,k)

plt.figure(dpi=300)
subf=plt.subplot(1,2,2); plt.imshow(imgOut)
plt.axis('off'); subf.title.set_text('Gaussian filter')
plt.show()

#%% LỌC Median

def median_filter(data, filter_size):
    temp = []
    indexer = filter_size // 2
    data_final = []
    data_final = np.zeros((len(data),len(data[0])))
    for i in range(len(data)):

        for j in range(len(data[0])):

            for z in range(filter_size):
                if i + z - indexer < 0 or i + z - indexer > len(data) - 1:
                    for c in range(filter_size):
                        temp.append(0)
                else:
                    if j + z - indexer < 0 or j + indexer > len(data[0]) - 1:
                        temp.append(0)
                    else:
                        for k in range(filter_size):
                            temp.append(data[i + z - indexer][j + k - indexer])

            temp.sort()
            data_final[i][j] = temp[len(temp) // 2]
            temp = []
    return data_final

img = cv2.imread('img/circuit.jpg', cv2.IMREAD_GRAYSCALE)
imgOut = median_filter(img, 7)
plt.figure(dpi=300)
subf=plt.subplot(1,2,2); plt.imshow(imgOut)
plt.axis('off'); subf.title.set_text('Median filter')
plt.show()

