"""A frame in Tk lets you organize and group widgets. It works like a container. Its a rectangular area in which widges can be placed.
If you make a GUI app, you’ll be using different widgets. Those widgets need to be organized somehow, that’s where a frame comes in."""

from tkinter import *

def say_hi():
    print("hello ~ !")

root = Tk()

frame1 = Frame(root)
frame2 = Frame(root)
root.title("tkinter frame")

label= Label(frame1,text="Label",justify=LEFT)
label.pack(side=LEFT)

hi_there = Button(frame2,text="say hi~",command=say_hi)
hi_there.pack()

frame1.pack(padx=1,pady=1)
frame2.pack(padx=10,pady=10)

root.mainloop()