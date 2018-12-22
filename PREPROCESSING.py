#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" 
    @Time    : 2018/10/25 17:45
    @Author  : Junting
    @File    : PREPROCESSING.py
"""

import numpy as np
import pandas as pd
import math

def desType(frame):
    temp=frame[2:3]
    print(temp)
    print(temp["dislikes"])
def move(dataframe,count):
    col_names = dataframe.columns  # 所有维度名字
    # temp=dataframe[count:count+1]
    # source=temp.loc[:,col_names[3:14]]
    # source_head=temp.loc[:,col_names[:4]]
    # value_list1=[source[names] for names in col_names[3:14]]
    # value_list2=[source_head[names] for names in col_names[:4]]
    # value_list2[3]=np.nan
    list=[n for n in range(4,len(col_names))]
    list.reverse()
    temp=dataframe.iloc[count,9]

    for i in list:
        dataframe.iloc[count,i]=dataframe.iloc[count,i-1]
    dataframe.iloc[count,3]=np.nan
    # dataframe.iloc[count,10]=temp
    print(dataframe.iloc[count,10])
    return temp
    # print(dataframe.iloc[count,4])

    # print(value_list2)
    # print(value_list2.extend(value_list1))
    # dataframe.loc[count]=value_list2.extend(value_list1)
    # print(list)
    # print("*********",temp["title"])
    # print("ooooooooooo",temp[names])
def changeType(dataframe,dataname_list): #返回出错的行数，供检查
    result=[]
    error={}

    count=0
    for names in dataname_list:
        print(names,"********************")
        for i in dataframe[names]:
            if isinstance(i,str) and i.endswith(".jpg"):  #修正
                error[count]=move(dataframe,count)  # 平移

            if i!=np.nan or i=="":
                # print(i)
                try:
                    temp=int(i)
                    result.append(temp)
                except:
                    result.append(i)

            else:
                result.append(np.nan)
            count+=1

        dataframe[names] = result
        result.clear()
        count=0
    temp_d=dataframe["thumbnail_link"]
    temp_d.to_csv("thumb.csv")
    del dataframe["thumbnail_link"]
    for keys in error:
        dataframe.iloc[keys,10]=error[keys]
    return error

# def publishTimeModi(frame):
#     result=[items[:-5].split("T") for items in frame["publish_time"]]
#     # result=[]
#     # count=0
#     # for items in frame["publish_time"]:
#     #     # if isinstance(items,float):
#     #     #     print(frame.iloc[count,4])
#     #     #     result.append(count)
#     #     if not items.startswith("2"):
#     #         result.append(count)
#     #     count+=1
#     # print(result)
#     frame["publish_spetime"]
def trashBox(frame):
    temp=frame.iloc[:,3]
    for count in range(len(temp)):
        if "," in temp[count]:
            k=3
            for infos in temp[count].split(","):
                frame.iloc[count,k]=infos
                k+=1
def dealTime(frame):
    f_time=frame["trending_date"]
    result=[]
    head="20"
    for i in frame:
            temp=head+i.replace(".","-")
            result.append(temp)
    frame["modi_date"]=result

youtb_frame=pd.read_csv("USvideos.csv",encoding="ISO-8859-1")
trashBox(youtb_frame)  #展开聚集单元格
print(youtb_frame.iloc[3374,3])
new_frame=youtb_frame.loc[:,youtb_frame.columns[:15]] #去掉垃圾列（此时无description）
desc=youtb_frame.loc[:,youtb_frame.columns[15:]]
desc.to_csv("description.csv")
col_names=new_frame.columns #所有维度名字
print(changeType(new_frame,("comment_count","likes","dislikes")))
# dealTime(new_frame)
print(new_frame.iloc[440,9])
# new_frame.to_csv("test.csv")


# changeType(youtb_frame,("likes","dislikes","comment_count"))  #str->int or nan

# # print(new_frame[440:441])

# print(new_frame.describe())
# print(new_frame.head())




# print(new_frmae.head())
# print(youtb_frame.columns)
# changeType(youtb_frame,(""))
# desType(youtb_frame)

