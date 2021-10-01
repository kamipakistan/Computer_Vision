
# ################################################################
# ################ COMPUTER VISION CHAPTER 8 #####################

# ##################### COLOR DETECTION ##########################

# ###################  Images Stacking Function #################

def stackImages(scale,imgArray):
    rows = len(imgArray)
    cols = len(imgArray[0])
    rowsAvailable = isinstance(imgArray[0], list)
    width = imgArray[0][0].shape[1]
    height = imgArray[0][0].shape[0]
    if rowsAvailable:
        for x in range ( 0, rows):
            for y in range(0, cols):
                if imgArray[x][y].shape[:2] == imgArray[0][0].shape [:2]:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (0, 0), None, scale, scale)
                else:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (imgArray[0][0].shape[1], imgArray[0][0].shape[0]), None, scale, scale)
                if len(imgArray[x][y].shape) == 2: imgArray[x][y]= cv2.cvtColor( imgArray[x][y], cv2.COLOR_GRAY2BGR)
        imageBlank = np.zeros((height, width, 3), np.uint8)
        hor = [imageBlank]*rows
        hor_con = [imageBlank]*rows
        for x in range(0, rows):
            hor[x] = np.hstack(imgArray[x])
        ver = np.vstack(hor)
    else:
        for x in range(0, rows):
            if imgArray[x].shape[:2] == imgArray[0].shape[:2]:
                imgArray[x] = cv2.resize(imgArray[x], (0, 0), None, scale, scale)
            else:
                imgArray[x] = cv2.resize(imgArray[x], (imgArray[0].shape[1], imgArray[0].shape[0]), None,scale, scale)
            if len(imgArray[x].shape) == 2: imgArray[x] = cv2.cvtColor(imgArray[x], cv2.COLOR_GRAY2BGR)
        hor= np.hstack(imgArray)
        ver = hor
    return ver

# ##########################################################################
# ########################## COLOR DETECTION ###############################
# ##########################################################################

# Importing Libraries
import cv2
import numpy as np


# Defining a Function for Trackbars
def empty(a):
    pass


# Creating the Window For TrackBras
cv2.namedWindow("TrackBars")
cv2.resizeWindow("TrackBars", 640, 240)

# Creating the TrackBars Values
cv2.createTrackbar("Hue Min", "TrackBars", 12, 179, empty)
cv2.createTrackbar("Hue Max", "TrackBars", 179, 179, empty)
cv2.createTrackbar("Sat Min", "TrackBars", 120, 255, empty)
cv2.createTrackbar("Sat Max", "TrackBars", 255, 255, empty)
cv2.createTrackbar("Val Min", "TrackBars", 81, 255, empty)
cv2.createTrackbar("Val Max", "TrackBars", 255, 255, empty)

# Reading the TrackBars Values
while True:
    # Reading the Image
    img = cv2.imread("lambo.png")

    # Converting it into HSV
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # Reading the TrackBars Values
    h_min = cv2.getTrackbarPos("Hue Min", "TrackBars")
    h_max = cv2.getTrackbarPos("Hue Max", "TrackBars")
    s_min = cv2.getTrackbarPos("Sat Min", "TrackBars")
    s_max = cv2.getTrackbarPos("Sat Max", "TrackBars")
    v_min = cv2.getTrackbarPos("Val Min", "TrackBars")
    v_max = cv2.getTrackbarPos("Val Max", "TrackBars")

    # Printing the Trackbar Values
    print(h_min, h_max, s_min, s_max, v_min, v_max)

    # We Will use the above TrackBars values to filter our image
    # and we get a particular color in that range

    # Creating a mask which are in the range of these colors
    lower = np.array([h_min, s_min, v_min])
    upper = np.array([h_max, s_max, v_max])
    mask = cv2.inRange(imgHSV, lower, upper)

    # Comparing The Mask and Original Image And Creating a new one from it
    imgResult = cv2.bitwise_and(img, img, mask=mask)

    imgStacks = stackImages(0.8, ([img, imgHSV], [mask, imgResult]))

    # Displaying all the Images
    cv2.imshow("Stacks", imgStacks)
    cv2.waitKey(1)
