# -*- coding: utf-8 -*-
"""
Created on Sat Mar 26 08:13:22 2022

@author: ngomi
"""

import cv2
import numpy as np
from matplotlib import pyplot
import matplotlib.pyplot as plt
#%% Xây dựng hàm tích chập
def conv(A,k,b=0):
    kh,kw=k.shape
    if b>0:
        h,w=A.shape
        B=np.ones((h+kh-1,w+kw-1))
        th=int(kh/2)
        tw=int(kw/2)
        B[th:h+th,tw:w+tw]=A
        A=B
    h,w=A.shape
    C=np.ones((h,w))
    for i in range(0,h-kh+1):
        for j in range(0,w-kw+1):
            sA=A[i:i+kh,j:j+kw]
            C[i,j]=np.sum(k*sA)
    C=C[0:h-kh+1,0:w-kw+1]
    return C
#%% Đọc file ảnh và hiển thị
img = cv2.imread('img/dog.jpg')
img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
img=cv2.resize(img,(200, 200))
plt.imshow(img)
plt.show()
#%% Tích chập ảnh với kernel 5x5=> lọc trung bình
k=np.ones((5,5))/25
r,g,b = cv2.split(img)
B=conv(b,k,1)
G=conv(g,k,1)
R=conv(r,k,1)
imgN=cv2.merge((R,G,B))
imgN=np.array(imgN,dtype='uint8')
plt.imshow(imgN)
plt.show()
