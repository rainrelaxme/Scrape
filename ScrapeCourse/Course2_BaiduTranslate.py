#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
@Project: Scrape
@Version:
@Author: RainRelaxMe
@Date: 2023/10/4 22:54
"""
# 百度翻译爬虫

import requests
import json

if __name__ == '__main__':
    post_url = 'https://fanyi.baidu.com/sug'
    # UA伪装
    request_header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36'
    }
    # 参数
    kw = input('please input keyword:')
    form_data = {
        'kw': kw
    }
    response = requests.post(url=post_url, data=form_data, headers=request_header)
    dic_obj = response.json()
    print(dic_obj)

    # 持久化存储
    fp = open('./files/' + kw + '.json', 'w', encoding='utf-8')
    json.dump(dic_obj, fp=fp, ensure_ascii=False)
