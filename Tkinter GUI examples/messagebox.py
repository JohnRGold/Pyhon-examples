"""A messagebox is a little popup showing a message. Sometimes it accompanied by an icon. Almost all the times, it interrupts what the user is doing.

The examples below show you how to create and use a messagebox with tkinter. The code shown here is for Python 3.x and newer. Older versions of Python import and use tkinter differently."""

import tkinter
import tkinter.messagebox

tkinter.messagebox.showinfo('title','message')
tkinter.messagebox.showwarning('title','message')
tkinter.messagebox.showerror('title','message')