
# ###########################################################################################################
# ################################################ OBJECT DETECTION #########################################
# ###########################################################################################################

# Importing libraries
import cv2 as cv
import numpy as np

cap = cv.VideoCapture(0)  # Capturing the webCamp

whT = 320  # Width and Height of the Image


# ########################## LOADING FILES FROM THE DESK #######################

# Reading COCO/ object Names file
classesFile = "coco.names"
classNames = []
with open(classesFile, 'r') as f:
    classNames = f.read().splitlines()
print(classNames)

# Loading the configuration and weights files
modelConfiguration = "yolov3-320.cfg"
modelWeights = "yolov3-320.weights"

# ##############################  Creating YOLO Network ##############################
net = cv.dnn.readNetFromDarknet(modelConfiguration, modelWeights)
# net.setPreferableBackend(cv.dnn.DNN_BACKEND_OPENCV)
# net.setPreferableTarget(cv.dnn.DNN_TARGET_CPU)


def findObjects(outputs, img):
    hT, wT, cT = img.shape  # Height , Width, and Channels of image
    boundingBoxes = []
    classIndexes = []
    confidenceValues = []

    # ##### We have multiple outputs from the Yolo network Layers
    # ##### so we will loof through single output one by one
    for output in outputs:
        # #### Now we have 85 elements in each output
        # #### So we will loof through each element one by one

        for detection in output:
            # ## First 5 out of 85 elements in detection are (cx, cy, w, h, conf)
            # ## And the Other 80 are the probability of element having the object in the image
            probScores = detection[5:]  # All the probability score
            classIndex = np.argmax(probScores)  # Index of High probability value
            confidence = probScores[classIndex]  # Getting the exact High prob.. Score through the index

            # If the confidence value of having the particular object in the image > 50
            # then we will save its Bounding boxes and confidence value and its name
            confThreshold = 0.5
            if confidence > confThreshold:
                # The original values are in float so we are converting it to pixels values
                w, h = int(detection[2]*wT), int(detection[3]*hT)

                # These values are the center points not the origin
                # So we are subtracting the img origin from these center pixels to get the origin points
                x, y = int((detection[0]*wT)-w/2), int((detection[1]*hT)-h/2)

                boundingBoxes.append([x, y, w, h])
                classIndexes.append(classIndex)
                confidenceValues.append(float(confidence))

    # None Maximum Suppression function remove the overlapping boxes on one object
    # And the keep the only one box which have maximum confidence vale
    nmsThreshold = 0.2  # if you are facing the boxes overlapping problem reduce its value
    indices = cv.dnn.NMSBoxes(boundingBoxes, confidenceValues, confThreshold, nmsThreshold)
    print(indices)
    # Drawing the Bounding boxes on image
    for i in indices:
        i = i[0]
        box = boundingBoxes[i]
        x, y, w, h = box[0], box[1], box[2], box[3]
        cv.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv.rectangle(img, (x-1, y-25), (x + w, y), (0, 255, 0), cv.FILLED)
        cv.putText(img, f'{classNames[classIndexes[i]].upper()} {int(confidenceValues[i]*100)}%',
                (x, y - 5), cv.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)


#  #### We cannot input the plain image to the network,
#  #### Yolo net accept only a particular type of image called blob
while True:
    success, img = cap.read()

    # Converting image to blob format
    blob = cv.dnn.blobFromImage(img, 1 / 255, (whT, whT), [0, 0, 0], swapRB=True, crop=False)

    # Input blob image to the Yolo network
    net.setInput(blob)

    #  #### In order to find the output from the Yolo network
    #  #### We need to know the names of the output layers
    #  #### So that we can refer to them network for finding outputs

    # Getting the names of all the layers used in yolo network
    layersNames = net.getLayerNames()
    print(layersNames)

    # We need only the names of the output layers
    outputLayersNames = net.getUnconnectedOutLayersNames()
    print(outputLayersNames)

    # Now we will forward the blob image output layers to the network and store its output
    # and from this output we will find the bounding boxes
    outputs = net.forward(outputLayersNames)

    # Output Details of from the OutPut layers of Yolo Net
    print(len(outputs))
    print(outputs[0].shape)
    print(outputs[1].shape)
    # print(outputs[2].shape)
    print(outputs[0][0])

    # Calling the findObjects Function
    findObjects(outputs, img)

    # Displaying the footage
    cv.imshow('Object Detection', img)
    if cv.waitKey(1) & 0xFF == ord("q"):
        break
