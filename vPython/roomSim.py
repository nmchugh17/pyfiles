from vpython import *
from time import *

mRadius = 0.75
wallThickness = 0.1
roomWidth = 15
roomDepth = 5
roomHeight = 10

ceiling = box(pos=vector(0,roomHeight/2,0),color=color.blue, size=vector(roomWidth,wallThickness,roomDepth))
floor = box(pos=vector(0,-roomHeight/2,0),color=color.blue, size=vector(roomWidth,wallThickness,roomDepth))
rightWall = box(pos=vector(roomWidth/2,0,0),color=color.blue, size=vector(wallThickness,roomHeight,roomDepth))
leftWall = box(pos=vector(-roomWidth/2,0,0),color=color.blue, size=vector(wallThickness,roomHeight,roomDepth))
backWall = box(pos=vector(0,0,-roomDepth/2),color=color.blue, size=vector(roomWidth,roomHeight,wallThickness))

marble = sphere(color=color.red, radius = mRadius)
deltaX = 0.1
xPos = 0

while True:
    rate(100)
    xPos += deltaX
    if xPos > ((roomWidth/2)-mRadius-wallThickness) or xPos < -((roomWidth/2)-mRadius-wallThickness):
        deltaX *= -1
    marble.pos = vector(xPos,0,0)

