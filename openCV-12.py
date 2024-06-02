import cv2
print(cv2.__version__)

# openCV12.py - With the main webcam window open click and drag to select subsection region of interest to open in new window - For this to work: when running need to hold left click down then drag across the webcam window before releasing
################           Press the Q key to Exit Camera       #################################

width =1280
height = 720

evt = 0

def mouseClick(event,xPos,yPos,flags,params):
    global evt 
    global pnt1
    global pnt2
    if event == cv2.EVENT_LBUTTONDOWN:
        print('at position ', xPos, yPos)
        print(event)
        pnt1 = (xPos, yPos)
        evt=event
    if event == cv2.EVENT_LBUTTONUP:
        print(event)
        pnt2 = (xPos, yPos)
        evt=event
    if event == cv2.EVENT_RBUTTONUP:
        evt=event


cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
cam.set(cv2.CAP_PROP_FPS, 30)
cam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))

cv2.namedWindow('My Webcam')
cv2.setMouseCallback('My Webcam', mouseClick)

while True:
    
    ignore, frame = cam.read()
    
    #print(frameROI)
    if evt == 4:
        cv2.rectangle(frame,pnt1,pnt2,(0,0,255),2)
        frameROI = frame[pnt1[1]:pnt2[1],pnt1[0]:pnt2[0]]
        cv2.imshow('My ROI', frameROI)
        cv2.moveWindow('My ROI', width, 0)
    if evt == 5:
        cv2.destroyWindow('My ROI')
        evt = 0
 
    cv2.imshow('My Webcam', frame)
    cv2.moveWindow('My Webcam', 0, 0)

    if(cv2.waitKey(1) & 0xff == ord('q')):
        break

cam.release()