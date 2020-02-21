# coding:utf-8
import time
import datetime
import picamera
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(26, GPIO.IN) #人感センサのピン番号
#import photo_send as send

save_folder = ""; #動画を保存するフォルダを指定

while True:
    inputValue = GPIO.input(26)
    print(inputValue)
    """
    #inputValue= True
    if (inputValue == True):    #反応があったら
        print(33)
        with picamera.PiCamera() as camera: #録画開始
            camera.resolution = (160, 120)  #解像度指定
            inputValue = False
            d = datetime.datetime.now() #現在時刻取得
            name = save_folder+d.strftime('%Y:%m:%d:%H:%M:%S') + '.h264' #ファイル名指定
            camera.start_recording(name)
            camera.start_preview()  # 撮影開始
	    time.sleep(5)
            if(inputValue == False):  #反応が消えたら
                #camera.capture(name) #保存
                camera.stop_recording()
                #send.send(name) #動画をホームモジュールに送信
                print("rec")
    """
    time.sleep(1)
