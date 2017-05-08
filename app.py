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
# end import module

app = Flask(__name__)
line_bot_api = LineBotApi('wbeBaLPb7xIuGymdaHU9yHy300QZ383XYgewhXLSoRe3TnlWo1xQuypNFpis1ExGrSTV1WpmtmQEiaR9tRPQHFUspwI9rVk2Ajfrg1WUwFpV9ewvq/vDx9LItfeNW+9y6Ih/OcwNpJPB/UfE9afIFwdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('49a9d31e3b8135ee7f85e6bc78848baa')
#end Token




picture = ["https://i.imgur.com/qKkE2bj.jpg",
           "https://i.imgur.com/QjMLPmx.jpg",
           "https://i.imgur.com/HefBo5o.jpg",
           "https://i.imgur.com/AjxWcuY.jpg",
           "https://i.imgur.com/3vDRl4r.jpg",
           "https://i.imgur.com/3qSGcKT.jpg",
           "https://i.imgur.com/ZbdV9Nz.jpg",
           "https://i.imgur.com/oAkIJmH.jpg",
           "https://i.imgur.com/MtcwDtD.jpg",
           "https://i.imgur.com/qre60t1.jpg",
           "https://i.imgur.com/Yrvc7LV.jpg",
           "https://i.imgur.com/4wJXl4D.jpg",
           "https://i.imgur.com/71suURR.jpg",
           "https://i.imgur.com/sNBVjhg.jpg",
           "https://i.imgur.com/h5HJmGx.jpg",
           "https://i.imgur.com/O92zfAa.jpg",
           "https://i.imgur.com/eaQyCc9.jpg",
           "https://i.imgur.com/CEuYLJ6.jpg",
           "https://i.imgur.com/yD8RcYu.jpg",
           "https://i.imgur.com/cOLTxKC.jpg",
           "https://i.imgur.com/pYQHJXU.jpg",
           "https://i.imgur.com/JC68vsX.jpg",
           "https://i.imgur.com/4hEWo2f.jpg",
           "https://i.imgur.com/FW6wzFO.jpg",
           "https://i.imgur.com/pgMFTp1.jpg",
           "https://i.imgur.com/GWoZrQB.jpg",
           "https://i.imgur.com/ytByPTQ.jpg",
           "https://i.imgur.com/Qta7jlq.jpg",
           "https://i.imgur.com/PByM0FF.jpg",
           "https://i.imgur.com/xCLD2QP.jpg",
           "https://i.imgur.com/vq7ONzd.jpg",
           "https://i.imgur.com/OKtXWJS.jpg",
           "https://i.imgur.com/RonVK6S.jpg",
           "https://i.imgur.com/cH9oLjI.jpg",
           "https://i.imgur.com/sn4p43t.jpg",
           "https://i.imgur.com/LaKmM7c.jpg",
           "https://i.imgur.com/7YzFhNt.jpg",
           "https://i.imgur.com/O6j2qDB.jpg",
           "https://i.imgur.com/N4pkG9S.jpg",
           "https://i.imgur.com/1SlHQU6.jpg",
           "https://i.imgur.com/mplQ8IO.jpg",
           "https://i.imgur.com/tO1R8Xt.jpg",
           "https://i.imgur.com/nCgWLuY.jpg",
           "https://i.imgur.com/ZQfoFsa.jpg",
           "https://i.imgur.com/ApmQia8.jpg",
           "https://i.imgur.com/CiUyuZb.jpg",
           "https://i.imgur.com/hfhA6d4.jpg",
           "https://i.imgur.com/KOljinG.jpg",
           "https://i.imgur.com/XmRwW0U.jpg",
           "https://i.imgur.com/Ee8CFje.jpg",
           "https://i.imgur.com/yNkxNkA.jpg",
           "https://i.imgur.com/hnkzX6p.jpg",
           "https://i.imgur.com/rrdr3zZ.jpg",
           "https://i.imgur.com/hzbdQU9.jpg",
           "https://i.imgur.com/xdNOHGc.jpg",
           "https://i.imgur.com/b2B1LPE.jpg",
           "https://i.imgur.com/BUfqlcN.jpg",
           "https://i.imgur.com/8yl3W2D.jpg",
           "https://i.imgur.com/DbxBheB.jpg",
           "https://i.imgur.com/DDNc9ot.jpg",
           "https://i.imgur.com/hh2e3LT.jpg",
           "https://i.imgur.com/2cdURNa.jpg"
           ]


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


def patternMega(text):
    patterns = ['mega', 'mg', 'mu', 'ＭＥＧＡ', 'ＭＥ', 'ＭＵ', 'ｍｅ', 'ｍｕ', 'ｍｅｇａ']
    for pattern in patterns:
        if re.search(pattern, text, re.IGNORECASE):
            return True


def eynyMovie():
    targetURL = 'http://www.eyny.com/forum-205-1.html'
    print('Start parsing eynyMovie....')
    rs = requests.session()
    res = rs.get(targetURL, verify=False)
    soup = BeautifulSoup(res.text, 'html.parser')
    content = ''
    for titleURL in soup.select('.bm_c tbody .xst'):
        if (patternMega(titleURL.text)):
            title = titleURL.text
            if '10990869-1-3' in titleURL['href']:
                continue
            link = 'http://www.eyny.com/' + titleURL['href']
            data = title + '\n' + link + '\n\n'
            content += data
    return content


def appleNews():
    targetURL = 'http://www.appledaily.com.tw/realtimenews/section/new/'
    head = 'http://www.appledaily.com.tw'
    print('Start parsing appleNews....')
    rs = requests.session()
    res = rs.get(targetURL, verify=False)
    soup = BeautifulSoup(res.text, 'html.parser')
    content = ""
    for index, data in enumerate(soup.select('.rtddt a'), 0):
        if index == 15:
            return content
        if head in data['href']:
            link = data['href']
        else:
            link = head + data['href']
        content += link + '\n\n'
    return content


article_list = []
article_gossiping = []


def getPageNumber(content):
    startIndex = content.find('index')
    endIndex = content.find('.html')
    pageNumber = content[startIndex + 5: endIndex]
    return pageNumber


def crawPage(url, push_rate, soup):
    for r_ent in soup.find_all(class_="r-ent"):
        try:
            # 先得到每篇文章的篇url
            link = r_ent.find('a')['href']
            if 'M.1430099938.A.3B7' in link:
                continue
            comment_rate = ""
            if (link):
                # 確定得到url再去抓 標題 以及 推文數
                title = r_ent.find(class_="title").text.strip()
                rate = r_ent.find(class_="nrec").text
                URL = 'https://www.ptt.cc' + link
                if (rate):
                    comment_rate = rate
                    if rate.find(u'爆') > -1:
                        comment_rate = 100
                    if rate.find('X') > -1:
                        comment_rate = -1 * int(rate[1])
                else:
                    comment_rate = 0
                # 比對推文數
                if int(comment_rate) >= push_rate:
                    article_list.append((int(comment_rate), URL, title))
        except:
            # print u'crawPage function error:',r_ent.find(class_="title").text.strip()
            # print('本文已被刪除')
            print('delete')


def crawPage_Gossiping(url, soup):
    for r_ent in soup.find_all(class_="r-ent"):
        try:
            # 先得到每篇文章的篇url
            link = r_ent.find('a')['href']
            # if 'M.1430099938.A.3B7' in link:
            #     continue

            if (link):
                # 確定得到url再去抓 標題 以及 推文數
                title = r_ent.find(class_="title").text.strip()
                URL = 'https://www.ptt.cc' + link
                article_gossiping.append((URL, title))
        except:
            # print u'crawPage function error:',r_ent.find(class_="title").text.strip()
            # print('本文已被刪除')
            print('delete')





@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    # cmd = defaultdict(default_factory, command)
    print("event.reply_token:", event.reply_token)
    print("event.message.text:", event.message.text)
    if event.message.text == "eyny":
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text='thongpoon'))
        return 0

    if event.message.text == "aa":
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text='your text is aa'))
        return 0





if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
