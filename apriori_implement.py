#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" 
    @Time    : 2018/12/20 21:21
    @Author  : Junting
    @File    : apriori_implement.py
"""

import pandas as pd
import re
import csv
import codecs
from PIL import Image
import numpy as np
import pymysql
import os

def inspection(element):
    print(element[:5])


youtubeFrame=pd.read_csv("ultimate_data.csv",encoding="utf-8")
itemCount=len(youtubeFrame)

# scan
def scan(youtubeFrame):
    itemCount=len(youtubeFrame)
    tagList=[]
    tagTypeList=[]
    apStartingPoint={}
    for entryCount in range(itemCount):
        # sparse "tag"  [none] is NA
        tempList=[]
        for blocks in youtubeFrame.at[entryCount, "tags"].split("|"):
                temp=re.sub('"',"", blocks).upper().strip()
                if temp:
                    if temp not in tagTypeList:
                        tagTypeList.append(temp)
                        apStartingPoint[temp]=1
                    else:apStartingPoint[temp]+=1
                    tempList.append(temp)
        tagList.append(sorted(tempList))
    tagTypeList=sorted(tagTypeList)
    apStartingPoint=[items for items in apStartingPoint.items()]
    # apStartingPoint=sorted(apStartingPoint,key=lambda d: d[1], reverse=True)
    dataWriteCsv("DATAS/apriori_starting_set.csv",apStartingPoint)
    dataWriteCsv("DATAS/tags.csv", tagList)

    return tagList,apStartingPoint

def dataWriteCsv(fileName, datas):
    '''

    :param fileName:  filename
    :param 格式数据：[(a,b)...]
    '''
    csvFile = codecs.open(fileName, 'w+', "utf-8")  # 追加
    writer = csv.writer(csvFile, delimiter=',', quotechar=',', quoting=csv.QUOTE_MINIMAL)
    for data in datas:
        temp=[element for element in data]
        writer.writerow(temp)
    print("保存文件成功")
# apriori
minSupportCount=600
if not os.path.exists("DATAS/apriori_starting_set.csv"):
    tagList,apStartingPoint=scan(youtubeFrame)
else:
    startingLoad=csv.reader(open("DATAS/apriori_starting_set.csv","r",encoding="utf-8"))
    # 初始化已缓存数据
    tagList=csv.reader(open("DATAS/tags.csv","r",encoding="utf-8"))
# 既是开始集合，也是排序参考
startingSet=sorted([[[items[0]],int(items[1])] for items in startingLoad if int(items[1])>minSupportCount],key=lambda d:d[0])
tagList=list(tagList)
print(len(startingSet))
# inspection(tagList)
# inspection(startingSet)


def countSupport(tagList, propSet):
    count=0
    for entries in tagList:
        if set(propSet) < set(entries):
            count+=1
    return count
def isCandidate(source,pair):
    if source[:-1]==pair[:-1] and pair[-1]>source[-1]:
        # print(pair[:-1])
        # print(source[-1])
        return pair+source[-1:]
    else:
        return None

def perfectSet(result,candi):
    if result:
        for count,i in enumerate(result):
            if set(i[0])<set(candi[0]):
                result.pop(count)

    result+=[candi]
    return result

def apriori(startingSet,tagList):
    result=[]
    currentSet=startingSet

    while currentSet:
        print(currentSet)
        cacheSet = []
        for sourceItemCount,sourceItem in enumerate(currentSet):
            for pairItemCount,pairItem in enumerate(currentSet):
                if sourceItemCount!=pairItemCount:
                    candi=isCandidate(sourceItem[0],pairItem[0])
                    # print(candi)
                    if candi is not None:
                        support=countSupport(tagList,candi)
                        if support>minSupportCount:
                            result=perfectSet(result,[candi,support])
                            cacheSet.append([candi,support])
                            print(len(cacheSet))
                            print("result:",result)
        currentSet=cacheSet

    print(result)
apriori(startingSet,tagList)














