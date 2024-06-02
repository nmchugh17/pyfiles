import cv2
import time
print(cv2.__version__)

# openCV9.py - selects a square in the middle of the live feed and has altered this section to grayscale
################           Press the Q key to Exit Camera       #################################

width =640
height = 360


cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
cam.set(cv2.CAP_PROP_FPS, 30)
cam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))


while True:
    
    ignore, frame = cam.read()
    frameROI = frame[150:210,250:390]
    frameROIGray = cv2.cvtColor(frameROI,cv2.COLOR_BGR2GRAY)
    frameROIBGR =  cv2.cvtColor(frameROIGray,cv2.COLOR_GRAY2BGR)

    cv2.imshow('My BGR ROI', frameROIBGR)
    cv2.moveWindow('My BGR ROI', 650, 180)

    frame[150:210,250:390] = frameROIBGR
    # frame[0:60,0:140] = frameROIBGR
    cv2.imshow('My Gray ROI', frameROIGray)
    cv2.moveWindow('My Gray ROI', 650, 90)

    cv2.imshow('My ROI', frameROI)
    cv2.moveWindow('My ROI', 650, 0)
    
    cv2.imshow('My Webcam', frame)
    cv2.moveWindow('My Webcam', 0, 0)
    if(cv2.waitKey(1) & 0xff == ord('q')):
        break

cam.release()