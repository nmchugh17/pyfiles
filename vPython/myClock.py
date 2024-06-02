# My Attempt #########################################
from vpython import *
import numpy as np
import time

clockR = 5
clockL = 0.5
secPntT = 0.1
minPntT = 0.2
hourPntT = 0.3
secArrowL = clockR*0.9
minArrowL = clockR*0.8
hourArrowL = clockR*0.5

clock = cylinder(pos = vector(0,0,0), axis=vector(0, 0, 1), color = color.white, length = clockL, radius = clockR)
# clockFrame = cylinder(color = color.black, length = 3, radius = 3.5)

for myHour in np.linspace(0,2*np.pi,13):  
    hour = box(pos = vector((clockR*0.8)*np.cos(myHour), (clockR*0.8)*np.sin(myHour),0.5), axis=vector((clockR*0.8)*np.cos(myHour), (clockR*0.8)*np.sin(myHour), 0), color = color.red, size = vector(0.8,0.3,0.2))

for myMinute in np.linspace(0,2*np.pi,61):
    minute = box(pos = vector((clockR*0.8)*np.cos(myMinute), (clockR*0.8)*np.sin(myMinute),0.5), axis=vector((clockR*0.8)*np.cos(myMinute), (clockR*0.8)*np.sin(myMinute), 0), color = color.black, size = vector(0.5,0.1,0.1))

secArrow = arrow(axis = vector(1,0,0), pos = vector(0,0,0.5),color = color.red, length = secArrowL, shaftwidth = secPntT)
minuteArrow = arrow(axis = vector(1,0,0), pos = vector(0,0,0.5),color = color.blue, length = minArrowL, shaftwidth = minPntT)
hourArrow = arrow(axis = vector(1,0,0), pos = vector(0,0,0.5),color = color.green, length = hourArrowL, shaftwidth = hourPntT)

while True:
    mySeconds = (2*np.pi)/(60/(time.localtime().tm_sec+1))
    secArrow.axis = vector(secArrowL*np.sin(mySeconds), secArrowL*np.cos(mySeconds),0)
    secArrow.length = secArrowL

    myMinutes = ((2*np.pi)/((60*60)/(time.localtime().tm_sec+1))) + (2*np.pi)/(60/(time.localtime().tm_min+1))
    minuteArrow.axis = vector(minArrowL*np.sin(myMinutes), minArrowL*np.cos(myMinutes),0)
    minuteArrow.length = minArrowL

    myHours = (2*np.pi)/((60*60*24)/(time.localtime().tm_sec+1)) + (2*np.pi)/(24/(time.localtime().tm_hour+1))
    hourArrow.axis = vector(hourArrowL*np.sin(myHours), hourArrowL*np.cos(myHours),0)
    hourArrow.length = hourArrowL

    print(time.localtime().tm_min)
        
        
# Solution #########################################
# from vpython import *
# import numpy as np

# clockR = 2
# clockT = clockR/10
# majorTickL = clockR/7
# majorTickT = 2*np.pi*clockR/400
# majorTickW = clockT * 1.2

# minorTickL = clockR/12
# minorTickT = 2*np.pi*clockR/600
# minorTickW = clockT * 1.2

# for theta in np.linspace(0,2*np.pi,13):    
#     majorTick = box(axis=vector(clockR*np.cos(theta), clockR*np.sin(theta), 0), color = color.black, length = majorTickL, width = majorTickW, height = majorTickT, pos = vector((clockR-majorTickL/2)*np.cos(theta), (clockR-majorTickL/2)*np.sin(theta),0))

# for theta in np.linspace(0,2*np.pi,61):    
#     minorTick = box(axis=vector(clockR*np.cos(theta), clockR*np.sin(theta), 0), color = color.black, length = minorTickL, width = minorTickW, height = minorTickT, pos = vector((clockR-minorTickL/2)*np.cos(theta), (clockR-minorTickL/2)*np.sin(theta),0))

# clockFace = cylinder(axis=vector(0, 0, 1), pos = vector(0,0,-clockT/2), color = vector(0,1,0.8), length = clockT, radius = clockR)

# while True:
#     pass