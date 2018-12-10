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
faces = CF.face.detect(img_url, face_id=False, landmarks=False, attributes='smile,emotion')

neutral = float(faces[0]["faceAttributes"]["emotion"]["neutral"]) * 100
smile = float(faces[0]["faceAttributes"]["smile"]) * 100
sadness = float(faces[0]["faceAttributes"]["emotion"]["sadness"]) * 100
surpirse = float(faces[0]["faceAttributes"]["emotion"]["surprise"]) * 100

print("あなたの表情は、\n通常：" + str(neutral) + "%\n笑顔：" + str(smile) + "%\n困惑：" + str(sadness) + "%\n驚き：" + str(surpirse) + "%\nです。")
print("画像処理が終了しました。")

img = cv2.imread("../img/" + now_picture)
cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

