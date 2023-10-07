#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
@Project: Scrape
@Version:
@Author: RainRelaxMe
@Date: 2023/10/5 0:17
"""
# 爬取Wallhaven壁纸图片

import requests
import os
import re
from scripts import check_file

if __name__ == '__main__':
    # 创建文件夹存放图片
    if not os.path.exists('./files/Wallpapers'):
        os.mkdir('./files/Wallpapers')

    # UA伪装
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36'
    }

    # 链接及页面翻页
    url = 'https://wallhaven.cc/toplist'
    page = int(input('please input pagesize you want to do scrape:'))
    for p in range(1, page+1):
        params = {
            'page': p
        }
        page_content = requests.get(url=url, params=params, headers=headers).text
        # print(page_content)
        # 正则
        # <img alt="loading" class="lazyload" data-src="https://th.wallhaven.cc/small/d6/d6dvdl.jpg" src="" ><a class="preview" href="https://wallhaven.cc/w/d6dvdl"  target="_blank"  ></a>
        ex = '<img alt="loading" class="lazyload.*?<a class="preview" href="(.*?)"  target="_blank".*?</a>'
        img_link = re.findall(ex, page_content, re.S)
        print('共{}张图片'.format(len(img_link)))

        # 再次请求详情页，拿到原图
        for src in img_link:
            src_lite = src.split('/')[-1]
            if check_file.is_exist(src_lite, './files/Wallpapers/', mode=1):
                continue
            else:
                img_detail = requests.get(url=src, headers=headers).text
                # <img id="wallpaper" src="https://w.wallhaven.cc/full/6d/wallhaven-6dy51x.jpg" alt="General 4744x6308 ILLDIAN black pantyhose legs simple background squatting looking at viewer cross portrait display long hair necklace M legs animal ears blue eyes dark hair digital art" data-wallpaper-id="6dy51x" data-wallpaper-width="4744" data-wallpaper-height="6308" crossorigin="anonymous" class="fill-horizontal">
                ex_big = '<img id="wallpaper" src="(.*?)" alt'
                img_src = re.findall(ex_big, img_detail, re.S)
                img = requests.get(url=img_src[0], headers=headers).content
                img_name = img_src[0].split('/')[-1]
                img_path = './files/Wallpapers/' + img_name
                with open(img_path, 'wb') as fp:
                    fp.write(img)
                    print(img_name, '下载完成!')
