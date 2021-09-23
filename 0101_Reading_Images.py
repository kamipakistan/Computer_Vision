
# ################################################################
# ################ COMPUTER VISION CHAPTER 1 #####################

# ##################### Reading images #####################

# Importing Libraries
import cv2
image_path = "lambo.jpg"

# Reading the image
img = cv2.imread(image_path)

# Displaying the image
cv2.imshow("Output", img)

# without delay the image can not show
# 1000 = 1 Sec
cv2.waitKey(0)

