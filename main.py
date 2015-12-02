# -*- coding: utf-8 -*-
"""
run this script on 5:00pm every working day
"""

import daily_download
import encodingconverter
import os
from datetime import date
import csv2stockeod
from db_tables import engine, Stock_eod_en
import pandas as pd
import cPickle as pkl
import sys
import numpy as np

#change to current directory so that crontab runs it correctly
os.chdir(os.path.dirname(sys.argv[0]))

reload(sys)
sys.setdefaultencoding('UTF8')


#download data from api and rename it
path_to_store = "data/eod_data_daily/"
daily_download.daily_data_download(path_to_store)

#encoding to utf-8
obj = encodingconverter.Encoding()
obj.setSRC('gbk')

#only encode data downloaded today
today_data_path = path_to_store + str(date.today())
os.path.walk(today_data_path , obj.processDirectory, None)


#write to db and record errors
today_file = today_data_path + '/stock_overview.csv'
error_log = {}

df = pd.read_csv(today_file,encoding='utf-8')
df.replace([np.inf, -np.inf], np.nan)
col = [i.name for i in Stock_eod_en.__table__.columns]
df.columns = col
df.replace(np.inf)

try:
    df.to_sql(name='stock_eod_en', con=engine, if_exists = 'append', index=False)
except Exception,e:
    error_log['error']=e

csv2stockeod.daily_file2_stockedo(today_file, error_log)
#write error log
if len(error_log)!= 0:
    with open('data/eod_data_daily/error_log/%s.txt'%str(date.today()), 'wb') as f:
        pkl.dump(error_log, f)



