import cv2
print(cv2.__version__)

# openCV7.py - adds text and shapes to a live webcam feed
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
cam.set(cv2.CAP_PROP_FPS, 30)
cam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))

while True:
    ignore, frame = cam.read()
    frame[140:220,250:390]=(255,0,0)
    cv2.rectangle(frame,upperLeft,lowerRight,(0,255,0),lineWidth)
    cv2.circle(frame,(int(width/2),int(height/2)),myRadius,myColor,myThickness)
    cv2.putText(frame,myText,(120,60),myFont,2,(0,0,255),2)
    cv2.imshow('My Webcam', frame)
    cv2.moveWindow('My Webcam', 0, 0)
    if(cv2.waitKey(1) & 0xff == ord('q')):
        break

cam.release()