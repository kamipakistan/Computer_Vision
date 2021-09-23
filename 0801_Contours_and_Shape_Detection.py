
# ################################################################
# ################ COMPUTER VISION CHAPTER 8 #####################

# ############### CONTOURS AND SHAPE DETECTION ###################

# #################################################################
# ##################### Contours Finding Method ###################
# #################################################################

# Importing libraries
import cv2
import numpy as np

# Defining Contours finding  method
def getContours(img):
    # Finding The Contours of the object
    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    # Ones we have find the contours it is saved in contours
    # So we wil loop through it for getting the values

    for cont in contours:
        # So for each contours we are going to find the area first
        contours_area = cv2.contourArea(cont)

        # After this we will Draw the Contours on original image
        print(f"\nArea = {contours_area}")

        if contours_area > 500:
            # In each loop it will draw the complete points present in cont
            cv2.drawContours(imgContours, cont, -1, (255, 0, 0), 3)

            # Now we will find the perimeter of the contours
            arcLen = cv2.arcLength(cont, True)
            print(f"Perimeter =  {arcLen}")

            # Approximate the corner point, How many points we have
            approx = cv2.approxPolyDP(cont, (0.02 * arcLen), True)
            print(approx)
            objCorners = len(approx)
            print(f"Object Corners = {objCorners}")

            # Creating bounding box length, height around the detected object
            x, y, w, h = cv2.boundingRect(approx)
            cv2.rectangle(imgContours, (x, y), (x + w, y + h), (255, 0, 0), 2)

            # Defining the Shape of the Object and Assigning name to it
            if objCorners == 3:
                objectType = "Tri"
            elif objCorners == 4:
                espectRatio = w / float(h)
                print(espectRatio)
                if espectRatio > 0.95 and espectRatio < 1.05:
                    objectType = "Square"
                else:
                    objectType = "Rectangle"
            elif objCorners == 5:
                objectType = "Pentagon"
            elif objCorners == 6:
                objectType = "Hexagon"
            elif objCorners > 6:
                objectType = "Circle"
            else:
                objectType = "None"

            # Writing Each Object name in each ittration
            cv2.putText(imgContours, objectType, (x + (w // 2) - 25, y + (h // 2) + 15), cv2.FONT_HERSHEY_COMPLEX, 0.7,
                        (0, 0, 0), 2)

# #################################################################
# ##################### STACKING FUNCTION #########################
# #################################################################

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


# #################################################################
# ##################### SHAPE DETECTION ###########################
# #################################################################

# Reading the image
img = cv2.imread("shape.jpg")

imgContours = img.copy()

# Converting it into Gray
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Converting into Blur
imgBlur = cv2.GaussianBlur(imgGray, (7, 7), 1)

# Canny Edge detector
imgCanny = cv2.Canny(imgBlur, 10, 10)

# Increase the edge size of canny image
imgDialation = cv2.dilate(imgCanny, (7, 7), 3)

# Calling the Contours Finding Function
getContours(imgDialation)

# Creating black image
imgBlank = np.zeros_like(img)

# Stacking images for better view
stackImg = stackImages(0.7, ([img, imgGray, imgBlur],
                             [imgDialation, imgContours, imgBlank]))

# Displaying the Stacked Images
cv2.imshow("Image", stackImg)
cv2.waitKey(0)

