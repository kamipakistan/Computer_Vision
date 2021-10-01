
# ################################################################
# ################ COMPUTER VISION CHAPTER 5 #####################
# ################ IMAGE TRANSFORMATION #########################

# ############### FLIPPING OF IMAGE ############################

import cv2
import numpy as np

# Loading the image
img = cv2.imread("lambo.jpg")

# Flipping
flip = cv2.flip(img, 1)

# Displaying the images
cv2.imshow("Flipped Image", flip)
cv2.imshow("Image", img)
cv2.waitKey(0)
