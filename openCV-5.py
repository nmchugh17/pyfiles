import cv2
import numpy as np

print(cv2.__version__)

# openCV5.py - we manipulate the colouring on in the webcam frame creating a checkerboard effect
################           Press the Q key to Exit Camera       #################################

squareEnd = 400
pos = []

frame = np.zeros([squareEnd,squareEnd,3],dtype=np.uint8)

def checkboard(boardLength):
    for x in np.linspace(0,boardLength,8):
        pos.append(int(x))

    for i in range(0,8,1):
        if i < 7:
            if i%2 > 0:
                frame[pos[i]:pos[i+1],:] = (0,0,255) 

        for j in range(0,8,2):
            if i < 7 and j < 7:
                if i%2 > 0:
                    frame[pos[i]:pos[i+1],pos[j]:pos[j+1]] = (0,0,0)
                elif i%2 == 0:
                    frame[pos[i]:pos[i+1],pos[j]:pos[j+1]] = (0,0,255)

checkboard(squareEnd)
        
while True:   
    cv2.imshow("My Window", frame)
    if cv2.waitKey(1) & 0xff == ord("q"):
        break




    


