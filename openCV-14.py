import cv2
print(cv2.__version__)

# openCV14.py - uses trackbars to maipulate the size and position of the live webcam window itself
################           Press the Q key to Exit Camera       #################################

width = 1280
height = int((width * 9)/16)
xPos = 0
yPos = 0

def myCallBack1(val):
    global xPos
    print('xPos: ', val)
    xPos = val

def myCallBack2(val):
    global yPos
    print('yPos: ', val)
    yPos = val

def myCallBack3(val):
    print('width: ', val)
    width = val
    height = int((width * 9)/16)
    cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
    cam.set(cv2.CAP_PROP_FRAME_HEIGHT, height)



cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
cam.set(cv2.CAP_PROP_FPS, 30)
cam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))

cv2.namedWindow('my Trackbars')
cv2.moveWindow('my Trackbars', width,0)
cv2.resizeWindow('my Trackbars', 400, 150)
cv2.createTrackbar('xPos','my Trackbars', 0, 2000, myCallBack1)
cv2.createTrackbar('yPos','my Trackbars', 0, 1000, myCallBack2)
cv2.createTrackbar('width','my Trackbars', width, 1920, myCallBack3)


while True:
    
    ignore, frame = cam.read()
    cv2.imshow('My Webcam', frame)
    cv2.moveWindow('My Webcam', xPos, yPos)

    if(cv2.waitKey(1) & 0xff == ord('q')):
        break

cam.release()