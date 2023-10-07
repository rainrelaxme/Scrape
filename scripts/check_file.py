#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
@Project: Scrape
@Version:
@Author: RainRelaxMe
@Date: 2023/10/5 20:08
"""
# 文件的基本操作，服务于爬虫
import os
import re


# 文件是否已经存在
def is_exist(filename, path, mode=0):
    """
    判断文件是否已经存在，mode=0精确匹配，mode=1模糊匹配
    如果已经存在，则返回1；不存在，则返回0.
    """
    file_list = os.listdir(path)
    results = []
    if mode == 0:
        if filename in file_list:
            results.append(filename)
        else:
            pass
    elif mode == 1:
        for file in file_list:
            result = re.search(filename, file)
            if result:
                results.append(result.string)
            else:
                continue
    else:
        print('Error mode!')
    if results:
        # print(results)
        return 1, '\n', results
    else:
        return 0


# if __name__ == '__main__':
#     path = 'E:/Project/Rainrelaxme/Scrape/ScrapeCourse/files/Wallpapers'
#     file = input('please input filename:')
#     is_exist(file, path, mode=1)
