#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" 
    @Time    : 2018/12/20 11:25
    @Author  : Junting
    @File    : buc.py
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

youtubeFrame = pd.read_csv("ultimate_data.csv", encoding="utf-8")
minSup = 2

propertyRange = ('publish_time', 'trending_date', 'category_id', "channel_title")
supportedSet = {}


def buc(pointerProp, currentEntrySet):
    if pointerProp != 4:
        if len(currentEntrySet) == 0:
            if pointerProp == 0:
                currentEntrySet = countDiffAttributes(propertyRange[pointerProp], currentEntrySet)
                buc(pointerProp + 1, currentEntrySet)
            else:
                pass
        else:
            for dictPairs in currentEntrySet.items():
                print("  %s   support: %s" % (dictPairs[0], str(len(dictPairs[1]))))
                supportedSet[dictPairs[0]] = len(dictPairs[1])
                currentEntrySet = countDiffAttributes(propertyRange[pointerProp], dictPairs)
                buc(pointerProp + 1, currentEntrySet)
    else:
        for dictPairs in currentEntrySet.items():
            print("  %s   support: %s" % (dictPairs[0], str(len(dictPairs[1]))))


def countDiffAttributes(column, listOfPreviousAttribute):
    temp = {}
    medium = {}
    result = {}
    column = youtubeFrame[column]
    if len(listOfPreviousAttribute) == 0:
        for itemCount, item in enumerate(column):
            if item not in temp:
                temp[item] = [itemCount]
            else:
                if item in result.keys():
                    result[item].append(itemCount)
                else:
                    temp[item].append(itemCount)
                    if len(temp[item]) >= minSup:
                        result[item] = temp[item]
    else:
        previousKey = listOfPreviousAttribute[0]
        for rowCount in listOfPreviousAttribute[1]:
            item = column[rowCount]
            if item not in temp:
                temp[item] = [rowCount]
            else:
                if item in medium.keys():
                    medium[item].append(rowCount)
                else:
                    temp[item].append(rowCount)
                    if len(temp[item]) >= minSup:
                        medium[item] = temp[item]
        for keys in medium.keys():
            result["   |   ".join((str(previousKey), str(keys)))] = medium[keys]

    # {item in that col: list of item count}
    return result


print("    ".join(propertyRange))
buc(0,{})
