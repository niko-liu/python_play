# encoding: utf-8
'''
Created on 2017年11月11日

@author: niko
'''

import time
import webbrowser

if __name__ == '__main__':
    t = time.time()
    twoHours = 10
    url = "http://v.youku.com/v_show/id_XMjg0NzQ5ODQzMg==.html?spm=a2h0k.8191407.0.0&from=s1.8-1-1.2"
    while (1) :
        now = time.time()
        if (now - t) >= twoHours :
            print("两小时时间到，是时候休息一下")
            webbrowser.open(url)
            time.sleep(300)
            t = time.time()
        else :
            print("时间不到两小时")
            time.sleep(1)
            
    pass