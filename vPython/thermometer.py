from vpython import *
import numpy as np

xPos = 0
yPos = -10
zPos = 0

scene = canvas(width = 800, height = 600)

bulb = sphere(pos = vector(xPos,yPos,zPos), radius = 3, color = color.white, opacity = 0.1)
mercuryball = sphere(pos = vector(xPos,yPos,zPos), radius = 2.5, color = color.red)

glassCylinder = cylinder(pos = vector(xPos,yPos+2,zPos), axis = vector(0,1,0), radius = 2, length = 20, color = color.white, opacity = 0.1)
mercuryCylinder = cylinder(pos = vector(xPos,yPos+0.5,zPos), axis = vector(0,1,0), radius = 1.5, length = 2, color = color.red)

glassTop = sphere(pos = vector(xPos,yPos+22,zPos), radius = 2, color = color.white, opacity = 0.1)

for tick in np.linspace(2,20,20):
    box(size=vector(2,0.1,0.5), pos = vector(xPos,yPos+tick+0.5,zPos+2), color=color.black)

while True:
    for myLength in np.linspace(2,20,1000):
        rate(250)
        mercuryCylinder.length = myLength
    
    for myLength in np.linspace(20,2,1000):
        rate(250)
        mercuryCylinder.length = myLength
    