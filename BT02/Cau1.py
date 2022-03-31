# -*- coding: utf-8 -*-
"""
Created on Wed Mar 30 21:11:06 2022

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

img = cv2.imread('img/circuit.jpg', cv2.IMREAD_COLOR)
img= cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
plt.figure(dpi=300)
subf=plt.subplot(1,2,1); plt.imshow(img)
plt.axis('off'); subf.set_title("Orignal image")

#%% Cau 1a: Log tranform, power law tranform, Piecewise-Linear tranform
c = 255 / np.log(1 + np.max(img))
log_image = c * (np.log(1+img))
log_image = np.array(log_image, dtype = np.uint8)
plt.figure(dpi=300)
subf=plt.subplot(1,2,1); plt.imshow(log_image)
plt.axis('off'); subf.set_title("Log Transform")

gamma = 0.4
power_image = np.array(255*(img / 255) ** gamma, dtype = 'uint8')
plt.figure(dpi=300)
subf=plt.subplot(1,2,1); plt.imshow(power_image)
plt.axis('off'); subf.set_title("Power Transform")

def pixelVal(pix, r1, s1, r2, s2):
    if (0 <= pix and pix <= r1):
        return (s1 / r1)*pix
    elif (r1 < pix and pix <= r2):
        return ((s2 - s1)/(r2 - r1)) * (pix - r1) + s1
    else:
        return ((255 - s2)/(255 - r2)) * (pix - r2) + s2
  
# Define parameters.
r1 = 70
s1 = 0
r2 = 140
s2 = 255
  
pixelVal_vec = np.vectorize(pixelVal)
contrast_stretched = pixelVal_vec(img, r1, s1, r2, s2)
plt.figure(dpi=300)
subf=plt.subplot(1,2,1); plt.imshow(contrast_stretched)
plt.axis('off'); subf.set_title("Piecewise-Linear tranform")

#%% Histogram equalization
i = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
img_gray = cv2.cvtColor(i, cv2.COLOR_BGR2GRAY)
equ = cv2.equalizeHist(img_gray)

plt.figure(dpi=300)
subf=plt.subplot(1,2,1); plt.imshow(equ)
plt.axis('off'); subf.set_title("Piecewise-Linear tranform")

#%% Rotation with bilinear interpolation and nearest interpolation

rolateDegree = 15
scale = 1.0
(h, w) = img.shape[:2]
center = (w / 2, h / 2)

M = cv2.getRotationMatrix2D(center, rolateDegree, scale)
rotated1 = cv2.warpAffine(img, M, (w, h))

plt.figure(dpi=300)
subf=plt.subplot(1,2,1); plt.imshow(rotated1)
plt.axis('off'); subf.set_title("Bilinear Interpolation")

rotated2 = cv2.warpAffine(img, M, (w, h), flags = cv2.INTER_NEAREST)

plt.figure(dpi=300)
subf=plt.subplot(1,2,1); plt.imshow(rotated2)
plt.axis('off'); subf.set_title("Nearest Interpolation")

