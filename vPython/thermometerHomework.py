from vpython import *
import numpy as np
from threading import Thread

class thermometer:

    def __init__(self,xPos,yPos,zPos, myDelta):
        self.xPos = xPos
        self.yPos = yPos
        self.zPos = zPos
        self.myDelta = myDelta

        self.bulb = sphere(pos = vector(self.xPos,self.yPos,self.zPos), radius = 3, color = color.white, opacity = 0.1)
        self.mercuryball = sphere(pos = vector(self.xPos,self.yPos,self.zPos), radius = 2.5, color = color.red)

        self.glassCylinder = cylinder(pos = vector(self.xPos,self.yPos+2,self.zPos), axis = vector(0,1,0), radius = 2, length = 20, color = color.white, opacity = 0.1)
        self.mercuryCylinder = cylinder(pos = vector(self.xPos,self.yPos+0.5,self.zPos), axis = vector(0,1,0), radius = 1.5, length = 2, color = color.red)

        self.glassTop = sphere(pos = vector(self.xPos,self.yPos+22,self.zPos), radius = 2, color = color.white, opacity = 0.1)

        for tick in np.linspace(2,20,20):
            box(size=vector(2,0.1,0.5), pos = vector(self.xPos,self.yPos+tick+0.5,self.zPos+2), color=color.black)
        
        def tempMove():
            while True:
                rate(50)
                self.mercuryCylinder.length = self.mercuryCylinder.length+self.myDelta
            
                if self.mercuryCylinder.length >=20 or self.mercuryCylinder.length <= 0.1:
                    self.myDelta = self.myDelta*(-1)

        tempThread = Thread(target = tempMove)
        tempThread.daemon = True
        tempThread.start()

scene = canvas(width = 800, height = 600)
therm1 = thermometer(-5,-10,0, 0.1)
therm2 = thermometer(5,-10,0, 0.2)



