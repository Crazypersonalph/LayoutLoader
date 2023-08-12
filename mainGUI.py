from pynput.keyboard import Key, Controller
import time
from utils.load import load

import tkinter
m = tkinter.Tk()
m.title("LayoutLoader")
title = tkinter.Label(m, text='LayoutLoader')
sub = tkinter.Label(m, text='Enter file path:')
title.pack()
sub.pack()
w=tkinter.Entry(m)
w.pack()
button = tkinter.Button(text='Submit', command=lambda : load(w.get()))
button.pack()
m.mainloop()