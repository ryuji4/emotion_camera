#!/usr/bin/env python3
#coding:utf-8
import datetime
import picamera
import time, os
import numpy as np
import cv2

now_picture = str(datetime.datetime.now()) + ".jpg"
with picamera.PiCamera() as camera:
    camera.resolution = (1024, 768)
    camera.vflip = True
    print("写真を撮影します。")
    time.sleep(2)
    print(3)
    time.sleep(1)
    print(2)
    time.sleep(1)
    print(1)
    time.sleep(2)
    camera.capture("../img/" + now_picture)
    print("撮影が完了しました。")

print("画像処理に入ります。")

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
img = cv2.imread("../img/" + now_picture)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray, 1.3, 5)
for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
    roi_gray = gray[y:y+h, x:x+w]
    roi_color = img[y:y+h, x:x+w]
    eyes = eye_cascade.detectMultiScale(roi_gray)
    for (ex,ey,ew,eh) in eyes:
        cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)

cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
print("処理が完了しました。")
