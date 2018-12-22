#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" 
    @Time    : 2018/12/7 10:25
    @Author  : Junting
    @File    : test.py
"""
import re
import pandas as pd
import re
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import nltk
from PIL import Image
import numpy as np
from nltk.corpus import stopwords as pw
# from sqlalchemy import create_engine



nltk.download('stopwords')
cacheStopWords=pw.words("english")
# print(cacheStopWords)

def inspection(count,element):
    if count<5:
        print(element)

youtubeFrame=pd.read_csv("main chart.csv",encoding="ISO-8859-1")
itemCount=len(youtubeFrame)
# temp= 0 if 1<2 else 1
# youtubeFrame.iloc[1,-1]=temp
# youtubeFrame.iloc[1,-1]=0 if youtubeFrame.iloc[1,-1]==False else 1
# print(youtubeFrame.head())



tags={}
pattern=r'\[|\]|"'
for entryCount in range(itemCount):
    # "publish time" standarlize
    timeElement=youtubeFrame.at[entryCount,"publish_time"][:-5].replace("-",".")
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

    # bitmap for comments_disabled,ratings_disabled,video_error_or_removed

    for i in range(-3,0):
        if youtubeFrame.iloc[entryCount, i] == False:
            youtubeFrame.iloc[entryCount,i]=0
        else :youtubeFrame.iloc[entryCount,i]=1


img = Image.open(r'images\1.png') #打开图片
img_array = np.array(img) #将图片装换为数组
font = r'C:\Windows\Fonts\FZSTK.TTF'
wordCloud = WordCloud(
    background_color='white',
    width=1000,
    height=673,
    mask=img_array,
    font_path=font,
    scale=1000
    ).generate_from_frequencies(tags)
plt.imshow(wordCloud)
plt.axis('off')
plt.show()
print("finish process 2")

print(youtubeFrame[0:1])

youtubeFrame.to_csv("ultimate_data.csv")