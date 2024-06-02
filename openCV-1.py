import cv2
print(cv2.__version__)

# openCV1.py - opens 4 camera frames each with different image colour gradings (eg. grayscale)
################           Press the Q key to Exit Camera       #################################

cam = cv2.VideoCapture(0)

while True:
    ignore, frame = cam.read()

    grayFrame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    altFrame = cv2.cvtColor(frame,cv2.COLOR_BGR2HLS_FULL)
    altFrame2 = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV_FULL)

    cv2.imshow('my WEBcam 1', frame)
    cv2.moveWindow('my WEBcam 1', 0, 0)

    cv2.imshow('my WEBcam 2', grayFrame)
    cv2.moveWindow('my WEBcam 2', 640, 0)
   
    cv2.imshow('my WEBcam 3', altFrame)
    cv2.moveWindow('my WEBcam 3', 0, 510)

    cv2.imshow('my WEBcam 4', altFrame2)
    cv2.moveWindow('my WEBcam 4', 640, 510)

    if(cv2.waitKey(1) & 0xff == ord('q')):
        break

cam.release()