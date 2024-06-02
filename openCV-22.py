
import cv2
import time

print(cv2.__version__)

# openCV22.py - using the classifiers we highlight both face and eye features in the webcam
################           Press the Q key to Exit Camera       #################################

width=1280
height=720

fps = 10
timeStamp = time.time()


cam=cv2.VideoCapture(0,cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,height)
cam.set(cv2.CAP_PROP_FPS, 30)
cam.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc(*'MJPG'))

faceCascade = cv2.CascadeClassifier('haar\haarcascade_frontalface_default.xml')
eyeCascade = cv2.CascadeClassifier('haar\haarcascade_eye.xml')

while True:


    ignore,  frame = cam.read()
    frameGray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(frameGray, 1.3, 5)

    for face in faces:
        x,y,w,h = face
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),3)
        frameROI = frame[y:y+h, x:x+w]
        frameROIGray = cv2.cvtColor(frameROI, cv2.COLOR_BGR2GRAY)

        eyes = eyeCascade.detectMultiScale(frameROIGray, 1.3, 5)
        for eye in eyes:
            xeye,yeye,weye,heye = eye
            cv2.rectangle(frame[y:y+h, x:x+w],(xeye,yeye),(xeye+weye,yeye+heye),(0,0,255),3)

    loopTime = time.time()-timeStamp
    timeStamp = time.time()
    fpsNEW = 1/loopTime
    fps = fps*0.9 + fpsNEW *0.1
    fps = int(fps)
    
    cv2.putText(frame,str(fps) + ' fps',(5,30),cv2.FONT_HERSHEY_PLAIN,2,(255,0,0),2)

    cv2.imshow('my WEBcam', frame)
    cv2.moveWindow('my WEBcam',0,0)
    if cv2.waitKey(1) & 0xff ==ord('q'):
        break
cam.release()