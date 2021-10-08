
# ################################################################
# ################ COMPUTER VISION CHAPTER 11 ####################
# ################################################################
# ##################### FACE RECOGNITION #########################
# ################################################################

# Importing Necessary libraries
import numpy as np
import winsound
import os
import cv2
import face_recognition

# #################################################### Step 1 #########################################################
# ######################################### Loading The Images from its Directory #####################################
# ################################## And Getting name from the images and assigning it to list of Names ###############

path = "faces"  # Path of the faces which we want to recognize
images = []  # list to keep the images/faces
classNames = []  # List to keep the name of the faces

myList = os.listdir(path)
print(myList)

for face in myList:  # loof through the faces Folder and extract all the images
    currentImg = cv2.imread(f"{path}/{face}")  # Reading the image
    # print(f"{path}/{face}")
    images.append(currentImg)  # Add the read image to the images list 1 by 1
    classNames.append(os.path.splitext(face)[0])  # Add the names of the images


# ############################################## Step 2 ###############################################
# ######################################### Find The Encoding #########################################


def imgEncoding(images):
    encodeList = []  # List to keep the encoding of each image
    for img in images:  # Loof Through the images list and extract image 1 by 1
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # Converting the image into RGB
        encode = face_recognition.face_encodings(img)[0]  # Find the encoding of the img
        encodeList.append(encode)
    return encodeList


print("Encoding Started...")
encodeListKnown = imgEncoding(images)   # Calling the function and passing the images list to the function
print("Encoding Complete")

# #########################################################  Step 3  ###################################################
# ######################################3### Find the Matches between our Encodings ####################################

cap = cv2.VideoCapture(0)  # Capturing the webCam

while cap.isOpened():
    success, img = cap.read()
    imgS = cv2.resize(img, (0, 0), None, 0.25, 0.25)  # Resizing the image for fast operation
    imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)

    # Finding location of all the images present in Current Frame 1by 1
    facesInCurrentFrame = face_recognition.face_locations(imgS)

    # Finding the encodings of all the faces present in current frame 1 by 1
    encodesInCurrentFrame = face_recognition.face_encodings(imgS, facesInCurrentFrame)

    # Finding the Matches
    for faceEncode, faceLoc in zip(encodesInCurrentFrame, facesInCurrentFrame):
        # We Will compare each face_encodes with our all known face encodings list
        matches = face_recognition.compare_faces(encodeListKnown, faceEncode)

        # Finding distance also comparing the know faces with the current face
        # And it will give us a list and if some face have the lowest distance
        # it will be that person
        faceDis = face_recognition.face_distance(encodeListKnown, faceEncode)
        print(f"Face Distances = {faceDis}")
        matchIndex = np.argmin(faceDis)
        print(f"Min Face Distances Index = {matchIndex}")

        # Creating a bounding box around the faces
        if matches[matchIndex]:
            name = classNames[matchIndex].upper()
            print(name)
            y1, x2, y2, x1 = faceLoc
            y1, x2, y2, x1 = y1*4, x2*4, y2*4, x1*4
            cv2.rectangle(img, (x1-1, y1-25), (x2+1, y1), (0, 255, 0), cv2.FILLED)
            cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.putText(img,name, (x1, y1-6), cv2.FONT_HERSHEY_COMPLEX, 0.50, (255,255,255), 1)

    cv2.imshow("WebCamp", img)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
