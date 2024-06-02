from vpython import *
from time import *

mRadius = 0.5
wallThickness = 0.1
roomWidth = 10
roomDepth = 8
roomHeight = 10

ceiling = box(pos=vector(0,roomHeight/2,0),color=color.blue, size=vector(roomWidth,wallThickness,roomDepth))
floor = box(pos=vector(0,-roomHeight/2,0),color=color.blue, size=vector(roomWidth,wallThickness,roomDepth))
rightWall = box(pos=vector(roomWidth/2,0,0),color=color.blue, size=vector(wallThickness,roomHeight,roomDepth))
leftWall = box(pos=vector(-roomWidth/2,0,0),color=color.blue, size=vector(wallThickness,roomHeight,roomDepth))
backWall = box(pos=vector(0,0,-roomDepth/2),color=color.blue, size=vector(roomWidth,roomHeight,wallThickness))

marble = sphere(color=color.red, radius = mRadius)
deltaX = 0.1
deltaY = 0.1
deltaZ = 0.1

xPos = 0
yPos = 0
zPos = 0

while True:
    rate(50)
    xPos += deltaX
    yPos += deltaY
    zPos += deltaZ
    Xrme = xPos+mRadius
    Xlme = xPos-mRadius
    Ytme = yPos+mRadius
    Ybme = yPos-mRadius
    Zbme = zPos-mRadius
    Zfme = zPos+mRadius
    Rwe = (roomWidth/2)-(wallThickness/2)
    Lwe = (-roomWidth/2)+(wallThickness/2)
    Cwe = (roomHeight/2)-(wallThickness/2)
    Flwe = (-roomHeight/2)+(wallThickness/2)
    Bwe = (-roomDepth/2)+(wallThickness/2)
    Fwe = (roomDepth/2)-(wallThickness/2)


    if ((Xrme >= Rwe) or (Xlme <= Lwe)):
        deltaX *= -1
    if ((Ytme >= Cwe) or (Ybme <= Flwe)):
        deltaY *= -1
    if ((Zfme >= Fwe) or (Zbme <= Bwe)):
        deltaZ *= -1

    marble.pos = vector(xPos,yPos,zPos)

