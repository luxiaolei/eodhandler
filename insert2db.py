# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 11:57:46 2015

@author: xl-macbook
"""

import pandas as pd
from db_tables import engine, Stock_eod_en
import sys
import os

reload(sys)
sys.setdefaultencoding('UTF8')

file_path = raw_input('please put your csv files directory:')

files_dir = os.listdir(file_path)
files_dir = [file_path+ i for i in files_dir]

col = [i.name for i in Stock_eod_en.__table__.columns]

error = {}
loop =0
for ff in files_dir[1:]:

    df = pd.read_csv(ff,encoding='utf-8')
    df.columns = col

    try:
        df.to_sql(name='stock_eod_en', con=engine, if_exists = 'append', index=False)
    except Exception,e:
        print e
    loop +=1
    print loop/len(files_dir)


