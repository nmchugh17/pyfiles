import cv2
print(cv2.__version__)

# openCV4.py - in ther terminal enter how many rows and columns you want and this will display that number of webcam windows on the screen
################           Press the Q key to Exit Camera       #################################

width = 1280
height = 720
rows = int(input("How many rows do you want? "))
columns = int(input("And How many columns do you want? "))

cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
cam.set(cv2.CAP_PROP_FPS, 30)
cam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))

while True:
    ignore, frame = cam.read()
    frame = cv2.resize(frame,(int(width/columns),int(height/columns)))
    for i in range(0,rows,1):
        for j in range(0,columns,1):
            windName = "Window "+str(i)+" x "+str(j)
            cv2.imshow(windName, frame)
            cv2.moveWindow(windName, int(width/columns)*j, int(height/columns+30)*i)
 
    

    

    if(cv2.waitKey(1) & 0xff == ord('q')):
        break

cam.release()