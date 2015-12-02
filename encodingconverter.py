#encoding=utf-8
"""

"""

import os
import glob
class Encoding:
    def __init__(self):

        self.ext = ".*"

        self.srcEncoding='gb2312'
        self.dstEncoding='utf-8'
    def convertEncoding(self, content, srcEncoding=None, dstEncoding=None):
        return content.decode(self.srcEncoding).encode(self.dstEncoding)
    def processDirectory(self, args, dirname, filenames):
        print 'Directory', dirname
        for filename in filenames:
            if filename == '.DS_Store': continue
            if not os.path.isdir(dirname+'/'+filename):
                if filename.endswith(self.ext) or self.ext == ".*":
                    print ' File', filename
                    self.f2f(dirname+'/'+filename)
    def f2f(self, filepath, srcEncoding=None, dstEncoding=None):
        try:
            f1 = open(filepath, 'rb')
            temp = f1.read()
            f1.close()
            f2 = open(filepath, 'wb')
            f2.write(temp.decode(self.srcEncoding).encode(self.dstEncoding))
            f2.close()
            print 'encoding successe!'
        except Exception, e:
            print e

    def colectFileType(self, dirname, fileType):
        for filename in glob.glob(r'*.'+fileType):
            print filename
    def setExt(self, ext='.csv'):
        if not ext.startswith('.'):
            ext = "." + ext
        self.ext = ext
    def setSRC(self, encoding):
        self.srcEncoding=encoding
    def setDST(self, encoding):
        self.dstEncoding=encoding
if __name__ == '__main__':
    obj = Encoding()

    obj.setExt('.csv')

    obj.setSRC('gb2312')

    obj.setDST('utf-8')
    """obj.setExt('html')
    obj.setSRC('gbk')
    obj.setDST('utf-8')"""
    path_to_store = "../data/eod_data_daily/2015-09-11/"
    path = raw_input("please input ur data directory:")
    os.path.walk(path, obj.processDirectory, None)