#import library
import cv2
import numpy as np
from matplotlib import pyplot as plt


######  FUNGSI ######
#menyimpan citra
def ambildata():
    global image
    image = cv2.imshow('data1.png',0)
    #image1 = cv2.imread('data2.png',0)
    #image2 = cv2.imread('data3.png',0)

    #image = cv2.medianBlur(image,5)
    #image1 = cv2.medianBlur(image1,5)
    #image2 = cv2.medianBlur(image2,5)


#convert rgb to grayscale
def gray():
    global grayImage
    grayImage = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    grayImage1 = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    grayImage2 = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

#thresholding
def tresholding():
    global th1
    #_, thr1 = cv2.threshold(,127, 255, cv2.THRESH_BINARY)
    #_, thr2 = cv2.threshold(grayImage,127, 255, cv2.THRESH_OTSU)
    #_, thr3 = cv2.threshold(image,127, 255, cv2.THRESH_BINARY_INV)
    th1 = cv2.adaptiveThreshold(grayImage,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)
#th2 = cv2.adaptiveThreshold(image3,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,2)

#thresholding after gaussian filter
#blur = cv2.GaussianBlur(image,(5,5),0)
#ret1, th3 = cv2.threshold(blur,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
#ret2, th4 = cv2.threshold(image,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)


#Segmentasi
def canny():
    global edges
    edges = cv2.Canny(thr2,100,200)

#memanggil citra yang sudah di simpan
#titles = ['Original Image', 'Threshold Otsu', 'Adaptive Threshold gaussian', 'adaptive threshold mean']
#images = [image2,thr2,th1,th2]

#for i in range (4):
#plt.subplot(2,2,i+1),plt.imshow(images[i],'gray')
#plt.title(titles[i]),plt.xticks([]),plt.ylim([])
#plt.show()


###### PROGRAM UTAMA ########
ambildata()
gray()
tresholding()
canny()

plt.subplot(121),plt.imshow(image,cmap= 'gray')
plt.title('gambar asli'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(edges,cmap = 'gray')
plt.title('otsu threshold 2'), plt.xticks([]), plt.yticks([])
plt.show()

#cv2.imshow('gambar asli',image3)
#cv2.imshow('gambar yang sudah di rubah',grayImage)

cv2.waitKey(0)
cv2.destroyAllWindows()