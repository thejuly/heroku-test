# line-bot-Tutorial
 教你建立自己的 line-bot 使用 python flask 📝   
 line-bot-tutorial use python flask

* [Youtube Demo Tutorial V1 ](https://youtu.be/EToFs-ysXKw)   

* [Youtube Demo V2](https://youtu.be/1IxtWgWxtlE)   

## 執行畫面

請先加入好友

我的 QRCODE

![alt tag](http://i.imgur.com/Kkpzt4p.jpg)

或是手機直接點選 [https://line.me/R/ti/p/%40vbi2716y](https://line.me/R/ti/p/%40vbi2716y)

![alt tag](http://i.imgur.com/oAgR5nr.jpg)

認證記得請選 <b>同意</b>

![alt tag](http://i.imgur.com/9LOlGHh.jpg)

### v2 2017/2/25 

![alt tag](http://i.imgur.com/M30GJOU.jpg)

![alt tag](http://i.imgur.com/PCcnc5R.jpg)

![alt tag](http://i.imgur.com/3fajqDK.jpg)

![alt tag](http://i.imgur.com/SXwT0bl.jpg)

![alt tag](http://i.imgur.com/mc0R0xL.jpg)

![alt tag](http://i.imgur.com/GJI1BwG.jpg)

![alt tag](http://i.imgur.com/5T32UW3.jpg)



### V1  commit [ba855d6307c50cc478db3d7ac689bf0c96122a0f](https://github.com/twtrubiks/line-bot-tutorial/tree/ba855d6307c50cc478db3d7ac689bf0c96122a0f)

成功加入後，我的 <b>阿肥bot</b> 會傳訊息給你，並且告訴你我提供的服務

![alt tag](http://i.imgur.com/n9Gj09Y.jpg)

之後你就可以依照你想要看的東西輸入指令 (目前是有分大小寫，所以請輸入 <b>小寫</b> )

#### "eyny" : eyny 電影版 Mega 連結的網址。

![alt tag](http://i.imgur.com/rIGbmWA.jpg)

#### "news" : apple news 即時新聞。

![alt tag](http://i.imgur.com/JGnn2vG.jpg)

#### "beauty" : ptt 表特版 近期大於 10 推的文章 。

![alt tag](http://i.imgur.com/mvxoq4M.jpg)

#### "ptthot" : ptt 近期熱門的文章。

![alt tag](http://i.imgur.com/doMVR3y.jpg)

#### "movie" : 近期上映的電影 ( 開眼電影網 )。

![alt tag](http://i.imgur.com/EGbEXJ7.jpg)

#### "technews" : 科技新聞。

![alt tag](http://i.imgur.com/rHdq69F.jpg)

#### "panx" : 科技新聞 ( 泛科技 ) 。

![alt tag](http://i.imgur.com/NhaGdlW.jpg)

如果輸入不存在的指令，<b>阿肥bot</b> 會告知你我目前能做的指令有哪些

![alt tag](http://i.imgur.com/dabsGfK.jpg)


希望這個 <b>阿肥bot</b> 能幫助大家，程式碼基本上就是很簡單的爬蟲。

如果需要其他的功能，可以給小弟一點建議，我會盡量完成他。



## 教學

請先到 [https://business.line.me/zh-hant/](https://business.line.me/zh-hant/) 這裡登入自己

原本的 line 帳號，然後點選 Messaging API

![alt tag](http://i.imgur.com/KIzExmQ.jpg)

接下來你會看到 <b>開始使用Messaging API</b> 以及 <b>開始使用Developer Trial</b>

在這裡我們選 <b>開始使用Messaging API</b>

![alt tag](http://i.imgur.com/graLPrj.jpg)

這兩個差別在哪裡呢? 可以到同一個頁面的下方觀看，基本上就只是方案不同而已

![alt tag](http://i.imgur.com/bERbTGz.jpg)

接著就是一些設定，點選 選擇公司/經營者

![alt tag](http://i.imgur.com/d1pVdx9.jpg)

點選 新增公司/經營者

![alt tag](http://i.imgur.com/of23y7W.jpg)

填寫一些資料

![alt tag](http://i.imgur.com/7L9nulI.jpg)

line bot 的 大頭貼 以及 名稱 設定

![alt tag](http://i.imgur.com/7483ljT.jpg)

![alt tag](http://i.imgur.com/a4Mf3Rl.jpg)

設定完後，請選擇 申請

![alt tag](http://i.imgur.com/Q6q8zGA.jpg)

以上設定應該不會有什麼問題

請選擇 開始使用 API

![alt tag](http://i.imgur.com/DOEjH0F.jpg)

請選擇 確認

![alt tag](http://i.imgur.com/pKWBvsj.jpg)

這些請注意，  選擇 <b>允許</b> ，然後記得 <b>儲存</b>

![alt tag](http://i.imgur.com/Ofm9SeJ.jpg)

點選 <b>Line Developers</b>

![alt tag](http://i.imgur.com/cW9713h.jpg)

你會進入下面這個畫面，在這個畫面中，有兩個東西很重要，分別是

* Channel Secret

* Channel Access Token

<b>Channel Secret</b>

![alt tag](http://i.imgur.com/jpIEMh4.jpg)

<b>Channel Access Token</b>

如果你看到的是空的，請點選 <b>ISSUE</b> 就會顯示了

![alt tag](http://i.imgur.com/PcCEL4P.jpg)

請將你的 <b>Channel Secret</b> 以及 <b>Channel Access Token </b>

貼到下方的程式碼

```
line_bot_api = LineBotApi('YOUR_CHANNEL_ACCESS_TOKEN')
handler = WebhookHandler('YOUR_CHANNEL_SECRET')
``` 

更多資訊可參考 [line-bot-sdk-python](https://github.com/line/line-bot-sdk-python)

接下來因為 Line Bot 需要 SSL憑證 ( https )，所以我直接使用 [Heroku](https://dashboard.heroku.com/) 

如果不知道什麼是 [Heroku](https://dashboard.heroku.com/)  以及它的使用方法

請參考我之前寫的 [Deploying-Flask-To-Heroku](https://github.com/twtrubiks/Deploying-Flask-To-Heroku)

佈署

![alt tag](http://i.imgur.com/kseRgxr.jpg)

如上圖，我的網址是 [https://python-ine-bot.herokuapp.com/](https://python-ine-bot.herokuapp.com/)

接著我們要加入 Webhook URL ，請點選 EDIT ，並且加入你自己的網址，網址格式

```
https://{你的網址}/callback
``` 

舉例，我的網址就是

```
https://python-ine-bot.herokuapp.com/callback
``` 

![alt tag](http://i.imgur.com/5ckn24T.jpg)

![alt tag](http://i.imgur.com/TIjIM9W.jpg)

輸入完之後，可以按 VERIFY ，如果你的 CODE 正確無誤，就會顯示 Success

![alt tag](http://i.imgur.com/Mey5FKF.jpg)

不過我使用 [line-bot-sdk-python](https://github.com/line/line-bot-sdk-python)當我按下 VERIFY，卻出現錯誤，不過是可以正常運作，所以暫時先不管他。

![alt tag](http://i.imgur.com/wb0Qw5W.jpg)

關於上述這個問題，可以到 [issues 2](https://github.com/twtrubiks/line-bot-tutorial/issues/2) 觀看

基本上到這裡就是完成了，趕快去加入自己的 line bot 玩玩看吧~

只要我有新的想法，我會同步更新在這篇文章， line bot 還有很多好玩的地方

## 其他補充
只要有使用到網址，請記得一定都要用 <b> https </b>

舉例

```
image_message = ImageSendMessage(
            original_content_url="https://example.com.img1.jpg",
            preview_image_url="https://example.com.img1.jpg"
        )
``` 




## 執行環境
* Python 3.4.3

## Reference 
* [line messaging-api](https://devdocs.line.me/en/#messaging-api) 
* [line-bot-sdk-python](https://github.com/line/line-bot-sdk-python)


## License
MIT license
