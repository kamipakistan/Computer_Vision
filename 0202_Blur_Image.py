# ################################################################
# ################ COMPUTER VISION CHAPTER 2 #####################
# ##################### BASIC FUNCTIONS ##########################

# ##################### BLUR IMAGE ##############################

import cv2

# Reading the image
img = cv2.imread("lambo.png")

# Converting into Blur
# Use odd Values for k_size
imgBlur = cv2.GaussianBlur(img, (11, 11), 0)

# Displaying Both the Images
cv2.imshow("Original Image", img)
cv2.imshow("Blur Image", imgBlur)
cv2.waitKey(0)