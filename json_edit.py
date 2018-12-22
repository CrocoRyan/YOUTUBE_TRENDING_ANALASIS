#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" 
    @Time    : 2018/10/25 16:08
    @Author  : Junting
    @File    : json_edit.py
"""

import json
import pandas as pd
import numpy as np
import csv


def extractInfos(country_short):
    result={}
    with open(country_short+"_category_id.json", 'r') as f:
        temp = json.loads(f.read())
        for i in temp["items"]:
            result[int(i["id"])]=i["snippet"]["title"]
    return result,sorted(result.keys())


#字典中的key值即为csv中列名
def writeCate(country_short):
    result, key_sort = extractInfos(country_short)
    #Python3.4以后的新方式，解决空行问题
    with open(country_short+'_category.csv', 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        for keys in key_sort:
            csv_writer.writerow([keys,result[keys]])


writeCate("US")
