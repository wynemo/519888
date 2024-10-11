# 配置文件 买哪些货币基金
# 非交易时间不做操作 也是配置文件
# C:\Users\admin\AppData\Local\Programs\Python\Python39\Scripts\pyinstaller.exe --onefile money_funds.py

import json
import os
import sys
import time

import pyautogui
from global_hotkeys import register_hotkeys, start_checking_hotkeys, stop_checking_hotkeys


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

while 1:
    if should_exit == 1:
        sys.exit(0)
        # os._exit(0)
    #批量下单
    pyautogui.click(62, 134)
    time.sleep(0.5)

    #证券代码
    pyautogui.click(297, 89)
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
