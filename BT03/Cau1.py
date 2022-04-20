import cv2
import numpy as np
import matplotlib.pyplot as plt
from math import e

plt.rcParams.update({'font.size': 5})
img = cv2.imread('img/hand.png', cv2.IMREAD_GRAYSCALE)
img = cv2.resize(img, (420, 344))
rows, cols = img.shape
crow,ccol = rows//2 , cols//2
Do = 25

# Low pass Filter using Distance Matrix
def LowDesign(img, rows, cols, Do):
    # D is distance Matrix
    D = np.zeros([rows, cols], dtype=np.uint32)
    # H is Filter
    H = np.zeros([rows, cols,2], dtype=np.uint8)
    r = rows // 2
    c = cols // 2
    # Distance Vector
    for u in range(0, rows):
        for v in range(0, cols):
            D[u, v] = ((u - r)**2 + (v - c)**2)**0.5
            square = -D[u,v]**2/2*Do**2
            H[u,v] = e**square
    # Using Cut off frequncy applying 0 and 255 in H to make alow pass filter and center = 1

    return H

# High pass Filter using Distance Matrix
def HighDesign(img, rows, cols, Do):
    # D is distance Matrix
    D = np.zeros([rows, cols], dtype=np.uint32)
    # H is Filter
    H = np.zeros([rows, cols,2], dtype=np.uint8)
    r = rows // 2
    c = cols // 2
    # Distance Vector
    for u in range(0, rows):
        for v in range(0, cols):
            D[u, v] = ((u - r)**2 + (v - c)**2)**0.5
            square = -D[u,v]**2/2*Do**2
            H[u,v] = 1 - e**square
    # Using Cut off frequncy applying 0 and 255 in H to make alow pass filter and center = 1

    return H


# create a mask remain all zeros, center is 1,
L= LowDesign(img, rows, cols, Do)
H= HighDesign(img, rows, cols, Do)
# apply mask and inverse DFT
dft = cv2.dft(np.float32(img),flags = cv2.DFT_COMPLEX_OUTPUT)
dft_shift = np.fft.fftshift(dft)
fshift = dft_shift*L
f_ishift = np.fft.ifftshift(fshift)
img_back = cv2.idft(f_ishift)
img_back = cv2.magnitude(img_back[:,:,0],img_back[:,:,1])
plt.subplot(121),plt.imshow(img, cmap = 'gray')
plt.title('Input Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(img_back, cmap = 'gray')
plt.title('Result'),
plt.xticks([]), plt.yticks([])
plt.show()