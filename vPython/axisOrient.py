from vpython import *
import numpy as np

arrowL = 2
arrowT = 0.02
pntT = 0.04
theta = np.pi/4
Xarrow = arrow(axis = vector(1,0,0),color = color.red, length = arrowL, shaftwidth = arrowT)
Yarrow = arrow(axis = vector(0,1,0),color = color.green, length = arrowL, shaftwidth = arrowT)
Zarrow = arrow(axis = vector(0,0,1), color = color.blue, length = arrowL, shaftwidth = arrowT)
# Zarrow.axis = vector(0,0,1)
# Zarrow.length = arrowL
pntArrow=arrow(axis=vector(arrowL*np.cos(theta), arrowL*np.sin(theta),0), color = color.orange, length = arrowL, shaftwidth = pntT)

while True:
    for myAngle in np.linspace(0,2*np.pi,1000):
        rate(50)
        pntArrow.axis = vector(arrowL*np.cos(myAngle), arrowL*np.sin(myAngle),0)
        pntArrow.length = arrowL


    