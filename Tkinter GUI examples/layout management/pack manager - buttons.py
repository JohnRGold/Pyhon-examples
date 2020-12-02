#!/usr/bin/env python3

"""
ZetCode Tkinter tutorial

In this script, we use the pack manager
to position two buttons in the
bottom-right corner of the window.

Author: Jan Bodnar
Website: www.zetcode.com
"""

from tkinter import Tk, RIGHT, BOTH, RAISED
from tkinter.ttk import Frame, Button, Style

class Example(Frame):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        self.master.title("Buttons")
        self.style = Style()
        self.style.theme_use("default")

        frame = Frame(self, relief=RAISED, borderwidth=1)
        frame.pack(fill=BOTH, expand=True)

        self.pack(fill=BOTH, expand=True)

        closeButton = Button(self, text="Close")
        closeButton.pack(side=RIGHT, padx=5, pady=5)
        okButton = Button(self, text="OK")
        okButton.pack(side=RIGHT)


def main():

    root = Tk()
    root.geometry("300x200+300+300")
    _ = Example()
    root.mainloop()


if __name__ == '__main__':
    main()

"""We have two frames. There is the base frame and an additional frame, which expands in both directions and push the two buttons to the bottom of the base frame. The buttons are placed in a horizontal box and placed to the right of this box.

frame = Frame(self, relief=RAISED, borderwidth=1)
frame.pack(fill=BOTH, expand=True)
We create another Frame widget. This widget takes the bulk of the area. We change the border of the frame so that the frame is visible; by default it is flat.

closeButton = Button(self, text="Close")
closeButton.pack(side=RIGHT, padx=5, pady=5)
A closeButton is created. It is put into a horizontal box. The side parameter causes the button to be placed to the right of the horizontal. The padx and the pady parameters put some space between the widgets. The padx puts some space between the button widgets and between the closeButton and the right border of the root window. The pady puts some space between the button widgets and the borders of the frame and the borders of the root window.

okButton.pack(side=RIGHT)
The okButton is placed next to the closeButton with 5 px space between them."""