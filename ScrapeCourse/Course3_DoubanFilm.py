#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
@Project: Scrape
@Version:
@Author: RainRelaxMe
@Date: 2023/10/4 23:14
"""
# 爬取豆瓣电影排行榜-喜剧

import requests
import json

if __name__ == '__main__':
    num = input('希望获取前____名电影排行？')
    # 链接
    url = 'https://movie.douban.com/j/chart/top_list'
    # UA伪装
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36'
    }
    params = {
        'type': '24',
        'interval_id': '100:90',
        'limit': num,
    }
    # 开始爬取
    response = requests.get(url=url, params=params, headers=headers)
    dic_obj = response.json()
    print('Scrape Over！\n', dic_obj)
    for i in range(0, int(num)):
        print(dic_obj[i]['rank'], '\t', dic_obj[i]['title'])

    # with open('./files/rankList.json', 'w', encoding='utf-8') as fp:
    #     json.dump(dic_obj, fp=fp, ensure_ascii=False)
    # print('保存成功！')