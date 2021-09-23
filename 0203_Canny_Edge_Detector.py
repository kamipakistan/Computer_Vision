
# ################################################################
# ################ COMPUTER VISION CHAPTER 2 #####################
# ##################### BASIC FUNCTIONS ##########################

# ################## CANNY EDGE DETECTOR #########################
# To find the edges in our image we will use canny edge detector

import cv2

# Reading the image
img = cv2.imread("lambo.jpg")

# Edge Detecting
imgCanny = cv2.Canny(img, 100, 100)

# Displaying the image
cv2.imshow("Original", img)
cv2.imshow("Canny", imgCanny)
cv2.waitKey(0)
