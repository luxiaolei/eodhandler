# -*- coding: utf-8 -*-
"""
*download daily data from yucezhe api
*return a dict with key: symbol_id, value: daily_data
"""

from urllib import urlopen
from zipfile import ZipFile
from StringIO import StringIO
import os
from datetime import date



def daily_data_download(path2store):
    """
    download daily EOF data from yucezhe api
    return a dictionary, key:symbol(without.csv) value: dataframe
    """

    def rename_downloaded_files(subpath):
        """
        replace the downloaded files' space with _
        """
        filenames = os.listdir(subpath)
        for filename in filenames:
            os.rename(os.path.join(subpath, filename), os.path.join(subpath, filename.replace(' ', '_')))


    token_url = "http://yucezhe.com/api/download/product/latest?token=8a5649858731&pdt_name=overview-push"
    try:
        download_url = urlopen(token_url).read()
        #get zip file object
        zipfile = ZipFile(StringIO(urlopen(download_url).read()))

        #create dir if not exists
        subpath = path2store+ str(date.today())
        if os.path.isdir(subpath) == False:
            os.mkdir(subpath)
            zipfile.extractall(path= subpath)
            rename_downloaded_files(subpath)



    except:
        print "download error!"

#        #check the zip file is for today
#        filedateStr = zipfile.namelist()[2][:10]
#        filename = filedateStr + " data.csv"
#
#        df = pd.read_csv(zipfile.open(filename))
#        result_dic = {}
#        print "Successfully downloaded today's data!"
#        for symbol, df in df.groupby('code'):
#            result_dic[symbol] = df
#            #result_dic[symbol] = df.ix[:, self.columns]
#        return result_dic, filedateStr
#    except: return 0, 0

if __name__== '__main__':
    path_to_store = "/data/eod_data_daily/"
    daily_data_download(path_to_store)