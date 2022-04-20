# -*- coding: utf-8 -*-
"""
Created on Sat Apr  9 09:33:51 2022

@author: ngomi
"""

import cv2 as cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('./images/F95.png', 0)
threshval = 100; n = 255
retval, imB = cv2.threshold(img, threshval, n, cv2.THRESH_BINARY)

kernel = np.ones((11,11), np.uint8)

opening = cv2.morphologyEx(imB, cv2.MORPH_OPEN, kernel)
closing = cv2.morphologyEx(imB, cv2.MORPH_CLOSE, kernel)
img_ero = cv2.erode(imB, kernel)
img_dil = cv2.dilate(imB, kernel)

plt.subplot(2,3,1),plt.axis('off')
plt.imshow(imB,cmap=plt.cm.gray)
plt.subplot(2,3,2),plt.axis('off')
plt.imshow(opening,cmap=plt.cm.gray)
plt.subplot(2,3,3),plt.axis('off')
plt.imshow(closing,cmap=plt.cm.gray)
plt.subplot(2,3,5),plt.axis('off')
plt.imshow(img_ero,cmap=plt.cm.gray)
plt.subplot(2,3,6),plt.axis('off')
plt.imshow(img_dil,cmap=plt.cm.gray)