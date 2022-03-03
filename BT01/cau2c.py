# -*- coding: utf-8 -*-
"""
Created on Thu Mar  3 22:48:10 2022

@author: ngomi
"""

import cv2 as cv

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

i1 = cv.cvtColor(i1, cv.COLOR_BGR2GRAY)
i2 = cv.cvtColor(i2, cv.COLOR_BGR2GRAY)
i3 = cv.cvtColor(i3, cv.COLOR_BGR2GRAY)
i4 = cv.cvtColor(i4, cv.COLOR_BGR2GRAY)
i5 = cv.cvtColor(i5, cv.COLOR_BGR2GRAY)
i6 = cv.cvtColor(i6, cv.COLOR_BGR2GRAY)
i7 = cv.cvtColor(i7, cv.COLOR_BGR2GRAY)
i8 = cv.cvtColor(i8, cv.COLOR_BGR2GRAY)
i9 = cv.cvtColor(i9, cv.COLOR_BGR2GRAY)
i10 = cv.cvtColor(i10, cv.COLOR_BGR2GRAY)

cv.imshow("1", i1)
cv.imshow("2", i2)
cv.imshow("3", i3)
cv.imshow("4", i4)
cv.imshow("5", i5)
cv.imshow("6", i6)
cv.imshow("7", i7)
cv.imshow("8", i8)
cv.imshow("9", i9)
cv.imshow("10", i10)

cv.waitKey(10000)
cv.destroyAllWindows()