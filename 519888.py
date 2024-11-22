# 配置文件 买哪些货币基金
# 非交易时间不做操作 也是配置文件
# C:\Users\admin\AppData\Local\Programs\Python\Python39\Scripts\pyinstaller.exe --onefile money_funds.py

from datetime import datetime
import json
import os
import sys
import random
import time

import pyautogui
from global_hotkeys import register_hotkeys, start_checking_hotkeys, stop_checking_hotkeys

from util import is_within_time_ranges


should_exit = 0
CONFIG_FILE = 'config.json'
DEFAULT_EXIT_HOTKEY = "control + 7"

def get_script_folder():
    if getattr(sys, 'frozen', False):  # Check if bundled by PyInstaller
        # If it's a PyInstaller executable, use the _MEIPASS attribute
        script_folder = os.path.dirname(sys.executable)
    else:
        # Otherwise, use __file__ to get the current script's directory
        script_folder = os.path.dirname(os.path.abspath(__file__))
    return script_folder

def check_exit():
    global should_exit
    print('exiting....')
    stop_checking_hotkeys()
    should_exit = 1

_config_file = os.path.join(get_script_folder(), CONFIG_FILE)
try:
    with open(_config_file) as f:
        _config = json.loads(f.read())
except:
    _config = {}

exit_hotkey = _config.get('exit_hotkey', DEFAULT_EXIT_HOTKEY)

# check https://pypi.org/project/global-hotkeys/
bindings = [
    [exit_hotkey, None, check_exit, True],
]

register_hotkeys(bindings)

# Finally, start listening for keypresses
start_checking_hotkeys()

funds = _config.get('funds', ["519888"])

while 1:
    current_time = datetime.now().time()
    if is_within_time_ranges(current_time):
        print("当前时间在范围内")
    else:
        print("当前时间不在范围内")
        continue

    if should_exit == 1:
        sys.exit(0)
    #批量下单
    pyautogui.click(62, 134)
    time.sleep(0.5)

    #证券代码
    pyautogui.click(297, 89)
    if len(funds) == 1:
        pyautogui.typewrite(funds[0])
    else:
        i = random.randint(0, len(funds) - 1)
        pyautogui.typewrite(funds[i])

    time.sleep(1.5)

    #单笔数量
    pyautogui.click(312, 184)
    pyautogui.click(312, 187)
    pyautogui.click(312, 186)
    pyautogui.typewrite('1000')
    time.sleep(0.4)

    #买入数量
    pyautogui.click(373, 212)
    pyautogui.typewrite('10000')
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
