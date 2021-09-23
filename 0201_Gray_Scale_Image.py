# ################################################################
# ################ COMPUTER VISION CHAPTER 2 #####################
# ##################### BASIC FUNCTIONS ##########################

# ##################### GRAY SCALE IMAGE #####################
# importing libraries
import cv2

# Reading the image
img = cv2.imread("lambo.png")

# Converting it into Gray scale image
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Displaying the images
cv2.imshow("Original Image", img)
cv2.imshow("Gray Image", imgGray)
cv2.waitKey(0)