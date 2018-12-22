#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" 
    @Time    : 2018/12/4 17:45
    @Author  : Junting
    @File    : standarlize.py
"""
import pandas as pd
import re
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import nltk
from PIL import Image
import numpy as np
from nltk.corpus import stopwords as pw
from sqlalchemy import create_engine
import pymysql



# nltk.download('stopwords')
cacheStopWords=pw.words("english")

def inspection(count,element):
    if count<5:
        print(element)

youtubeFrame=pd.read_csv("main chart.csv",encoding="utf-8")
itemCount=len(youtubeFrame)

tags={}
pattern=r'\[|\]|"'
for entryCount in range(itemCount):
    # "publish time" standarlize
    timeElement=youtubeFrame.at[entryCount,"publish_time"][2:10].replace("-",".")
    inspection(entryCount,timeElement)
    youtubeFrame.at[entryCount,"publish_time"]=timeElement

    # sparse "tag"  [none] is NA
    for blocks in youtubeFrame.at[entryCount, "tags"].split("|"):
        for items in blocks.split(" "):
            temp=re.sub(pattern,"", items).lower()
            if temp not in cacheStopWords:
                if temp not in tags:
                    tags[temp]=1
                else:
                    tags[temp]+=1

    for i in range(-3,0):
        if youtubeFrame.iloc[entryCount, i] == False:
            youtubeFrame.iloc[entryCount,i]=0
        else :youtubeFrame.iloc[entryCount,i]=1
for entryCount in range(itemCount):
    date = youtubeFrame.at[entryCount, "trending_date"][3:5]
    month=youtubeFrame.at[entryCount,"trending_date"][-2:]
    year=youtubeFrame.at[entryCount,"trending_date"][:2]
    result=".".join((year,month,date))
    youtubeFrame.at[entryCount,"trending_date"]=result
    inspection(entryCount,result)



# img = Image.open(r'images\1.png') #打开图片
# img_array = np.array(img) #将图片装换为数组
# font = r'C:\Windows\Fonts\FZSTK.TTF'
# wordCloud = WordCloud(
#     background_color='white',
#     width=1000,
#     height=1000,
#     mask=img_array,
#     font_path=font,
#     ).generate_from_frequencies(tags)
# wordCloud.to_file("WC.png")
# plt.imshow(wordCloud)
# plt.axis('off')
# plt.show()
# print("finish process 2")

# print(youtubeFrame[0:1])

youtubeFrame.to_csv("ultimate_data.csv")



