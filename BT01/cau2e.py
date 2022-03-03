# -*- coding: utf-8 -*-
"""
Created on Thu Mar  3 23:19:53 2022

@author: ngomi
"""

import cv2 as cv


i9 = cv.imread("./img/9.jpg");

(h, w) = i9.shape[:2]
center = (round(w / 2), round(h / 2))

crop_x = round(w / 4)
crop_y = round(h / 4)
crop_w = round(w / 2)
crop_h = round(h / 2)

cv.imshow("image", i9)
crop_img = i9[center[1]:h, center[0]:w]
cv.imshow("cropped", crop_img)

cv.waitKey(10000)
cv.destroyAllWindows()