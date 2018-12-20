#!/usr/bin/python3
#coding:utf-8
import datetime
import picamera
import time
import cognitive_face as CF
import cv2
import io,sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')

now_picture = str(datetime.datetime.now()) + ".jpg"

with picamera.PiCamera() as camera:
    camera.resolution = (1024, 768)
    camera.vflip = True
    print("Content-type: text/html\r\n")
    print("<!DOCTYPE html>")
    print("<html lang='ja'>")
    print("<head>")
    print("    <meta charset='utf-8'>")
    print("    <title>表情訓練</title>")
    print("</head>")
    print("<body>")
    print("<h1>表情訓練システム</h1><br>")
    print("写真を撮影します。<br>")
    time.sleep(2)
    print("3<br>")
    time.sleep(1)
    print("2<br>")
    time.sleep(1)
    print("1<br>")
    time.sleep(2)
    camera.capture("/home/pi/img/" + now_picture)
    print("<img src='/home/pi/img/" + now_picture + "' ><br>")
    print("撮影が完了しました。<br>")
    time.sleep(5)

print("画像処理に入ります。<br>")

KEY = ''
BASE_URL = 'https://westcentralus.api.cognitive.microsoft.com/face/v1.0'

CF.Key.set(KEY)
CF.BaseUrl.set(BASE_URL)

img_url = "/home/pi/img/" + now_picture
faces = CF.face.detect(img_url, face_id=False, landmarks=False, attributes='smile,emotion')

count = False
face_data = {"通常":0,"笑顔":0,"困惑":0,"驚き":0}

if faces != []:
    face_data["通常"] = round(faces[0]["faceAttributes"]["emotion"]["neutral"],3) * 100
    face_data["笑顔"] = round(faces[0]["faceAttributes"]["smile"],3) * 100
    face_data["困惑"] = round(faces[0]["faceAttributes"]["emotion"]["sadness"],3) * 100
    face_data["驚き"] = round(faces[0]["faceAttributes"]["emotion"]["surprise"],3) * 100

    print("あなたの表情は、<br>")
    for f in face_data:
        if face_data[f] != 0:
            print("<h2>" + f + "：" + str(face_data[f]) + "%です。</h2><br>")
            count = True
        else:
            pass
else:
    print("<h2>表情を検出出来ませんでした。</h2><br>")

print("画像処理が終了しました。<br>")

print("</body>")
print("</html>")
