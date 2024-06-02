import cv2
print(cv2.__version__)

# openCV10.py - live webcam in grayscale with a colour square moving about the live window (look closely depending on lighting)
################           Press the Q key to Exit Camera       #################################

width =1280
height = 720

rowStart = int(height/2)
rowNums = int(height/4)
rowEnd = rowStart + rowNums
colStart = int(width/2)
colNums = int(width/4)
colEnd = colStart + colNums

xDelta = 1
yDelta = 1


cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
cam.set(cv2.CAP_PROP_FPS, 30)
cam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))


while True:
    
    ignore, frame = cam.read()
    frameROI = frame[rowStart:rowEnd,colStart:colEnd]
    # frameROI = frame[120:210,230:390]
    frameROIGray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    frame =  cv2.cvtColor(frameROIGray,cv2.COLOR_GRAY2BGR)

    frame[rowStart:rowEnd,colStart:colEnd] = frameROI
    # frame[0:60,0:140] = frameROIBGR
    
    cv2.imshow('My Webcam', frame)
    cv2.moveWindow('My Webcam', 0, 0)

    rowStart += yDelta
    rowEnd += yDelta
    colStart += xDelta
    colEnd += xDelta


    if (rowStart+yDelta) <= 0 or (rowStart+rowNums+yDelta) >= height :
        yDelta *= -1
    if (colStart+xDelta) <= 0 or (colStart+colNums+xDelta) >= width :
        xDelta *= -1

    if(cv2.waitKey(1) & 0xff == ord('q')):
        break

cam.release()