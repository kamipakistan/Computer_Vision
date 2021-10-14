
# ################################################################
# ################ COMPUTER VISION CHAPTER 5 #####################
# ################ IMAGE TRANSFORMATION #########################

# ############### ROTATION OF IMAGE ############################
import cv2
import numpy as np


def imgRotation(img, angle, rotationPoint = None):
    (width, height) = img.shape[1], img.shape[0]
    if rotationPoint is None:
        rotationPoint = (width//2, height//2)
    rotationMatrix = cv2.getRotationMatrix2D(rotationPoint, angle, 1.0)
    dimensions = (width, height)
    return cv2.warpAffine(img, rotationMatrix, dimensions)


img = cv2.imread("lambo.jpg")
rotated = imgRotation(img, 90)
cv2.imshow("Rotated Image", rotated)
cv2.imshow("Image", img)
cv2.waitKey(0)
