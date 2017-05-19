import cv2 #memanggil library numpy
import numpy as np #memanggil library opencv
from matplotlib import pyplot as plt #memanggil library matplotlib
from scipy import ndimage #memangil library ndimagedariscipy

img = cv2.imread('cat.jpg') #mengambil file gambar
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) #mengkonversigambarberwarnamengjadi grayscale
lpf = cv2.filter2D(img,-1,np.ones((5,5),np.float32)/25) #membuat low pass filter dengan kernel 5x5
data = np.array(gray, dtype=float)

kernel = np.array([[-9, 9, -9, ],
                   [ 9, 0,  9, ],
                   [-9, 9, -9, ]])

highpass_5x5 = ndimage.convolve(data, kernel) #membuat High pass filter

equ = cv2.equalizeHist(gray) 

cv2.imshow('Gambar Asli',img) #menampilkan gambar asli
cv2.imshow('High Pass Filter',highpass_5x5) #menampilkan gambar yang sudah filter dengan high pass filter
cv2.imshow('Low Pass Filter',lpf) #menampilkan gambar yang sudah filter dengan low pass filter
cv2.imshow('Histogram Equalization', equ) #menampilkan gambar hasil dari histogram equalization

plt.figure('Histogram Equalization') #menampilkan histogram gambar
plt.subplot(2,1,1),plt.hist(gray.ravel(),256,[0,256]),plt.title('Histogram awal') #menampilkan histogram awal
plt.subplot(2,1,2),plt.hist(equ.ravel(),256,[0,256]),plt.title('Histogram hasil equalization') #menampilkan histogram hasil equalization
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()
