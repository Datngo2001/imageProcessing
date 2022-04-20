# -*- coding: utf-8 -*-
"""
Created on Wed Apr 20 16:17:04 2022

@author: ngomi
"""

import cv2 as cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('./images/cau1.png', 0)
img = 255 - img
threshval = 100; n = 255
retval, imB = cv2.threshold(img, threshval, n, cv2.THRESH_BINARY)

kernel = np.ones((3,3), np.uint8)
kernel[0][0] = 1
kernel[1][1] = 1
kernel[2][2] = 1

erode = cv2.erode(imB, kernel, iterations = 5)
dilate = cv2.dilate(imB, kernel, iterations = 5)

plt.figure(dpi=300)
plt.axis('off')
plt.imshow(imB,cmap=plt.cm.gray)
plt.figure(dpi=300)
plt.axis('off')
plt.imshow(erode,cmap=plt.cm.gray)
plt.figure(dpi=300)
plt.axis('off')
plt.imshow(dilate,cmap=plt.cm.gray)
