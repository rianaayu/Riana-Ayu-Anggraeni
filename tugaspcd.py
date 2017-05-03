import numpy as np
import cv2


vid = cv2.VideoCapture(0)

while (True):
	
	ret, lihat = vid.read() 
	gray = cv2.cvtColor(lihat,cv2.COLOR_BGR2GRAY) 
    #untuk Mengkonversi gambar menjadi skala keabuan
	negatif = (255 - gray) 
    #untuk mengkonversi gambar menjadi skala Negatif
	brightness = (lihat + 20) 
    #untuk Mengatur Brightness dari Gambar Asli


	cv2.imshow('Gambar Asli',lihat) #untuk Menampilkan Gambar Asli
	cv2.imshow('Skala keabuan',gray) #untuk Menampilkan skala keabuan pada gambar
	cv2.imshow('skala Negatif',negatif)  #untuk Menampilkan skala Negatif pada gambar
	cv2.imshow('Brightness',brightness)  #untuk Mengatur Brightness dari Gambar Asli
	if cv2.waitKey(1) & 0xFF == ord('x'): 
		break
		

vid.release()
cv2.destroyAllWindows()
