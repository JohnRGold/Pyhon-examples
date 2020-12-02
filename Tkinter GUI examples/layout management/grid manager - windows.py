#!/usr/bin/env python3

"""
ZetCode Tkinter tutorial

In this script, we use the grid
manager to create a more complicated Windows
layout.

Author: Jan Bodnar
Website: www.zetcode.com
"""

from tkinter import Tk, Text, BOTH, W, N, E, S
from tkinter.ttk import Frame, Button, Label, Style


class Example(Frame):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        self.master.title("Windows")
        self.pack(fill=BOTH, expand=True)

        self.columnconfigure(1, weight=1)
        self.columnconfigure(3, pad=7)
        self.rowconfigure(3, weight=1)
        self.rowconfigure(5, pad=7)

        lbl = Label(self, text="Windows")
        lbl.grid(sticky=W, pady=4, padx=5)

        area = Text(self)
        area.grid(row=1, column=0, columnspan=2, rowspan=4,
            padx=5, sticky=E+W+S+N)

        abtn = Button(self, text="Activate")
        abtn.grid(row=1, column=3)

        cbtn = Button(self, text="Close")
        cbtn.grid(row=2, column=3, pady=4)

        hbtn = Button(self, text="Help")
        hbtn.grid(row=5, column=0, padx=5)

        obtn = Button(self, text="OK")
        obtn.grid(row=5, column=3)


def main():

    root = Tk()
    root.geometry("350x300+300+300")
    _ = Example()
    root.mainloop()


if __name__ == '__main__':
    main()

"""In this example, we use a Label widget, a Text widget, and four buttons.

self.columnconfigure(1, weight=1)
self.columnconfigure(3, pad=7)
self.rowconfigure(3, weight=1)
self.rowconfigure(5, pad=7)
We define some space among widgets in the grid. The weight parameter makes the second column and fourth row 
growable. This row and column is occupied by the text widget, so all the extra space is taken by it.

lbl = Label(self, text="Windows")
lbl.grid(sticky=W, pady=4, padx=5)
The label widget is created and put into the grid. If no column and row is specified, then the first column or
row is assumed. The label sticks to the west and it has some padding around its borders.

area = Text(self)
area.grid(row=1, column=0, columnspan=2, rowspan=4,
    padx=5, sticky=E+W+S+N)
The text widget is created and starts from the second row and first column. 
It spans two columns and four rows. There is a 4px space between the widget and the left border of the root 
window. Finally, the widget sticks to all the four sides. So when the window is resized, the text widget grows
in all directions.

abtn = Button(self, text="Activate")
abtn.grid(row=1, column=3)

cbtn = Button(self, text="Close")
cbtn.grid(row=2, column=3, pady=4)
These two buttons go next to the text widget.

hbtn = Button(self, text="Help")
hbtn.grid(row=5, column=0, padx=5)

obtn = Button(self, text="OK")
obtn.grid(row=5, column=3)
These two buttons go below the text widget; the Help button takes the first column, the Ok Button takes the 
last column.

"""