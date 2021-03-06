# -*- coding: utf-8 -*-
"""
Created on Sat Apr  9 09:36:40 2022

@author: ngomi
"""
import cv2 as cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('./images/vantay.jpg', 0)
img = 255 - img
threshval = 100; n = 255
retval, imB = cv2.threshold(img, threshval, n, cv2.THRESH_BINARY)

kernel = np.ones((3,3), np.uint8)
result = cv2.morphologyEx(imB, cv2.MORPH_CLOSE, kernel)

plt.figure(dpi=300)
plt.axis('off')
plt.imshow(imB,cmap=plt.cm.gray)
plt.figure(dpi=300)
plt.axis('off')
plt.imshow(result,cmap=plt.cm.gray)
