# mujin

## whats this?
- Raspberry Pi Zero 2 W をキーボードデバイスとして認識させ、人間が与えたテーマの文章をAI生成し、その文章を人間が入力しているかのように見せかける仕組み

- 在宅ワークでキーボードのタイプ数やその内容を監視されている人向けの提案

- キーロガーにある程度意味のある文字列を自動入力する

- 入力文字数でサボっているか判別するのは無理がある

- 職業や立場にもよるが、手を止めた思考労働も必要

## 注意
- これはPoCなので完璧な動作は保証しません。

## 使い方

1. デバイスの準備
    - Raspberry Pi Zero 2 W で Raspberry Pi OS Lite が動く状態であること(OSインストールはweb上に色々あるので割愛)

    - Wi-Fi(2.4GHz帯)経由でRaspberry PiにSSHログインできること

    - Raspberry Piのアップデート(sudo apt updateなど)が済んでいること

    - Raspberry Pi基盤の2番目(HDMI端子に近い方)のUSB Type-BとPCのUSB Type-Aをつなぐ

    - Raspberry Piの電源を入れる

1.  HID設定
    - 下記URL内容を実施する

        https://randomnerdtutorials.com/raspberry-pi-zero-usb-keyboard-hid/

        USBのType変換やUSBハブを経由するとうまく動かない

        (自分が試した中ではRaspberry PiのUSB Type-BとPCのUSB Type-Aの直接接続でのみうまく動いた)

    - この後作るプログラムが一般ユーザ権限で動くよう下記修正を加える

        ```
        sudo nano /etc/rc.local

        # nanoエディタ内「exit 0」の前に下記コマンドを加える

        chmod 777 /dev/hidg0
        ```

    - 修正したら再起動する

1. pipアップデート
    ```
    pip3 install --upgrade pip
    ``` 

1. Pythonライブラリのインストール

    ```
    pip3 install openai
    pip3 install Py-Keyboard
    pip3 install python3-evdev python3-uinput
    ```

1. OpenAI API Keyの入手

    たくさん記事があるので割愛

1. プログラム

    - mujin.pyをRaspberry Piにコピペ保存

    - APIキーは自分のものを入力すること

1. 実行方法

    - 文字を入力させたいPCでテキストエディタなどを開き、日本語入力可能な状態にする

    - 下記コマンドを実行

     ```
     python3 mujin.py 書かせたいテーマ 日本語での文字数

     例 python3 mujin.py デジタルセキュリティ 100
     ```

1. 期待される結果
    
    - Raspberry Piのプロンプト上には日本語の文章とASCII変換した文字列が表示される

    - USB接続先のPCには誤字脱字はありつつもそれっぽい文章が入力される
