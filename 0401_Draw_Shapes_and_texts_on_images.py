
# ################################################################
# ################ COMPUTER VISION CHAPTER 4 #####################
# ################ SHAPES AND TEXT ON IMAGES #####################

import cv2
import numpy as np

# Making an black (0 = black) image
img = np.zeros((512, 512, 3), np.uint8)

# We can even convert it in to different Colors
# Blue Image, (BGR)
# img[:] = 255, 0, 0


# ################## DRAWING SHAPES OF IMAGE ###########################

# Creating Line on image
cv2.line(img, (0, 0), (img.shape[0], img.shape[1]), (0, 0, 255), 3)

# Creating a Rectangle
cv2.rectangle(img, (40, 300), (200, 450), (0, 255, 0), 2)

# Creating a Circle
cv2.circle(img, (400, 100), 50, (255, 0, 0), 3)


# ################## DRAWING TEXTS ON IMAGE ###########################

# Circle
cv2.putText(img, "Circle", (360, 110), cv2.FONT_HERSHEY_COMPLEX, 0.8, (0, 255, 0), 2)

# Rectangle
cv2.putText(img, "Rectangle", (58, 380), cv2.FONT_HERSHEY_COMPLEX, 0.8, (0, 255, 0), 2)

# line
cv2.putText(img, "Line", (220, 250), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 0), 2)


# Displaying image
cv2.imshow("Image", img)
cv2.waitKey(0)