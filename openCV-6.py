import cv2

# openCV6.py - we manipulate the colouring on in the webcam frame creating a checkerboard effect this time accepting inputs for window size and number of squares
################           Press the Q key to Exit Camera       #################################

print(cv2.__version__)
import numpy as np

boardSize = int(input('What size is your board? (Number in Pixels): '))
numSquares = int(input('And, How many squares? '))
squareSize = int(boardSize/numSquares)

darkColor = (0,0,0)
lightColor = (0,0,255)
nowColor = darkColor

while True:
    x = np.zeros([boardSize,boardSize,3], dtype=np.uint8)

    for row in range(0,numSquares):
        for column in range(0,numSquares):
            x[squareSize*row:squareSize*(row+1),squareSize*column:squareSize*(column+1)] = nowColor
            if nowColor == darkColor:
                nowColor = lightColor
            else:
                nowColor = darkColor
                
        if nowColor == darkColor:
            nowColor = lightColor
        else:
            nowColor = darkColor

    cv2.imshow('My Checkboard', x)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break


