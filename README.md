# Emoticon Key / 表情電鍵拍

## 題目發想緣起

在我們這一輩，常看到電影或紀錄片中，人們快速的用電鍵打著摩斯電碼來傳遞訊息，實在是很酷的一件事。

因此，想嘗試用 Raspberry Pi 實作一台電鍵；但在英文、數字，甚至是符號都具備的現代鍵盤旁，只能傳送無線電訊號的電鍵似乎有點無用武之地。

不過有一種語言，是現有的鍵盤不易打出來的，那就是「顔文字」。顏文字使用文字和符號組成表情或圖案，來傳達傳訊者的心情；
但其內容常包含了許多現有鍵盤無法打出來的字符。

若是，將每組顏文字都配以一摩斯電碼，在欲輸入顏文字時，只要在「表情電鍵拍」上敲打，即可輕鬆寫意又自在的輸入顏文字了！

本專題嘗試使用 Raspberry Pi 實作電鍵，並自行將一些常用的顏文字配以摩斯電碼，在網頁上呈現。

## 實作所需材料

| 材料名稱 | 取得來源 | 價格 |
| --- | --- | ---: |
| Raspberry Pi | 課堂提供 | NT$0 |
| 電鍵材料 | [MOLi](https://www.facebook.com/MOLi.rocks) 提供 | NT$0 |
| 螺絲少許 | NCNU IM Lab b11 工具箱 | NT$0 |
| 螺絲少許 | 國棟五金行 | NT$5 |
| 公母杜邦線 *2 | 組別 [BT-7](https://github.com/NCNU-OpenSource/BT-7) 提供 | NT$0 |

## 使用的現有軟體與來源

  - 電鍵 STL model
    - 由 ku4tp 於 [thingiverse](http://www.thingiverse.com) 以 [CC BY-SA 3.0](http://creativecommons.org/licenses/by-sa/3.0/) 方式授權[提供](http://www.thingiverse.com/thing:790879)
  - Raspberry Pi 上實作摩斯電碼機教學
    - 由 [Raspberry Pi Foundation](https://www.raspberrypi.org/) 以 [CC BY-SA](https://www.raspberrypi.org/creative-commons/) 方式授權[提供](https://www.raspberrypi.org/learning/morse-code/worksheet/)
  - Python Firebase
    - 由 Ozgur Vatansever 以 [The MIT License](https://github.com/ozgur/python-firebase/blob/master/LICENSE) 方式授權[提供](https://github.com/ozgur/python-firebase)

## 實作過程（碰到哪些問題、如何解決）

  - 電鍵印製出來後，找不到適合的螺絲組裝
    - 感謝 [@Trustmyself79](https://github.com/Trustmyself79)、[@zxp86021](https://github.com/zxp86021)、[@kenornotes](https://github.com/kenornotes) 協助組裝

## 運用哪些與課程內容中相關的技巧

  - Linux 基本觀念
  - 以 SSH 遠端連線
  - GPIO 基本觀念
  - LAMP Web Server 設定

## 組裝過程及製作教學

### 電鍵

  1. 以 3D 列印機印製模型材料。
  2. 按照[示意圖](http://www.thingiverse.com/thing:790879)，以 #4-40 號螺絲將之組裝。
  3. 準備兩條公母杜邦線，將公頭拆去後，把外漏的線纏住螺絲（按壓時會接觸的那兩顆）。
  4. 被接觸的下方螺絲，其線插於 GPIO pin \#6；接地。
  5. 接觸的上方螺絲，其線插於 GPIO pin \#7；正極。

### 資料庫

  1. 於 [Firebase](https://www.firebase.com) 註冊帳號。
  2. 將 Data URL 填於 `index.html` 以及 `morse-lookup.py` 中。

### Raspberry Pi

  1. 將 `morse-code.py` 以及 `morse-lookup.py` 放置於 Pi 中同一目錄下。
  2. 設定 `morse-code.py` 權限：

    ```sh
    chmod +x morse-code.py
    ```

## 操作教學

  1. 將電鍵與 Raspberry Pi 接好線。
  2. 啟動 Raspberry Pi，並執行 `morse-code.py`：

    ```sh
    sudo ./morse-code.py
    ```

  3. 開啟 `index.html` 於輸入框開始做文。
  4. 需要輸入顏文字時，使用電鍵鍵入需要的顏文字代碼。顏文字會自動加入到文末。

## 工作分配表

  - 電鍵製作：李悅
  - 程式撰寫：李悅
  - 簡報製作、報告：呂煉乳、李悅
  - 文件製作：呂煉乳、李悅
