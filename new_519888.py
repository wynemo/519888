"""

python -m pip install pytesseract Pillow lobal_hotkeys opencv-python pyautogui


pyautogui
基金代码 点击  Point(x=245, y=69) 输入 519888

申购金额 点击 Point(x=233, y=148) 输入 1000到100000 随机


点击 Point(x=162, y=239) 我已知晓

点击 Point(x=314, y=277) 申购


点击 Point(x=1064, y=521) 确定

点击 Point(x=1037, y=515) 确定

每个过程sleep 0.5s

最后sleep 3.3s
"""

import random
import sys
import time

import cv2
import numpy as np
import pyautogui
import pytesseract
from global_hotkeys import register_hotkeys, start_checking_hotkeys, stop_checking_hotkeys

# Windows 需要指定 tesseract 路径
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

should_exit = 0

def check_exit():
    global should_exit
    print('exiting....')
    stop_checking_hotkeys()
    should_exit = 1

# 热键退出 control + 7
bindings = [
    ["control + 7", None, check_exit, True],
]

register_hotkeys(bindings)
start_checking_hotkeys()

while True:
    if should_exit == 1:
        sys.exit(0)

    # 基金代码 点击并输入 519888
    pyautogui.click(245, 69)
    time.sleep(0.5)
    pyautogui.typewrite('519888')
    time.sleep(0.5)

    # 申购金额 点击并输入 1000到100000 随机
    pyautogui.click(233, 148)
    # 双击，清除内容
    pyautogui.doubleClick(233, 148)
    # back
    pyautogui.press('backspace')


    # 判断现有钱的数量
    x1, y1 = 215, 116
    x2, y2 = 359, 134
    screenshot = pyautogui.screenshot(region=(x1, y1, x2-x1, y2-y1))
    img = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)
    text = pytesseract.image_to_string(img, lang='eng').strip()

    try:
        balance = float(text.replace(',', ''))
    except:
        print(f"无法识别金额: {text}")
        time.sleep(1)
        continue

    print(f"当前余额: {balance}")

    # 余额小于1000，跳过
    if balance < 1000:
        print("余额不足1000，跳过")
        time.sleep(1)
        continue

    # 随机金额，但不能超过余额
    max_amount = min(100000, int(balance))
    amount = random.randint(1000, max_amount)

    time.sleep(0.5)
    pyautogui.typewrite(str(amount))
    time.sleep(0.5)

    # 点击 我已知晓
    pyautogui.click(162, 239)
    time.sleep(0.5)

    # 点击 申购
    pyautogui.click(314, 277)
    time.sleep(0.5)

    # 点击 确定
    pyautogui.click(1064, 521)
    time.sleep(0.5)

    # 点击 确定
    pyautogui.click(1037, 515)
    time.sleep(0.5)

    # 最后等待
    time.sleep(3.3)
