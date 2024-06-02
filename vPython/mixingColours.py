from vpython import *
import numpy as np

# Attempt 1 #########################################################
red = 0
green = 0
blue = 0
myColor = 'red'
myDelta = 0.01

mySphere = sphere(radius = 1, color = vector(red,green,blue))

while True:
    rate(10)
    if red + green + blue < 1:
        myColor = 'red'
    elif red + green + blue >= 1 and red + green + blue < 2:
        myColor = 'green'
    elif red + green + blue >= 2 and red + green + blue < 3:
        myColor = 'blue'
    elif red + green + blue >= 3 or red + green + blue <= 0:
        myDelta *= -1
        
    if myColor == 'red':
        red += myDelta
        mySphere.color = vector(np.round(red,2), np.round(green,2), np.round(blue,2))
    elif myColor == 'green':
        green += myDelta
        mySphere.color = vector(np.round(red,2), np.round(green,2), np.round(blue,2))
    elif myColor == 'blue':
        blue += myDelta
        mySphere.color = vector(np.round(red,2), np.round(green,2), np.round(blue,2))

