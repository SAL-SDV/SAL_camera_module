# coding:utf-8
import time
import datetime
import picamera
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(26, GPIO.IN) #人感センサのピン番号
import photo_send as send

save_folder = "movie/"; #動画を保存するフォルダを指定
print("a")

while True:
    inputValue = GPIO.input(26)
    print(inputValue)
    #inputValue= True
    if (inputValue == True):    #反応があったら
        with picamera.PiCamera() as camera: #録画開始
            camera.resolution = (800, 600)  #解像度指定
            #inputValue = False
            d = datetime.datetime.now() #現在時刻取得
            name = save_folder+d.strftime('%Y:%m:%d:%H:%M:%S') + '.h264' #ファイル名指定
            camera.start_recording(name)
            time.sleep(5)
            while(inputValue):
                inputValue = GPIO.input(26)
                time.sleep(1)
                print("rec")

            if(inputValue == False):  #反応が消えたら
                camera.stop_recording()
                send.send(name) #動画をホームモジュールに送信
                print("scp_OK!")
    time.sleep(1)

