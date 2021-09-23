
# ################################################################
# ################ COMPUTER VISION CHAPTER 8 #####################

# ######################## FACE DETECTION ########################

# #################################################################
# ##################### Face Detection in WebCam ##################
# #################################################################

import cv2
# Loading the Face Detection Cascade
faceCascade = cv2.CascadeClassifier("Cascades/haarcascade_frontalface_default.xml")

# Capturing the Video
videoCap = cv2.VideoCapture(0)

while True:
    # Getting the images from the video
    success, img = videoCap.read()

    # Converting it into Gray Scale
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Detecting the faces
    faces = faceCascade.detectMultiScale(imgGray, 1.1, 4)

    # Drawing the rectangle around the face
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, h+y), (0, 255, 0), 2)
    cv2.imshow("Video", img)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
