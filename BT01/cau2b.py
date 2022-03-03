# -*- coding: utf-8 -*-
"""
Created on Thu Mar  3 22:22:17 2022

@author: ngomi
"""

import cv2 as cv

def splitAndShow(i, number):
    number = str(number)
    b, g, r = cv.split(i)
    cv.imshow("b" + number, b)
    cv.imshow("g" + number, g)
    cv.imshow("r"+ number, r)

i1 = cv.imread("./img/1.png");
i2 = cv.imread("./img/2.bmp");
i3 = cv.imread("./img/3.jpg");
i4 = cv.imread("./img/4.png");
i5 = cv.imread("./img/5.bmp");
i6 = cv.imread("./img/6.jpg");
i7 = cv.imread("./img/7.png");
i8 = cv.imread("./img/8.bmp");
i9 = cv.imread("./img/9.jpg");
i10 = cv.imread("./img/10.jpg");

splitAndShow(i1,1)
"""
splitAndShow(i2,2)
splitAndShow(i3,3)
splitAndShow(i4,4)
splitAndShow(i5,5)
splitAndShow(i6,6)
splitAndShow(i7,7)
splitAndShow(i8,8)
splitAndShow(i9,9)
splitAndShow(i10,20)
"""

cv.waitKey(10000)
cv.destroyAllWindows()