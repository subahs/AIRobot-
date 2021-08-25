import cv2
import dlib
import face_recognition
import numpy
import os
from os import environ
import time
from datetime import datetime
def suppress_qt_warnings():
    environ["QT_DEVICE_PIXEL_RATIO"] = "0"
    environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"
    environ["QT_SCREEN_SCALE_FACTORS"] = "1"
    environ["QT_SCALE_FACTOR"] = "1"

if __name__ == "__main__":
    suppress_qt_warnings()
    # Init QT etc...

path = 'images'
images = []
names = []
faceCoordinates = []
myList = os.listdir(path)
for i in myList :
    images.append(cv2.imread(f'{path}/{i}'))
    names.append(os.path.splitext(i)[0])
print('Images loaded and names parsed')
print(myList)
def attendance(name) :
    with open('records/attendance.csv', 'r+') as f:
        myDataList = f.readlines()
        nameList = []
        for line in myDataList :
            entry = line.split(',')
            nameList.append(entry[0])
        if name not in nameList :
            now = datetime.now()
            dtString = now.strftime('%H:%M:%S')
            f.writelines(f'\n {name},{dtString}')
            print(f'{name} attended at {dtString}')

def findEncodings(images) :
    encodingList = []
    for i in images :
        i = cv2.cvtColor(i, cv2.COLOR_BGR2RGB)
        encodingList.append(face_recognition.face_encodings(i)[0])
    return encodingList

print('Face Data Encoding Completed')
encodingList = findEncodings(images)
webcam = cv2.VideoCapture(0)
lamo = []
def faceRec():
    temp = 0
    done = False
    while not done :
        success, frame = webcam.read()
        print(success)
        convertedImage = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        faceCoordinates = face_recognition.face_locations(convertedImage)
        for i in faceCoordinates :
            (x, y, w, h) = i
            cv2.rectangle(frame, (h, x), (y, w), (0, 255, 0), 2)
        # cv2.imshow('AI RECEPTION ASSISTANT', frame)
        cv2.waitKey(1)
        encode = face_recognition.face_encodings(convertedImage)
        for encode , faceCoordinates in zip(encode, faceCoordinates) :
            matches = face_recognition.compare_faces(encodingList, encode)
            faceDistance = face_recognition.face_distance(encodingList, encode)
            matchIndex = numpy.argmin(faceDistance)
            if numpy.amin(faceDistance) < 0.6 :
                # cv2.putText(frame,f'{names[matchIndex].upper()},{faceDistance[matchIndex]}',(50,50), cv2.FONT_HERSHEY_COMPLEX, 1,(0,0,255),2)
                done = True
                temp = 1
                print(f'{names[matchIndex]}')
                attendance(names[matchIndex])
                break
            else :
                # cv2.putText(frame,f'unknown,{faceDistance[matchIndex]}',(50,50), cv2.FONT_HERSHEY_COMPLEX, 1,(0,0,255),2)
                done = True
                temp = 1
                print('unknown')
                break
                
        # cv2.imshow('AI RECEPTION ASSISTANT', frame)
        if temp == 1 :
            break
    webcam.release()
    cv2.destroyAllWindows()
# faceRec()
if __name__ == '__faceRec__':
    faceRec()
if __name__ == '__findEncodings__':
    findEncodings()
if __name__ == '__attendance__' :
    attendance()
