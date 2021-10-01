# ################################################################
# ################ COMPUTER VISION CHAPTER 3 #####################
# ############## RESIZING AND CROPPING OF IMAGES #################

# ################## RESIZING / RESCALING OF IMAGE ###############


# Importing library
import cv2


# Defining Rescaling function
def rescalingImg(img, scale=0.75):
    width = int(img.shape[1] * scale)
    height = int(img.shape[0] * scale)
    return cv2.resize(img, (width, height))


# Reading the image
img = cv2.imread("lambo.png")
print(img.shape)

# Calling the Resizing function
imgResize = rescalingImg(img, 0.4)

# Displaying the Images
cv2.imshow("Original Image", img)
cv2.imshow("Resize Image", imgResize)

cv2.waitKey(0)
