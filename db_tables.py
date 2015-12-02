# -*- coding: utf-8 -*-
"""
run this script to create table stock_eod_en

"""

from datetime import  date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import (MetaData, Table, Column, Numeric, Integer, BIGINT, String, Unicode,\
                        Boolean, UnicodeText, Date, ForeignKey, create_engine)

engine = create_engine('mysql://root:911Ljsam@127.0.0.1/jusha?charset=utf8')
metadata = MetaData()
Base = declarative_base(bind= engine)



#This table stores stocks End Of Day (eod) data
stock_eod_en = Table('stock_eod_en', metadata,
                #composite primary key [symbol_id, traded_on]
                Column('symbol_id',  Unicode(8), primary_key= True),
                Column('stock_name',  Unicode(8)),\
                Column('traded_on', Date(),primary_key= True),\
                #renamming open & close is for avoding clashes with mysql keywords
                Column('industry', Unicode(20)),\
                Column('concept', Unicode(20)),\
                Column('arear', Unicode(20)),\

                Column('open_', Numeric(10,2)),\
                Column('high_', Numeric(10,2)),\
                Column('low_', Numeric(10,2)),\
                Column('close_', Numeric(10,2)),\
                Column('backward_adj_price', Numeric(10,2)),\
                Column('forward_adj_price', Numeric(10,2)),\
                Column('change_', Numeric(30,4)),\
                Column('volume', Integer()),\
                Column('turnover', BIGINT()),\
                Column('turnover_rate', Numeric(10,4)),\
                Column('circulation_value', BIGINT()),\
                Column('total_value', BIGINT()),\
                Column('limit_up', Boolean(), default= False),\
                Column('limit_down',Boolean(), default= False),\
                Column('pe', Numeric(10,2)),\
                Column('ps', Numeric(10,2)),\
                Column('pcf', Numeric(10,2)),\
                Column('pb', Numeric(10,2)),\
                Column('MA_5', Numeric(10,2)),\
                Column('MA_10', Numeric(10,2)),\
                Column('MA_20', Numeric(10,2)),\
                Column('MA_30', Numeric(10,2)),\
                Column('MA_60', Numeric(10,2)),\
                Column('MA_gold_die', String(8)),\
                Column('MACD_DIF', Numeric(10,2)),\
                Column('MACD_DEA', Numeric(10,2)),\
                Column('MACD_MACD', Numeric(10,2)),\
                Column('MACD_gold_die', String(8)),\
                Column('KDJ_K', Numeric(10,2)),\
                Column('KDJ_D', Numeric(10,2)),\
                Column('KDJ_J', Numeric(10,2)),\
                Column('KDJ_gold_die', String(8)),\
                Column('bullin_mid', Numeric(10,2)),\
                Column('bullin_up', Numeric(10,2)),\
                Column('bullin_down', Numeric(10,2)),\
                Column('psy', Numeric(10,2)),\
                Column('psyma', Numeric(10,2)),\
                Column('rsi1', Numeric(10,2)),\
                Column('rsi2', Numeric(10,2)),\
                Column('rsi3', Numeric(10,2))\
                )


class Stock_eod_en(Base):
    __table__ = stock_eod_en

if __name__=='__main__':

    metadata.bind = engine
    stock_eod_en.create()
