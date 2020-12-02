"""Python Tkinter (and TK) offer a set of dialogs that you can use when working with files. By using these you don’t have to design standard dialogs your self. Example dialogs include an open file dialog, a save file dialog and many others. Besides file dialogs there are other standard dialogs, but in this article we will focus on file dialogs.

File dialogs help you open, save files or directories. This is the type of dialog you get when you click file, open. This dialog comes out of the module, there’s no need to write all the code
manually.

Tkinter does not have a native looking file dialog, instead it has the customer tk style.

The tkinter filedialog comes in several types. Which type you need really depends on your applications needs. All of them are methods calls.

You can open a single file, a directory, save as file and much more. Each dialog made with the example below is a different type of dialog."""

import tkinter.filedialog

tkinter.filedialog.asksaveasfilename()
tkinter.filedialog.asksaveasfile()
tkinter.filedialog.askopenfilename()
tkinter.filedialog.askopenfile()
tkinter.filedialog.askdirectory()
tkinter.filedialog.askopenfilenames()
tkinter.filedialog.askopenfiles()


# You can create an open file dialog which asks for a filename, and then returns the name of the selected dialog.
import tkinter as tk
from tkinter import filedialog as fd


def callback():
	name = fd.askopenfilename()
	print(name)


errmsg = 'Error!'
tk.Button(text='Click to Open File',
		  command=callback).pack(fill=tk.X)
tk.mainloop()