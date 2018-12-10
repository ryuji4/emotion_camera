#!/usr/bin/env python3
#coding:utf-8
import datetime
import picamera
import time
import cognitive_face as CF
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
    time.sleep(5)

print("画像処理に入ります。")

KEY = ''
BASE_URL = 'https://westcentralus.api.cognitive.microsoft.com/face/v1.0'

CF.Key.set(KEY)
CF.BaseUrl.set(BASE_URL)

img_url = "../img/" + now_picture
faces = CF.face.detect(img_url)
print(faces)

print("処理が完了しました。")
