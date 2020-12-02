"""The tkinter entry box lets you input text in your desktop software. Usually an entry box (input field) comes with a label, that’s because without labels its not clear what the user should type there.

You can add more than one input field. The input field can show latin character but also other types of input (like passwords)"""

# !/usr/bin/python
# -*- coding: UTF-8 -*-

from tkinter import *

top = Tk()
L1 = Label(top, text="Label")
L1.pack(side=LEFT)
E1 = Entry(top, bd=5)
E1.pack(side=RIGHT)

top.mainloop()