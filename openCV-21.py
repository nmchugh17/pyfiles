import cv2
print(cv2.__version__)

# openCV20.py - using the classifiers we highlight face or eye features in the webcam
################           Press the Q key to Exit Camera       #################################

width=1280
height=720
cam=cv2.VideoCapture(0,cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,height)
cam.set(cv2.CAP_PROP_FPS, 30)
cam.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc(*'MJPG'))

faceCascade = cv2.CascadeClassifier('../Python/haar/haarcascade_frontalface_default.xml')
eyesCascade = cv2.CascadeClassifier('../Python/haar/haarcascade_eye.xml')

while True:
    ignore,  frame = cam.read()
    frameGray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(frameGray, 1.3, 5)
    for face in faces:
        x,y,w,h = face
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),3)
        
    cv2.imshow('my WEBcam', frame)
    cv2.moveWindow('my WEBcam',0,0)
    if cv2.waitKey(1) & 0xff ==ord('q'):
        break
cam.release()