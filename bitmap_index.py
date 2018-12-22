#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" 
    @Time    : 2018/12/18 19:20
    @Author  : Junting
    @File    : bitmap_index.py
"""
import pandas as pd
import pymysql


class BitmapIndex:
    def __init__(self, binString):
        self.digit = len(binString)
        self.binString = binString
        self.encodedBinString = int(binString, 2)

    def __and__(self, other):
        result = str(bin(self.encodedBinString & other.encodedBinString))[2:]
        totalDigit = max(self.digit, other.digit)
        # 补零
        return BitmapIndex((totalDigit - len(result)) * "0" + result)

    def __or__(self, other):
        return BitmapIndex(str(self.encodedBinString & other.encodedBinString)[2:])

    def searchPositive(self):
        result = []
        for charCount in range(len(self.binString)):
            if self.binString[charCount] == '1':
                result.append(charCount)
        return result


def toBinString(youtubeFrame, index):
    result, resultReversed = "", ""
    for items in list(youtubeFrame.iloc[:, index]):
        result += str(items)
        resultReversed += str(abs(1 - items))
    print(result)
    print(resultReversed)
    return BitmapIndex(result), BitmapIndex(resultReversed)


youtubeFrame = pd.read_csv("ultimate_data.csv", encoding="utf-8")
videoErrorOrRemoved, videoErrorOrRemovedReversed = toBinString(youtubeFrame, -1)
ratingsDisabled, ratingsDisabledReversed = toBinString(youtubeFrame, -2)
commentsDisabled, commentsDisabledReversed = toBinString(youtubeFrame, -3)

# search attempt
searchAttempt = ratingsDisabled & commentsDisabledReversed

# 打开数据库连接
db = pymysql.connect("localhost", "root", "chen0898", "youtube", charset='latin1')

# 使用cursor()方法获取操作游标
cursor = db.cursor()

# SQL 查询语句
for resultElement in searchAttempt.searchPositive():
    sql = "SELECT * FROM main_table \
           LIMIT %s,1" % (resultElement)
    try:
        # 执行SQL语句
        cursor.execute(sql)
        # 获取所有记录列表
        results = cursor.fetchall()
        # for row in results:
        #    #    fname = row[0]
        #    #    lname = row[1]
        #    #    age = row[2]
        #    #    sex = row[3]
        #    #    income = row[4]
        #    #    # 打印结果
        #    #    print ("fname=%s,lname=%s,age=%s,sex=%s,income=%s" % \
        #    #           (fname, lname, age, sex, income ))
        for i in results:
            print(i)
    except:
        print("Error: unable to fecth data")

# 关闭数据库连接
db.close()
