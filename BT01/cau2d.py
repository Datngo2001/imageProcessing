# -*- coding: utf-8 -*-
"""
Created on Thu Mar  3 23:05:37 2022

@author: ngomi
"""

import cv2 as cv


i5 = cv.imread("./img/5.bmp");


rolateDegree = 15
scale = 1.0
(h, w) = i5.shape[:2]
center = (w / 2, h / 2)
for i in range(1, 100):
    M = cv.getRotationMatrix2D(center, rolateDegree, scale)
    rotated = cv.warpAffine(i5, M, (w, h))
    cv.imshow("rotated", rotated)
    rolateDegree += 15
    scale *= 0.9
    cv.waitKey(50)
    pass

cv.waitKey(5000)
cv.destroyAllWindows()