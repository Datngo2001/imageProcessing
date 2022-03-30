# -*- coding: utf-8 -*-
"""
Created on Sat Mar 12 10:16:20 2022

@author: ngomi
"""

#from cv2 import *
import cv2
import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage import convolve
plt.rcParams.update({'font.size': 5})
pathIn='Images//'
pathOut='Ouputs//'
#%% GAUSSIAN FILTER
def Gausskernel(l=5, sig=1.5):
    s=round((l - 1)/2)
    ax = np.linspace(-s, s, l)
    gauss = np.exp(-np.square(ax) / (2*np.square(sig)))
    kernel = np.outer(gauss, gauss) #Compute the outer product of two vectors.
    return kernel# / np.sum(kernel)
def Conv(img,k):
    Out=img
    if img.ndim >2:
        for i in range(3):
           Out[:,:,i]=convolve(img[:,:,i],k)
    else:
        Out=convolve(img,k)
    return Out


img = cv2.imread(pathIn+'AT3_1m4_08.tif', cv2.IMREAD_COLOR)
img= cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
#img = cv2.imread(pathIn+'lenna.jpg', cv2.IMREAD_GRAYSCALE)
#%%
s=21;sig=1.2;
k=Gausskernel(s, sig)
imgG=Conv(img,k)
plt.imshow(imgG)
plt.axis('off')