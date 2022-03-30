# -*- coding: utf-8 -*-
"""
Created on Sat Mar  5 09:25:27 2022

@author: ngomi
"""

import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

img = cv.imread("night.jpg", cv.IMREAD_COLOR)
img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
plt.imshow(img)
plt.show()

c = 0.05
gamma = 1.3

s = np.array(c * 255 * ((img/255) ** gamma))

plt.imshow(s)
plt.show()
