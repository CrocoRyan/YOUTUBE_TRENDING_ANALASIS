#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" 
    @Time    : 2018/10/25 16:04
    @Author  : Junting
    @File    : __init__.py.py
"""

import numpy as np
import pandas as pd
import math

# import urllib.request as request
# import requests
#
# proxies = {
#     'https': 'https://47.88.55.41:47780',
#     'http': 'http://47.88.55.41:47780'
# }
# headers = {
#     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'
# }
#
# print('--------------使用urllib--------------')
# google_url = 'https://www.google.com'
# opener = request.build_opener(request.ProxyHandler(proxies))
# request.install_opener(opener)
#
# req = request.Request(google_url, headers=headers)
# response = request.urlopen(req)
#
# print(response.read().decode())
#
# print('--------------使用requests--------------')
# response = requests.get(google_url, proxies=proxies)
# print(response.text)
#
#
# # response=request.urlopen("http://www.baidu.com").read()
# # import chardet
# # print ("该网页使用的编码是：%s" %(chardet.detect(response)))
# #
# #
# # 从列表写入csv文件
# csvFile2 = open('C:/Users/Administrator/Desktop/20170904副本.csv','wb')
# writer = csv.writer(csvFile2)
# # writer.writerow(result1)
# m = len(result1)
# for i in result1:
#     writer.writerow([i])
# csvFile2.close()

test=pd.read_csv("description.csv",encoding="ISO-8859-1")
print(test.iloc[31026,1])

