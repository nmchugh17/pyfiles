from time import *
from threading import Thread

def myBox(d):
    while True:
        print("....My box is Open: ")
        sleep(d)
        print("....My box is Closed: ")
        sleep(d)
    
def myLED(d):  
    while True:  
        print("My LED is On: ")
        sleep(d)
        print("My LED is Off: ")
        sleep(d)

delayBox=5
delayLED=1
boxThread = Thread(target = myBox, args=(delayBox,))
LEDThread = Thread(target = myLED, args=(delayLED,))

boxThread.daemon = True
LEDThread.daemon = True

boxThread.start()
LEDThread.start()

j = 0
while True:
    print(j)
    j+=1
    sleep(2)