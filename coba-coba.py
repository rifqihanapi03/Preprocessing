#import library
import cv2
import numpy as np
from PIL import Image
from matplotlib import pyplot as plt
############## FUNGSI ##############
#############menyimpan citra#####################
image = cv2.imread('data2.jpg')
#im = np.array(image[50][50])
#image1 = cv2.imread('data2.png',0)
#image2 = cv2.imread('data3.png',0)
#image = cv2.medianBlur(image,5)
#image1 = cv2.medianBlur(image1,5)
#image2 = cv2.medianBlur(image2,5)

#############convert rgb to grayscale############

#grayImage = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
#grayImage1 = cv2.cvtColor(image1,cv2.COLOR_BGR2GRAY)
#grayImage2 = cv2.cvtColor(image2,cv2.COLOR_BGR2GRAY)
#im = np.array(grayImage)

#################thresholding###################
#_, thr1 = cv2.threshold(image3,127, 255, cv2.THRESH_BINARY)
#_, thr2 = cv2.threshold(grayImage,127, 255, cv2.THRESH_OTSU)
#_, thr3 = cv2.threshold(image,127, 255, cv2.THRESH_BINARY_INV)
#th1 = cv2.adaptiveThreshold(image,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)
#th2 = cv2.adaptiveThreshold(grayImage,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,2)
#thresholding after gaussian filter
#blur = cv2.GaussianBlur(image,(5,5),0)
#ret1, th3 = cv2.threshold(blur,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
#ret2, th4 = cv2.threshold(grayImage,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)


################Segmentasi######################
#edges = cv2.Canny(thr2,100,200)
#im = np.array(thr2)

#####################FCC########################
#contours,_= cv2.findContours(thr2, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

#cv2.putText(image, "Number of contours = {}".format(len(contours))), (400,35), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0),2)

#cv2.drawContours(image, contours, 2, (0,0,255),3)

################ PROGRAM UTAMA ####################
#memanggil citra yang sudah di simpan
#titles = ['Original Image', 'Threshold Otsu', 'Adaptive Threshold gaussian', 'adaptive threshold mean']
#images = [image2,thr2,th1,th2]

#for i in range (4):
#plt.subplot(2,2,i+1),plt.imshow(images[i],'gray')
#plt.title(titles[i]),plt.xticks([]),plt.ylim([])
#plt.show()

#plt.subplot(121),plt.imshow(th2,cmap = 'gray')
#plt.title('gambar asli'), plt.xticks([]), plt.yticks([])
#plt.subplot(122),plt.imshow(edges,cmap = 'gray')
#plt.title('otsu threshold 2'), plt.xticks([]), plt.yticks([])
#plt.show()

#cv2.imshow('gambar asli',image)
#cv2.imshow('gambar yang sudah di rubah',grayImage)

cv2.imshow('image',thinned)
#np.savetxt('matrixthr1.txt',im,fmt="%s")
cv2.waitKey(0)
cv2.destroyAllWindows()