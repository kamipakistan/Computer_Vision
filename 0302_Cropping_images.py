
# ################################################################
# ################ COMPUTER VISION CHAPTER 3 #####################
# ############## RESIZING AND CROPPING OF IMAGES #################

# ################## CROPPING OF IMAGE ###########################

# For cropping we do not need the cv2 functions,
# Image is an 2D Array we just limit its size of the Row and columns

import cv2

# Reading the image
img = cv2.imread("lambo.png")

# Cropping the Image
# img[height, width]
imgCropped = img[71:304, 100:430]

# Displaying the Images
cv2.imshow("Original Image", img)
cv2.imshow("Resize Image", imgCropped)

cv2.waitKey(0)

# Displaying The Shapes of the images
print(img.shape)
print(imgCropped.shape)
