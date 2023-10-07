# 爬取pocket内的网址
# !/usr/bin/env python3
# -*- coding:utf-8 -*-
# author rainrelaxme
import re

import requests
import requests

if __name__ == '__main__':
    url = 'https://wallhaven.cc/w/p9gdrp'
    # url = 'https://wallhaven.cc/w/m3ywwy'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36'
    }
    page_content = requests.get(url=url, headers=headers).text
    ex = '<img id="wallpaper" src="(.*?)" alt'
    img_link = re.findall(ex, page_content, re.S)
    img = requests.get(url=img_link[0], headers=headers).content
    with open('./test.html', 'w', encoding='utf-8') as fp:
        fp.write(page_content)
        print('Over!')


