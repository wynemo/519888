# new_guodu_v6.exe
#http://www.guodu.com/download.jsp?fileid=000000006a1ecd0f016b9173c49e10bc  下载安装

# python

# https://www.python.org/ftp/python/3.8.1/python-3.8.1-amd64.exe 下载安装

# 找到pip.exe C:\Users\yourname\AppData\Local\Programs\Python\Python38\Scripts\pip.exe


# 命令行安装
#pip.exe install -i https://mirrors.aliyun.com/pypi/simple/  pyautogui==0.9.46 global-hotkeys

#C:\Users\user\AppData\Local\Programs\Python\Python36\python.exe C:\Users\user\519888.py

import pyautogui
import time
from global_hotkeys import register_hotkeys, start_checking_hotkeys
import sys
# import os

should_exit = 0

def check_exit():
    global should_exit
    print('exiting....')
    should_exit = 1


bindings = [
    ["control + 7", None, check_exit, True],
]

register_hotkeys(bindings)

# Finally, start listening for keypresses
start_checking_hotkeys()



while 1:
    if should_exit == 1:
        sys.exit(0)
        # os._exit(0)
    #批量下单
    pyautogui.click(62, 134)

    time.sleep(0.2)
    pyautogui.click(297, 89)
    pyautogui.typewrite('519888')


    time.sleep(0.3)
    pyautogui.click(242, 184)
    time.sleep(0.3)
    pyautogui.click(312, 186)
    time.sleep(1.8)
    pyautogui.typewrite('1000')


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
    time.sleep(0.5)
    pyautogui.click(373, 212)
    pyautogui.typewrite('10000')
    time.sleep(0.2)



    time.sleep(0.1)
    pyautogui.click(359, 236)

    time.sleep(0.5)
    pyautogui.click(1036, 616)
    time.sleep(1.5)
    pyautogui.click(1069, 573)

    time.sleep(2.5)
