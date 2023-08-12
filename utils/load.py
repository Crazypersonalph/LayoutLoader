from pynput.keyboard import Key, Controller
import time
import pygetwindow as gw

keyboard = Controller()

def init():
    win = gw.getWindowsWithTitle('Roblox')[0] 
    win.activate()
    time.sleep(1)

def load(file_path):
    init()
    config_file = open(file_path,"r")
    config = config_file.readlines()

    for i in config:
        keyboard.press('/')
        keyboard.release('/')
        time.sleep(1)
        keyboard.type(i.replace("\n", ""))
        time.sleep(1)
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
        time.sleep(1)