# ################################################################
# ################ COMPUTER VISION CHAPTER 6 #####################
# ###################### JOINING IMAGES ##########################

# ########## Horizontal and Vertical Stacking of ImageS #########

# Importing the libraries
import cv2
import numpy as np

# Reading the image
img = cv2.imread("lambo.png")

# Note the dimensions of the stacking images will be the same
# Horizontal Stacking the image
imgHorStack = np.hstack((img, img))

# vertically stacking the image
imgVrStack = np.vstack((img, img))

# Displaying the both images
cv2.imshow("Hor Stack", imgHorStack)
cv2.imshow("Var Stack", imgVrStack)
cv2.waitKey(0)


# ######################### Advance Stacking ##########################
# Stacking Function you can stack images with different channels
# and in horizontals and also in Vertical

# ######################### Stacking Function #########################

def stackImages(scale, imgArray):
    rows = len(imgArray)
    cols = len(imgArray[0])
    rowsAvailable = isinstance(imgArray[0], list)
    width = imgArray[0][0].shape[1]
    height = imgArray[0][0].shape[0]
    if rowsAvailable:
        for x in range(0, rows):
            for y in range(0, cols):
                if imgArray[x][y].shape[:2] == imgArray[0][0].shape[:2]:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (0, 0), None, scale, scale)
                else:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (imgArray[0][0].shape[1], imgArray[0][0].shape[0]),
                                                None, scale, scale)
                if len(imgArray[x][y].shape) == 2: imgArray[x][y] = cv2.cvtColor(imgArray[x][y], cv2.COLOR_GRAY2BGR)
        imageBlank = np.zeros((height, width, 3), np.uint8)
        hor = [imageBlank] * rows
        hor_con = [imageBlank] * rows
        for x in range(0, rows):
            hor[x] = np.hstack(imgArray[x])
        ver = np.vstack(hor)
    else:
        for x in range(0, rows):
            if imgArray[x].shape[:2] == imgArray[0].shape[:2]:
                imgArray[x] = cv2.resize(imgArray[x], (0, 0), None, scale, scale)
            else:
                imgArray[x] = cv2.resize(imgArray[x], (imgArray[0].shape[1], imgArray[0].shape[0]), None, scale, scale)
            if len(imgArray[x].shape) == 2: imgArray[x] = cv2.cvtColor(imgArray[x], cv2.COLOR_GRAY2BGR)
        hor = np.hstack(imgArray)
        ver = hor
    return ver


# ############## Stacking images with Advance Function ############

img = cv2.imread("lam.png")
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgStacking = stackImages(1, [[img, imgGray, img], [img, imgGray, img]])

cv2.imshow("Stacking", imgStacking)
cv2.waitKey(0)
