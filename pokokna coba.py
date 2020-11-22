import cv2
import numpy as np

img = cv2.imread("data2.jpg",0)
_, thr = cv2.threshold(img,0, 255, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
img1 = thr.copy()

# Structuring Element
kernel = cv2.getStructuringElement(cv2.MORPH_CROSS,(3,3))
# Create an empty output image to hold values
thin = np.zeros(img.shape,dtype='uint8')

# Loop until erosion leads to an empty set
while (cv2.countNonZero(img1)!=0):
    # Erosion
    erode = cv2.erode(img1,kernel)
    # Opening on eroded image
    opening = cv2.morphologyEx(erode,cv2.MORPH_OPEN,kernel)
    # Subtract these two
    subset = erode - opening
    # Union of all previous sets
    thin = cv2.bitwise_or(subset,thin)
    # Set the eroded image for next iteration
    img1 = erode.copy()

cv2.imshow('original',thr)
cv2.imshow('thinned',thin)
cv2.waitKey(0)
cv2.destroyAllWindows()