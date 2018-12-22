#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" 
    @Time    : 2018/12/18 18:52
    @Author  : Junting
    @File    : to_sql.py
"""
import pandas as pd
from sqlalchemy import create_engine
import pymysql





youtubeFrame=pd.read_csv("ultimate_data.csv",encoding="utf-8")



db_info = {'user': 'root',
           'password': 'chen0898',
           'host': 'localhost',
           'database': 'youtube'
           }
engine = create_engine('mysql+pymysql://%(user)s:%(password)s@%(host)s/%(database)s?charset=utf8'
                       % db_info,encoding='utf-8')
youtubeFrame.to_sql('main_table',engine,index=False,if_exists='replace')
