
# ################################################################
# ################ COMPUTER VISION CHAPTER 8 #####################

# ######################## FACE DETECTION ########################

# #################################################################
# ##################### Face detection in images ###################
# #################################################################

import cv2

# Loading the face detection Cascade
faceCascade = cv2.CascadeClassifier("Cascades/haarcascade_frontalface_default.xml")

# Reading the image
img = cv2.imread("220px-Lenna_(test_image).png")

# Converting it into Gray Scale
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Detecting faces
faces = faceCascade.detectMultiScale(img, 1.1, 4)

# Drawing Rectangle around the face
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
    cv2.imshow("image", img)
    cv2.waitKey(0)

