import cv2
print(cv2.__version__)

# openCV13.py - created trackbars that manipulate a circle animation within the live webcam feed and can then change its size and position

################           Press the Q key to Exit Camera       #################################



width =1280
height = 720
myRad = 25
myThick = 1
xPos = int(width/2)
yPos = int(height/2)

def myCallBack1(val):
    global xPos
    print('xPos: ', val)
    xPos = val

def myCallBack2(val):
    global yPos
    print('yPos: ', val)
    yPos = val

def myCallBack3(val):
    global myRad
    print('yPos: ', val)
    myRad = val

def myCallBack4(val):
    global myThick
    print('yPos: ', val)
    myThick = val


cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
cam.set(cv2.CAP_PROP_FPS, 30)
cam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))

cv2.namedWindow('myTrackbars')
cv2.resizeWindow('myTrackbars', 400, 150)
cv2.moveWindow('myTrackbars', width,0)
cv2.createTrackbar('xPos','myTrackbars', xPos, 1920, myCallBack1)
cv2.createTrackbar('yPos','myTrackbars', yPos, 1080, myCallBack2)
cv2.createTrackbar('radius','myTrackbars', myRad, int(height/2), myCallBack3)
cv2.createTrackbar('thick','myTrackbars', myThick, 7, myCallBack4)


while True:
    
    ignore, frame = cam.read()
    if myThick == 0:
        myThick = -1
    cv2.circle(frame,(xPos,yPos),myRad,(255,0,0),myThick)
    cv2.imshow('My Webcam', frame)
    cv2.moveWindow('My Webcam', 0, 0)

    if(cv2.waitKey(1) & 0xff == ord('q')):
        break

cam.release()