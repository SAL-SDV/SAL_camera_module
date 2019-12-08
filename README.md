# SAL_camera_module
***
raspberry-pi:zeroにおいて
1. 人感センサーから信号を受け取る
2. 1をトリガーとして動画の撮影を行う（センサーが反応している間）
3. 撮影した動画を保存
4. 動画をhome_moduleに送信する
という4つの処理を行うプログラムです。

## 旧プログラム
```
・ma_4.0.py 動作しません。
・ma_5.py   常時撮影し動体検知を行う。動画検知後、動画を保存しhome_moduleに送信する。途中カスケード分類機にかけて顔認識も行っているが、未完成の模様。
```
## 新プログラム
```
・sensor_event.py 1.2.3を行う(メインプログラム)
・photo_send.py 4を行う(sensor_event.pyからimportされる)
```

備考
・cp,paramikoはパッケージをインストールする必要あり（何らかのエラーが発生したら本体をアップデート)
・市役所サーバの準備ができたら、sensor_event.pyの通信が秘密鍵で行えるようにする事を推奨  
・photo_send.pyでは秘密鍵を用いたscpを採用しているが、事前の設定が必要([参考サイト](https://qiita.com/kuro___inu/items/93da8aa9b56847c3a2bf))
