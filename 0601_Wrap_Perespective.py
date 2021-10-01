
# ################################################################
# ################ COMPUTER VISION CHAPTER 6 #####################
# ###################### WRAP PERSPECTIVE ########################

import cv2
import numpy as np

# Reading the image
img = cv2.imread("cards.png")

# Size required for our final image
width, height = 250, 350

# Choose the Four Coordinates of the Card
pts1 = np.float32([[452, 200], [583, 252], [382, 381], [522, 444]])

# Choose Which Coordinate is of which side
pts2 = np.float32([[0, 0], [width, 0], [0, height], [width, height]])

# Getting the Transformation matrix
matrix = cv2.getPerspectiveTransform(pts1, pts2)

# Compare the Matrix and the image and  Warping it out
result = cv2.warpPerspective(img, matrix, (width, height))

# Displaying the images
cv2.imshow("Cards", img)
cv2.imshow("Wrap", result)
cv2.waitKey(0)
