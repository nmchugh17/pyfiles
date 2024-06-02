import os
import cv2
import face_recognition as fr

# openCV25.py - file manipulation - unfinished
imageDir = '../Python/demoImages/known'

for root, dirs, files in os.walk(imageDir):
    print('my working folder (root): ', root)
    print('dirs in root: ', dirs)
    print('my files in root: ', files)