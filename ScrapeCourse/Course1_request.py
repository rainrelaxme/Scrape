#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
@Project: Scrape
@Version:
@Author: RainRelaxMe
@CrateTime: 
@EditTime: 2023/10/2 0:10
"""
from urllib import request

# 爬虫练习

import requests

if __name__ == '__main__':
    # UA伪装
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36'
    }
    # https://www.baidu.com/s?wd=python&rsv_spt=1&rsv_iqid=0xa22bc37300008164&issp=1&f=8&rsv_bp=1&rsv_idx=2&ie=utf-8&rqlang=cn&tn=baiduhome_pg&rsv_dl=tb&rsv_enter=0&oq=python&rsv_btype=t&rsv_t=b50dWdhvxoeP9syF9bRlgvLTmMw0AnEIc8ys7D%2B5aC6swqpJbrwOtHa2N2%2FVRxlkCt6D&rsv_pq=b6b6601f00004eff
    url = 'https://www.baidu.com'
    key_word = input('enter a word:')
    param = {
        'wd': key_word
    }
    response = requests.get(url=url, params=param, headers=headers)
    page_content = response.text
    fileName = key_word + '.html'
    with open(fileName, 'w', encoding='utf-8') as fp:
        fp.write(page_content)
    print(fileName, '保存成功！')
