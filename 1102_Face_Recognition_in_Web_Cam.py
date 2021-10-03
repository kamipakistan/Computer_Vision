
# ################################################################
# ################ COMPUTER VISION CHAPTER 11 ####################
# ################################################################
# ##################### FACE RECOGNITION #########################
# ################################################################

import numpy as np
import os
import cv2
import face_recognition

path = "faces"
images = []
classNames = []
myList = os.listdir(path)
print(myList)
for cl in myList:
    currentImg = cv2.imread(f"{path}/{cl}")
    images.append(currentImg)
    classNames.append(os.path.splitext(cl)[0])


# ######################## Step 2 ###########################
# ################### Find The Encoding #####################


def imgEncoding(images):
    encodeList = []
    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)
    return encodeList

print("Encoding Started...")
encodeListKnown = imgEncoding(images)
print("Encoding Complete")

# #####################  Step 3  ###########################
# #################### Find the Matches between our Encodings #################

cap = cv2.VideoCapture(0)

while cap.isOpened():
    success, img = cap.read()
    imgS = cv2.resize(img, (0, 0), None, 0.25, 0.25)
    imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)

    # Finding location os all the images present in Current Frame
    facesInCurrentFrame = face_recognition.face_locations(imgS)

    # Finding the encodings of all the faces present in current frame
    encodesInCurrentFrame = face_recognition.face_encodings(imgS, facesInCurrentFrame)

    # Finding the Matches
    for faceEncode, faceLoc in zip(encodesInCurrentFrame, facesInCurrentFrame):
        # We Will compare each face_encodes with our all known face encodings list
        matches = face_recognition.compare_faces(encodeListKnown, faceEncode)

        # Finding distance also comparing the know faces with the current face
        # And it will give us a list and if some face have the lowest distance
        # it will be that person
        faceDis = face_recognition.face_distance(encodeListKnown, faceEncode)
        print(faceDis)
        matchIndex = np.argmin(faceDis)

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
