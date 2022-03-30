# -*- coding: utf-8 -*-
"""
Created on Sat Mar 12 08:41:13 2022

@author: ngomi
"""

import numpy as np
import scipy.stats as st
import cv2 as cv
from scipy.ndimage import convolve
import matplotlib.pyplot as plt

x = 1
def gkern(kernlen=21, nsig=3):
    """Returns a 2D Gaussian kernel."""
    s = round((kernlen - 1) / 2) 
    x = np.linspace(-s, s, kernlen)
    kern1d = np.diff(st.norm.cdf(x))
    kern2d = np.outer(kern1d, kern1d)
    return kern2d/kern2d.sum()
"""
x = np.linspace(-1.5, 1.5, 51+1)
kern1d = np.diff(st.norm.cdf(x))
"""

matrix = gkern(51, 1)
img = cv.imread("x-ray.jpg", cv.IMREAD_GRAYSCALE)

a1 = np.array(img)
a2 = np.array(matrix)
imgResult = convolve(a1, a2)

plt.imshow(img, cmap='gray')
plt.show()
plt.imshow(imgResult, cmap='gray')
plt.show()