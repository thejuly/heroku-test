# -*- coding: utf-8 -*-
import os
from flask import Flask, request
import json
import requests

import re
import random
from bs4 import BeautifulSoup
from collections import defaultdict
from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *

from linebot import LineBotApi
from linebot.exceptions import LineBotApiError
# end import module

app = Flask(__name__)
line_bot_api = LineBotApi('wbeBaLPb7xIuGymdaHU9yHy300QZ383XYgewhXLSoRe3TnlWo1xQuypNFpis1ExGrSTV1WpmtmQEiaR9tRPQHFUspwI9rVk2Ajfrg1WUwFpV9ewvq/vDx9LItfeNW+9y6Ih/OcwNpJPB/UfE9afIFwdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('49a9d31e3b8135ee7f85e6bc78848baa')
#end Token




@app.route("/callback", methods=['POST'])
def callback():
    
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    # print("body:",body)   
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'








@handler.default()
def default(event):
    print(event)


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    print("event.reply_token:", event.reply_token)
    print("event.message.text:", event.message.text)

    
    if event.message.text == "aa":
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text='your text is aa'))
        return 0

    if event.message.text == "bb":
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text=event.message.text))
        return 0

    if event.message.text == "cc":
        profile = line_bot_api.get_profile('C91f0e330efd3aebe03c34bfd2bd40cce')
        #profile = line_bot_api.get_profile('U5e90b6b6d543d8d96be449d8fcd3ddbe')
        a = (profile.display_name)
        #b = (profile.group_id) #for group_id
        #c = (profile.picture_url)
        #d = (profile.status_message)
        #line_bot_api.push_message(event.reply, TextSendMessage(text='Hello MyJob'))
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text=a))
        return 0
    
    if event.message.text == "dd":
        profile = line_bot_api.get_profile('U5e90b6b6d543d8d96be449d8fcd3ddbe') #profile of sender => Thongpoon Auto 0684 (User)
        a = (profile.display_name)
        b = (profile.user_id) #for user_id
        c = (profile.picture_url)
        d = (profile.status_message)
        line_bot_api.push_message(b, TextSendMessage(text='Hello Thongpoon!'))
        return 0


    if event.message.text == "json":
        
        #Thongpoon
        json_line = request.get_json()
        json_line = json.dumps(json_line)
        decoded = json.loads(json_line)

        #user = user who send message to me
        #messageGet = message that user send to me
        #typeGet = type of data that user send to me
        user = decoded["events"][0]['replyToken']
        messageGet = decoded["events"][0]['message']['text']
        typeGet = decoded["events"][0]['message']['type']
        #Thongpoon
    
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text=json_line))
        return 0








if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
