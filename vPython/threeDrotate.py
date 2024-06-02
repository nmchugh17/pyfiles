# HOMEWORK ATTEMPT #################################################
# from vpython import *
# import numpy as np

# arrowL = 2
# arrowT = 0.02
# pntT = 0.04

# Xarrow = arrow(axis = vector(1,0,0),color = color.red, length = arrowL, shaftwidth = arrowT)
# Yarrow = arrow(axis = vector(0,1,0),color = color.green, length = arrowL, shaftwidth = arrowT)
# Zarrow = arrow(axis = vector(0,0,1), color = color.blue, length = arrowL, shaftwidth = arrowT)

# Parrow=arrow(vector(1,0,0), color = color.orange, length = arrowL, shaftwidth = pntT)

# count = 0

# while True:
    
#     for myAngle in np.linspace(0,2*np.pi,1000):
#         rate(50)
#         # print(count)
#         if count == 0:
#             Parrow.axis = vector(arrowL*np.cos(myAngle), arrowL*np.sin(myAngle),0)
#             Parrow.length = arrowL
#         if count == 1:
#             Parrow.axis = vector(0, arrowL*np.sin(myAngle),arrowL*np.cos(myAngle))
#             Parrow.length = arrowL
#         if count == 2:
#             Parrow.axis = vector(arrowL*np.sin(myAngle),0,arrowL*np.cos(myAngle))
#             Parrow.length = arrowL
#         if count == 3:
#             count = 0

#         if myAngle == 2*np.pi:
#             count+=1

# HOMEWORK SOLUTION #################################################
from vpython import *
import numpy as np

arrowL = 2
arrowT = 0.02
pntT = 0.04
bRadius = 0.05

Xarrow = arrow(axis = vector(1,0,0),color = color.red, length = arrowL, shaftwidth = arrowT)
Yarrow = arrow(axis = vector(0,1,0),color = color.green, length = arrowL, shaftwidth = arrowT)
Zarrow = arrow(axis = vector(0,0,1), color = color.blue, length = arrowL, shaftwidth = arrowT)

Parrow = arrow(axis = vector(1,0,0), color = color.orange, length = arrowL, shaftwidth = pntT)

myBall = sphere(make_trail=True, trail_color = color.orange, radius= bRadius, color = color.red, pos = vector(arrowL,0,0))
while True:
    
    for myAngle in np.linspace(0,2*np.pi,1000):
        rate(50)
        Parrow.axis = vector(arrowL*np.cos(myAngle), arrowL*np.sin(myAngle),0)
        Parrow.length = arrowL
        myBall.pos = vector(arrowL*np.cos(myAngle), arrowL*np.sin(myAngle),0)
    for myAngle in np.linspace(0,5*np.pi/2,1000):
        rate(50)
        Parrow.axis = vector(arrowL*np.cos(myAngle),0,arrowL*np.sin(myAngle))
        Parrow.length = arrowL
        myBall.pos = vector(arrowL*np.cos(myAngle),0,arrowL*np.sin(myAngle))
    for myAngle in np.linspace(0,2*np.pi,1000):
        rate(50)
        Parrow.axis = vector(0, arrowL*np.sin(myAngle),arrowL*np.cos(myAngle))
        Parrow.length = arrowL
        myBall.pos = vector(0, arrowL*np.sin(myAngle),arrowL*np.cos(myAngle))
    for myAngle in np.linspace(np.pi/2,2*np.pi,1000):
        rate(50)
        Parrow.axis = vector(arrowL*np.cos(myAngle), 0, arrowL*np.sin(myAngle))
        Parrow.length = arrowL
        myBall.pos = vector(arrowL*np.cos(myAngle), 0, arrowL*np.sin(myAngle))


    