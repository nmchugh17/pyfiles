import cv2
import face_recognition as fr

# openCV23.py - using demo images and text we highlight and identify specific peoples faces

font = cv2.FONT_HERSHEY_SIMPLEX

donFace = fr.load_image_file('../Python/demoImages/known/Donald Trump.jpg')
faceLoc = fr.face_locations(donFace)[0]
donFaceEncode = fr.face_encodings(donFace)[0]

nancyFace = fr.load_image_file('..Python/demoImages/known/Nancy Pelosi.jpg')
faceLoc = fr.face_locations(nancyFace)[0]
nancyFaceEncode = fr.face_encodings(nancyFace)[0]

penceFace = fr.load_image_file('../Python/demoImages/known/Mike Pence.jpg')
faceLoc = fr.face_locations(penceFace)[0]
penceFaceEncode = fr.face_encodings(penceFace)[0]

knownEncodings = [donFaceEncode, nancyFaceEncode, penceFaceEncode] 
names = ['Donald Trump', 'Nancy Pelosi', 'Mike Pence']

unknownFace = fr.load_image_file('C:/Users/Niall McHugh/Python/demoImages/unknown/u1.jpg')
unknownFaceBGR = cv2.cvtColor(unknownFace,cv2.COLOR_RGB2BGR)
faceLocations = fr.face_locations(unknownFace)
unknownEncodings = fr.face_encodings(unknownFace, faceLocations)

for faceLocation, unknownEncoding in zip(faceLocations, unknownEncodings):
    top, right, bottom, left = faceLocation
    print(faceLocation)
    cv2.rectangle(unknownFaceBGR,(left,top),(right,bottom),(255,0,0),3)
    name='Unknown Person'
    matches = fr.compare_faces(knownEncodings, unknownEncoding)
    print(matches)

    if True in matches:
        matchIndex = matches.index(True)
        print(matchIndex)
        print(names[matchIndex])
        name = names[matchIndex]
    cv2.putText(unknownFaceBGR,name,(left,top),font,0.75,(0,0,255),2)

cv2.imshow('My Faces', unknownFaceBGR)
cv2.waitKey(5000)