
# ################################################################
# ################ COMPUTER VISION CHAPTER 1 #####################

# ##################### Capturing images #####################

# Reading libraries
import cv2

video_path = "E:\Movies\Dolittle (2020) HDRip 1080p  HQ Lines Telugu+Tamil+Hindi+Eng[MB].mkv"

# Reading the video
capv = cv2.VideoCapture(video_path)

# The Video is consist of continues images
# so that's why we are putting loop on the images

while True:
    success, img = capv.read()
    cv2.imshow("video", img)

    # the images will continuously showing until we press q
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break


