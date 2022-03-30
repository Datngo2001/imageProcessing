# -*- coding: utf-8 -*-
"""
Created on Sat Mar  5 08:51:47 2022

@author: ngomi
"""

import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread("x-ray.jpg", cv.IMREAD_GRAYSCALE)
plt.imshow(img, cmap='gray')
plt.show()
Neg = (256-1)-img
plt.imshow(Neg, cmap='gray')
plt.show()