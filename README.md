# SAL_camera_module
***
raspberry-pi:zeroにおいて
1. 人感センサーから信号を受け取る
2. 1をトリガーとして動画の撮影を行う（センサーが反応している間）
3. 撮影した動画を保存
4. 動画をhome_moduleに送信する
という4つの処理を行うプログラムです。

## 旧コード
- ma_4.0.py 動作しません。
- ma_5.py   常時撮影し動体検知を行う。動画検知後、動画を保存しhome_moduleに送信する。途中カスケード分類機にかけて顔認識も行っているが、未完成の模様。

## 新コード
- sensor.py 1.2.3を行う(メインプログラム)
- photo_send.py 4を行う(sensor_event.pyからimportされる)
- check_sensor.py 人感センサの値を表示する（デバック用）

# 使い方
sudo python3 senser.py

もしカメラモジュール単体で動作確認をしたい(動画を送りたくない)のであればsenser_event.pyの`send.send(name)`をコメントアウト


### 備考
- scp,paramikoはパッケージをインストールする必要あり（何らかのエラーが発生したら本体をアップデート)
- photo_send.pyは現在パスフレーズを用いたSCPを使用（秘密鍵推奨）([参考サイト](https://qiita.com/kuro___inu/items/93da8aa9b56847c3a2bf))
