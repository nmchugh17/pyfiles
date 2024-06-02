import cv2 
import face_recognition as fr

# openCV24.py - in the demo images folder added our own images and coded to recognise people i know with the webcam - 
# NOTE: removed pics other than my own from the demo image folder
# NOTE: image is sluggish would need to use GPU for better performance
################           Press the Q key to Exit Camera       #################################

font = cv2.FONT_HERSHEY_SIMPLEX
width = 1280
height = 720

cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)

cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
cam.set(cv2.CAP_PROP_FPS, 30)
cam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))

niallFace = fr.load_image_file('../Python/demoImages/known/niall.png')
faceLoc = fr.face_locations(niallFace)[0]
niallFaceEncode = fr.face_encodings(niallFace)[0]

# louiseFace = fr.load_image_file('../Python/demoImages/known/louise.png')
# faceLoc = fr.face_locations(louiseFace)[0]
# louiseFaceEncode = fr.face_encodings(louiseFace)[0]

# roisinFace = fr.load_image_file('../Python/demoImages/known/roisin.png')
# faceLoc = fr.face_locations(roisinFace)[0]
# roisinFaceEncode = fr.face_encodings(roisinFace)[0]

# seanFace = fr.load_image_file('../Python/demoImages/known/sean.png')
# faceLoc = fr.face_locations(seanFace)[0]
# seanFaceEncode = fr.face_encodings(seanFace)[0]

# coraFace = fr.load_image_file('../Python/demoImages/known/cora.png')
# faceLoc = fr.face_locations(coraFace)[0]
# coraFaceEncode = fr.face_encodings(coraFace)[0]

# knownEncodings = [niallFaceEncode, louiseFaceEncode, roisinFaceEncode, seanFaceEncode, coraFaceEncode] 
knownEncodings = [niallFaceEncode] 
names = ['Niall', 'Louise', 'Roisin', 'Sean', 'Cora']



while True:
    ignore, unknownFace = cam.read()

    unknownFaceRGB = cv2.cvtColor(unknownFace,cv2.COLOR_BGR2RGB)
    faceLocations = fr.face_locations(unknownFaceRGB)
    unknownEncodings = fr.face_encodings(unknownFaceRGB, faceLocations)

    for faceLocation, unknownEncoding in zip(faceLocations, unknownEncodings):
        top, right, bottom, left = faceLocation
        # print(faceLocation)
        cv2.rectangle(unknownFace,(left,top),(right,bottom),(255,0,0),3)
        name='Unknown Person'
        matches = fr.compare_faces(knownEncodings, unknownEncoding)
        # print(matches)

        if True in matches:
            matchIndex = matches.index(True)
            # print(matchIndex)
            # print(names[matchIndex])
            name = names[matchIndex]
        cv2.putText(unknownFace,"Hello " + name,(left,bottom),font,0.75,(0,0,255),2)

    cv2.imshow('My Faces', unknownFace)
    cv2.moveWindow('My Faces',0,0)

    if cv2.waitKey(1) & 0xff == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()