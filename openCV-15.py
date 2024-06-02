import cv2
import numpy as np
print(cv2.__version__)

# openCV15.py - click on the live webcam feed, a new window will appear displaying the colour and rgb code of the colour within the specific pixel that was clicked
################           Press the Q key to Exit Camera       #################################

evt = 0
xVal = 0
yVal = 0
width = 1280
height = 720

def mouseClick(event,xPos,yPos,flags,params):
    global evt
    global xVal
    global yVal
    if event == cv2.EVENT_LBUTTONDOWN:
        print(event)
        evt = event
        xVal = xPos
        yVal = yPos
    if event == cv2.EVENT_RBUTTONUP:
        print(event)
        evt = event
        xVal = xPos
        yVal = yPos

cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
cam.set(cv2.CAP_PROP_FPS, 30)
cam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))

cv2.namedWindow('My Webcam')
cv2.setMouseCallback('My Webcam', mouseClick)

while True:
    
    ignore, frame = cam.read()
    if evt == 1 :
        x = np.zeros([250,250,3], dtype=np.uint8)
        y=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
        clr=y[yVal][xVal]
        print(clr)
        x[:,:] = clr
        cv2.putText(x,str(clr),(0,50),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,0),1)
        cv2.imshow('Color Picker', x)
        cv2.moveWindow('Color Picker', width,0)
        # evt=0

    cv2.imshow('My Webcam', frame)
    cv2.moveWindow('My Webcam', 0, 0)

    if(cv2.waitKey(1) & 0xff == ord('q')):
        break

cam.release()