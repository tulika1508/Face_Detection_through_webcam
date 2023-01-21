
"""
Created on Thu Jan 19 23:52:35 2023

@author: TULIKA
"""

import cv2


face = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

c = cv2.VideoCapture(0)

while True:
    # Reading the frame
    _, img = c.read()
    # Converting to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # Detecting the faces
    faces = face.detectMultiScale(gray, 1.1, 4)
    # Draw the rectangle around each face
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (260, 0, 0), 2)
   
    cv2.imshow('img', img)
    
    k = cv2.waitKey(30) & 0xff
    if k==27:
        break

c.release()