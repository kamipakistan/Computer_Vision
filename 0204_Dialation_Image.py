
# ###############################################################
# ################ COMPUTER VISION CHAPTER 2 ####################
# ##################### BASIC FUNCTIONS #########################

# ################## DILATION IMAGE ############################
# Dilation means Increase the thickness of edges in Canny

import cv2
import numpy as np

# Reading the image
img = cv2.imread("lambo.jpg")

# Making Kernel for the Dilation
kernel = np.ones((5, 5), np.uint8)

# Making canny image
imgCanny = cv2.Canny(img, 100, 100)

# Making Dilation of Canny images
# iterations value means how many thickness we want
imgDilation = cv2.dilate(imgCanny, kernel, iterations=1)

# Displaying the images
cv2.imshow("Canny Image", imgCanny)
cv2.imshow("Dilation", imgDilation)

cv2.waitKey(0)


