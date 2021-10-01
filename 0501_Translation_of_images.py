
# ################################################################
# ################ COMPUTER VISION CHAPTER 5 #####################
# ################ IMAGE TRANSFORMATION #########################

# ############### TRANSLATION OF IMAGE ##########################
import cv2
import numpy as np


# Defining Image Translation Function
def imgTranslation(img, x, y):
    transMat = np.float32([[1, 0, x], [0, 1, y]])
    imgDimensions = (img.shape[1], img.shape[0])
    return cv2.warpAffine(img, transMat, imgDimensions)


# Loading the image
img = cv2.imread("lambo.jpg")

# Displaying the images
tImg = imgTranslation(img, 100, 100)
cv2.imshow("Translated Image", tImg)
cv2.imshow("Image", img)
cv2.waitKey(0)
