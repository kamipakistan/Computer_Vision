
# ################################################################
# ################ COMPUTER VISION CHAPTER 3 #####################
# ############## RESIZING AND CROPPING OF IMAGES #################

# ################## RESIZING OF IMAGE ###########################

# Importing library
import cv2

# Reading the image
img = cv2.imread("lambo.png")

# Resizing the Image
imgResize = cv2.resize(img, (200, 132))

# Displaying the Images
cv2.imshow("Original Image", img)
cv2.imshow("Resize Image", imgResize)

cv2.waitKey(0)

# Displaying The Shapes of the images
print(img.shape)
print(imgResize.shape)
