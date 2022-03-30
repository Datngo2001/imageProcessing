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
#%% LỌC TRUNG BÌNH với kernel 11x11
img = cv2.imread('img/dog.jpg', cv2.IMREAD_COLOR)
img= cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
plt.figure(dpi=300)
subf=plt.subplot(1,2,1); plt.imshow(img)
plt.axis('off'); subf.set_title("Orignal image")

k=np.ones((11,11))/(11*11)
imgOut=Conv(img,k)
subf=plt.subplot(1,2,2); plt.imshow(imgOut)
plt.axis('off'); subf.title.set_text('Mean filter')
plt.show()
#%% LỌC Gaussian với kernel 11x11 và sig=3
img = cv2.imread('img/dog.jpg', cv2.IMREAD_COLOR)
img= cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
plt.figure(dpi=300)
subf=plt.subplot(1,2,1); plt.imshow(img)
plt.axis('off'); subf.set_title("Orignal image")
s=11;sig=3;
k=Gausskernel(s, sig)
imgOut=Conv(img,k)
subf=plt.subplot(1,2,2); plt.imshow(imgOut)
plt.axis('off'); subf.title.set_text('Gaussian filter')
plt.show()

#%% LỌC Gaussian với kernel kích thước khác nhau và sigmal khác nhau
img = cv2.imread('img/dog.jpg', cv2.IMREAD_COLOR)
img= cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
GauSig= np.linspace(1,4,5,endpoint=True)
ks= np.linspace(1,10,5,endpoint=True,dtype=int)*2+1
plt.figure(dpi=300)
subf=plt.subplot(2,3,1)
subf.imshow(img)
plt.axis('off'); subf.set_title("Orignal image")
for i,sig in enumerate(GauSig):
    k=Gausskernel(ks[i], sig)
    imgG=Conv(img,k)
    subf=plt.subplot(2,3,i+2)
    subf.imshow(imgG)
    subf.set_title('Gaussian(s='+str(ks[i])+'; sig='+ str(sig)[0:3]+')');
    subf.axis('off')
