# -*- coding: utf-8 -*-
"""
Created on Sat Apr  9 10:02:59 2022

@author: ngomi
"""

import cv2 as cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('./images/vanban.jpg', 0)
img = 255 - img
threshval = 150; n = 255
retval, imB = cv2.threshold(img, threshval, n, cv2.THRESH_BINARY)

kernel = np.ones((3,3), np.uint8)

img_ero = cv2.erode(imB, kernel)
img_dil = cv2.dilate(imB, kernel)
result = cv2.morphologyEx(img_dil, cv2.MORPH_OPEN, kernel)

plt.figure(dpi=300)
plt.axis('off')
plt.imshow(imB,cmap=plt.cm.gray)
plt.figure(dpi=300)
plt.axis('off')
plt.imshow(img_ero,cmap=plt.cm.gray)
plt.figure(dpi=300)
