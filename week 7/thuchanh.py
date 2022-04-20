# -*- coding: utf-8 -*-
"""
Created on Sat Apr  2 10:16:58 2022

@author: ngomi
"""

import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread('./img/circuit.jpg',0)

f = np.fft.fft2(img)
fshift = np.fft.fftshift(f)
magnitude_spectrum= 20*np.log(np.abs(fshift))

plt.figure(dpi=300)
plt.subplot(121)
plt.imshow(img, cmap = 'gray')
plt.title('Input Image'),
plt.xticks([]), plt.yticks([])
plt.subplot(122),
plt.imshow(magnitude_spectrum, cmap = 'gray')
plt.title('Magnitude Spectrum'),
plt.xticks([]), plt.yticks([])
plt.show()

rows, cols = img.shape
crow,ccol = rows//2 , cols//2
fshift[crow-30:crow+31, ccol-30:ccol+31] = 0
f_ishift = np.fft.ifftshift(fshift)
img_back = np.fft.ifft2(f_ishift)
img_back = np.real(img_back)

plt.figure(dpi=300)
plt.subplot(131)
plt.imshow(img, cmap = 'gray')
plt.title('Input Image')
plt.xticks([]), plt.yticks([])
plt.subplot(132)
plt.imshow(img_back, cmap = 'gray')
plt.title('Image after HPF')
plt.xticks([]), plt.yticks([])
plt.subplot(133),plt.imshow(img_back)
plt.title('Result in JET')
plt.xticks([]), plt.yticks([])
plt.show()

rows, cols = img.shape
crow,ccol = rows//2 , cols//2
# create a mask remain all zeros, center is 1,
mask = np.zeros((rows,cols,2),np.uint8)
mask[crow-30:crow+30, ccol-30:ccol+30] = 1
# apply mask and inverse DFT
dft = cv.dft(np.float32(img),flags = cv.DFT_COMPLEX_OUTPUT)
dft_shift = np.fft.fftshift(dft)
fshift = dft_shift*mask
f_ishift = np.fft.ifftshift(fshift)
img_back = cv.idft(f_ishift) 
img_back = cv.magnitude(img_back[:,:,0],img_back[:,:,1])

plt.figure(dpi=300)
plt.subplot(121),plt.imshow(img, cmap = 'gray')
plt.title('Input Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(img_back, cmap = 'gray')
plt.title('Magnitude Spectrum'),
plt.xticks([]), plt.yticks([])
plt.show()