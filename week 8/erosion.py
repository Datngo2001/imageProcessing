# -*- coding: utf-8 -*-
"""
Created on Sat Apr  9 07:54:15 2022

@author: ngomi
"""

import cv2 as cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('./images/F95.png', 0)
threshval = 100; n = 255
retval, imB = cv2.threshold(img, threshval, n, cv2.THRESH_BINARY)

kernel1 = np.ones((11,11), np.uint8)
kernel2 = np.ones((15,15), np.uint8)
kernel3 = np.ones((45,45), np.uint8)
img_ero1 = cv2.erode(imB, kernel1, iterations=1)
img_ero2 = cv2.erode(imB, kernel2, iterations=1)
img_ero3 = cv2.erode(imB, kernel3, iterations=1)

plt.subplot(2,2,1),plt.axis('off')
plt.imshow(imB,cmap=plt.cm.gray)
plt.subplot(2,2,2),plt.axis('off')
plt.imshow(img_ero1,cmap=plt.cm.gray)
plt.subplot(2,2,3),plt.axis('off')
plt.imshow(img_ero2,cmap=plt.cm.gray)
plt.subplot(2,2,4),plt.axis('off')
plt.imshow(img_ero3,cmap=plt.cm.gray)