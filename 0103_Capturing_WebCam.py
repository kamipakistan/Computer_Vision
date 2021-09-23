
# ################################################################
# ################ COMPUTER VISION CHAPTER 1 #####################

# ##################### Capturing WebCam #####################

# Reading libraries
import cv2

# Inside VideoCapture() 0 = to the number of camera you want to attach , now is 1
v_cap = cv2.VideoCapture(0)

# Defining the Width of the Video

# set(property_Id: Any, value: Any)
v_cap.set(3, 640)

# Defining the height of the Video
v_cap.set(4, 480)

while True:
    success, img = v_cap.read()
    cv2.imshow("video", img)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
