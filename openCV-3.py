import cv2
print(cv2.__version__)

# openCV3.py - resizes the camera frame that appears on the window and opens muplie frames filling the comouter screen
################           Press the Q key to Exit Camera       #################################

width = 160
height = 90

cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
cam.set(cv2.CAP_PROP_FPS, 30)
cam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))

while True:
    ignore, frame = cam.read()

    grayFrame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    cv2.imshow('my WEBcam', frame)
    cv2.moveWindow('my WEBcam', 0, 0)

    cv2.imshow('my WEBcam 2', frame)
    cv2.moveWindow('my WEBcam 2', width*2, 0)

    cv2.imshow('my WEBcam 3', frame)
    cv2.moveWindow('my WEBcam 3', width*4, 0)

    cv2.imshow('my WEBcam 4', frame)
    cv2.moveWindow('my WEBcam 4', width*6, 0)

    cv2.imshow('my WEBcam 5', frame)
    cv2.moveWindow('my WEBcam 5', width*8, 0)

    cv2.imshow('my WEBcam 6', frame)
    cv2.moveWindow('my WEBcam 6', width*10, 0)

    cv2.imshow('my WEBcam 7', frame)
    cv2.moveWindow('my WEBcam 7', 0, height*4)

    cv2.imshow('my WEBcam 8', frame)
    cv2.moveWindow('my WEBcam 8', width*2, height*4)

    cv2.imshow('my WEBcam 9', frame)
    cv2.moveWindow('my WEBcam 9', width*4, height*4)

    cv2.imshow('my WEBcam 10', frame)
    cv2.moveWindow('my WEBcam 10', width*6, height*4)

    cv2.imshow('my WEBcam 11', frame)
    cv2.moveWindow('my WEBcam 11', width*8, height*4)

    cv2.imshow('my WEBcam 12', frame)
    cv2.moveWindow('my WEBcam 12', width*10, height*4)

    cv2.imshow('my WEBcam 13', frame)
    cv2.moveWindow('my WEBcam 13', 0, height*8)

    cv2.imshow('my WEBcam 14', frame)
    cv2.moveWindow('my WEBcam 14', width*2, height*8)

    cv2.imshow('my WEBcam 15', frame)
    cv2.moveWindow('my WEBcam 15', width*4, height*8)

    cv2.imshow('my WEBcam 16', frame)
    cv2.moveWindow('my WEBcam 16', width*6, height*8)

    cv2.imshow('my WEBcam 17', frame)
    cv2.moveWindow('my WEBcam 17', width*8, height*8)

    cv2.imshow('my WEBcam 18', frame)
    cv2.moveWindow('my WEBcam 18', width*10, height*8)

    if(cv2.waitKey(1) & 0xff == ord('q')):
        break

cam.release()