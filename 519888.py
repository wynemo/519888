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
    #批量下单
    pyautogui.click(62, 134)
    time.sleep(0.5)
    #证券代码
    pyautogui.click(297, 89)
    time.sleep(0.1)
    i = random.randint(1, 10)
    if i < 3:
        pyautogui.typewrite('519878')
    elif i >= 3 and i < 6:
        pyautogui.typewrite('519858')
    else:
        pyautogui.typewrite('519888')
    time.sleep(1.5)
    #单笔数量
    pyautogui.click(312, 184)
    pyautogui.click(312, 187)
    pyautogui.click(312, 186)
    pyautogui.typewrite('1000')

    time.sleep(0.4)
    #买入数量
    pyautogui.click(373, 212)
    j = str(random.randint(1, 1)*10000)
    pyautogui.typewrite(j)
    time.sleep(0.2)

    #买入下单
    pyautogui.click(359, 236)

    time.sleep(1.5)
    pyautogui.click(1036, 616)
    time.sleep(3.9)
    pyautogui.click(1069, 573)
    pyautogui.click(1069, 573)
    pyautogui.click(1069, 573)

    time.sleep(3.3)
