# new_guodu_v6.exe
#http://www.guodu.com/download.jsp?fileid=000000006a1ecd0f016b9173c49e10bc  下载安装

# python

# https://www.python.org/ftp/python/3.8.1/python-3.8.1-amd64.exe 下载安装

# 找到pip.exe C:\Users\yourname\AppData\Local\Programs\Python\Python38\Scripts\pip.exe 


# 命令行安装
#pip.exe install -i https://mirrors.aliyun.com/pypi/simple/  pyautogui==0.9.46

#C:\Users\nemo\AppData\Local\Programs\Python\Python36\python.exe C:\Users\nemo\mysyncthing\519888.py

import pyautogui
import time
import random

while 1:
    #卖出
    pyautogui.click(70, 101)
    #买入
    pyautogui.click(57, 78)
    time.sleep(0.5)

    pyautogui.click(363, 116)
    #pyautogui.clear()
    i = random.randint(1, 10)
    if i < 3:
        pyautogui.typewrite('519878')
    elif i >= 3 and i < 6:
        pyautogui.typewrite('519858')
    else:
        pyautogui.typewrite('519888')
    time.sleep(1.5)
    pyautogui.click(344, 191)
    pyautogui.typewrite('10000')

    #下单
    time.sleep(0.4)
    pyautogui.click(376, 231)

    #全部
    #time.sleep(0.1)
    #pyautogui.click(377, 148)
    
    # time.sleep(0.1)
    # pyautogui.click(373, 212)
    # pyautogui.press('backspace')
    # pyautogui.press('backspace')
    # pyautogui.press('backspace')
    # pyautogui.press('backspace')
    # time.sleep(0.1)
    # pyautogui.typewrite('0')
    # pyautogui.typewrite('0')

    #是
    pyautogui.click(909, 635)

    time.sleep(1.5)
    #确定
    pyautogui.click(953, 597)
    time.sleep(3.9)

    
    time.sleep(3.3)
