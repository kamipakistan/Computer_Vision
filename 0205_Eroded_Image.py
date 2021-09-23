
# ################################################################
# ################ COMPUTER VISION CHAPTER 2 #####################
# ##################### BASIC FUNCTIONS ##########################

# ################## ERODED IMAGE #############################
# Opposite of the Dilation (Decrease The edges)

import cv2
import numpy as np

# Reading the image
img = cv2.imread("lambo.jpg")

# Making Kernel for the Dilation and Erosion image
kernel = np.ones((5, 5), np.uint8)

# Making canny image
imgCanny = cv2.Canny(img, 200, 200)

# Making Dilation of Canny images
# iterations value means how many thickness we want
imgDilation = cv2.dilate(imgCanny, kernel, iterations = 1)

# Making Eroded Image
imgEroded = cv2.erode(imgDialation, kernel, iterations=1)

# Displaying the images
cv2.imshow("Dilation image", imgDilation)
cv2.imshow("Eroded image", imgEroded)

cv2.waitKey(0)