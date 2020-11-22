import cv2
import numpy as np
# from pyimagesearch import imutils
# from skimage import exposure
import imutils

# ambil gambar dan langsung di ubah jadi grayscale
img = cv2.imread('data2.jpg',0)
# ubah citra dari grayscale ke thresholding
_, thr1 = cv2.threshold(img,127, 255, cv2.THRESH_OTSU)
# karnel
kernel = np.ones((2,3),np.uint8)
# erode untuk menipiskan lapisan / thinning
erosion = cv2.erode(thr1,kernel,iterations =1 )
# segmentasi
edge = cv2.Canny(erosion,100,200)

# menemukan untuk di potong pada image
cnts = cv2.findContours(edge.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)
cnts = sorted(cnts, key=cv2.contourArea, reverse=True) [:10]
screenCnt = None

for c in cnts:
    peri = cv2.arcLength(c, True)
    approx = cv2.approxPolyDP(c, 0.015 * peri, True)

    if len(approx) == 4:
        screenCnt = approx
        break

cv2.drawContours(img, screenCnt,0, (0,255,0),3)
cv2.imshow("hasil",thr1)
cv2.waitKey(0)
cv2.destroyAllWindows()
