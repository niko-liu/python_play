# encoding: utf-8
'''
Created on 2017年11月11日

@author: niko
'''

import os 
import re

def rename_file():
    path = r"/Users/niko/niko_dev/prank"
    files = os.listdir(path);
    regx = r'(?:[\d]*)([\D]+)'
    for f in files :
        print(f)
        if f == '.DS_Store' :
            continue
        matcher = re.match(regx, f, re.DOTALL | re.IGNORECASE)
        if matcher:
            print(f + " match: " + matcher.group(1))
            nfname = matcher.group(1)
            os.rename(path + "/" + f, path + "/" + nfname)
            print "rename file " + f + " to " + nfname

def translate():
    f = "48abc.jpg"
    path = r"/Users/niko/niko_dev/prank"
    nf = f.translate(None, "0123456789")
    rootPath = os.getcwd()
    print rootPath
    os.chdir(path)
    rootPath = os.getcwd()
    print rootPath
    
    print nf
    
translate()

'''rename_file()'''