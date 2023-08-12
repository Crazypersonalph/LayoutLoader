from pynput.keyboard import Key, Controller
import time
import argparse
keyboard = Controller()
import pygetwindow as gw

parser = argparse.ArgumentParser()
parser.add_argument("-c", "--config", help = "The layout you want to load", required=True)

args = parser.parse_args()
win = gw.getWindowsWithTitle('Roblox')[0] 
win.activate()
time.sleep(1)

config_file = open(args.config,"r")
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