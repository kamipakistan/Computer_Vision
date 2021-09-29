
# ################################################################
# ################ COMPUTER VISION CHAPTER 8 #####################

# ############### CONTOURS AND SHAPE DETECTION ###################

# #################################################################
# ##################### Contours Detection ########################
# #################################################################

import cv2
import numpy as np

# Reading the image
img = cv2.imread("shape.jpg")

# Creating a blank Image
blankImg = np.zeros((375, 500, 3), np.uint8)

# Converting it into Gray, Blur and Canny
grayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blurImg = cv2.GaussianBlur(grayImg, (5, 5), 0)
cannyImg = cv2.Canny(blurImg, 80, 80)

# Finding the Contours in the image
contours, hierarchy = cv2.findContours(cannyImg, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

# Draw the Detected Contours on the blank image
drawCont = cv2.drawContours(blankImg, contours, -1, (0,255, 0), 2)

# Creating a Bounding box Around the detected Contours
for cont in contours:
    contArea = cv2.contourArea(cont)
    if contArea > 50:
        x, y, w, h = cv2.boundingRect(cont)
        cv2.rectangle(img, (x,y), (x+w, y+h), (255, 0, 0), 2)

# Displaying the images
cv2.imshow("Blank Image", blankImg)
cv2.imshow("Canny Image", cannyImg)
cv2.imshow("Image", img)
cv2.waitKey(0)
