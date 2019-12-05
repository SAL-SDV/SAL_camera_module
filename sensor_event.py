import time
import datetime
import picamera
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(25, GPIO.IN) #人感センサのピン番号
import photo_send as send

save_folder = ""; #動画を保存するフォルダを指定

while True:
    inputValue = GPIO.input(25)　    #人感センサの反応を監視
    if (inputValue == True):    #反応があったら
        with picamera.PiCamera() as camera: #録画開始
            camera.resolution = (160, 120)  #解像度指定
            camera.start_preview()  # 撮影開始
            if(inputValue == False):  #反応が消えたら
                d = datetime.datetime.now() #現在時刻取得
                name = save_folder+d.strftime('%Y:%m:%d:%H:%M:%S') + '.mp4' #ファイル名指定
                camera.capture(name)　#保存
                send.send(name) #動画をホームモジュールに送信
    time.sleep(1)
