import cv2
import time
print(cv2.__version__)

# openCV8.py - rougly calculates and display the current frame rate on a live webcam
################           Press the Q key to Exit Camera       #################################

width = 640
height = 360
myRadius = 30
myColor = (0,0,0)
myThickness = 2
myText = 'Niall is here'
myFont = cv2.FONT_HERSHEY_COMPLEX
upperLeft = (250,140) 
lowerRight = (390,220)
lineWidth = 4

cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
cam.set(cv2.CAP_PROP_FPS, 10)
cam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))
tLast = time.time()
time.sleep(.1)
fpsFILT = 30
while True:
    dT = time.time()-tLast
    fps=1/dT
    fpsFILT=fpsFILT*0.9+fps*0.1
    print(fps)
    tLast=time.time()
    ignore, frame = cam.read()
    # cv2.putText(frame,myText,(120,125),myFont,2,(0,0,255),2)
    cv2.rectangle(frame,(0,0),(120,40),(255,0,255),-1)
    cv2.putText(frame,str(int(fpsFILT)) + ' fps',(5,30),myFont,1,(0,255,255),1)
    cv2.imshow('My Webcam', frame)
    cv2.moveWindow('My Webcam', 0, 0)
    if(cv2.waitKey(1) & 0xff == ord('q')):
        break

cam.release()