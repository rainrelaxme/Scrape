#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
@Project: Scrape
@Version:
@Author: RainRelaxMe
@Date: 2023/10/5 21:41
"""
# 学习bs4
from bs4 import BeautifulSoup
import requests


if __name__ == '__main__':
    base_url = 'https://www.shicimingju.com/'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36'
    }
    url = base_url + 'book/sanguoyanyi.html'
    page_content = requests.get(url=url, headers=headers,).text.encode('iso-8859-1')    # 默认utf-8会出现乱码，采用此方法及下方.content的方法可以转换成功

    # 实例化beautifulsoup对象，将页面源码加载到对象中
    soup = BeautifulSoup(page_content, 'lxml')
    li_list = soup.select('.book-mulu>ul>li')
    fp = open('./files/sanguo.txt', 'w', encoding='utf-8')
    for li in li_list:
        title = li.a.string
        # 详情页链接
        detail_url = base_url + li.a['href']
        detail_page_text = requests.get(url=detail_url, headers=headers).content
        detail_soup = BeautifulSoup(detail_page_text, 'lxml')
        chapter_content = detail_soup.find('div', class_='chapter_content').text
        fp.write(title + ':' + chapter_content + '\n')
        print(title, 'scrape success!')
