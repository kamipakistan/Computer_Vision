
# ################################################################
# ################ COMPUTER VISION CHAPTER 2 #####################
# ##################### BASIC FUNCTIONS ##########################

# ################## THRESHOLD IMAGE #############################

import cv2
import numpy as np

# Reading the image
img = cv2.imread("lambo.jpg")

GrayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Making Threshold Image
ret, thresh = cv2.threshold(GrayImg, 125, 255, cv2.THRESH_BINARY)

# Displaying the images
cv2.imshow("Threshold image", thresh)
cv2.imshow("Original image", img)

cv2.waitKey(0)