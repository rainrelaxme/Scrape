#爬取公司的git账号下的人员清单，及其工作记录，并生成文档提交给财务
# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author shawn

from urllib.request import urlopen

# 爬取的地址
address = input("please input the address you want to scrape : ")
shortAddress = input("please input the abbreviation : ")
html = urlopen(address)
content = str(html.read())
# print(address)


# 存储文件
file = open("./FileStorage/" + shortAddress + "ScrapeCon.txt", mode = "w")
# file.write(input("please input content : "))
file.write(content)


