"""The radiobutton lets you select from a variety of items. They are part of the default tk module. Unlike a checkbox, a tkinter lets you select only one option.

You can achive that by adding the same variable as parameter for the radiobuttons. If a radiobutton is clicked you can call a callback function.

The program below creates 3 radiobuttons with the method Radiobutton. It adds a window as parameter, the text, the variable to connect it with and a callback function.

For it to work, all radiobuttons need to be linked to the same variable, in this example var."""

import tkinter as tk

window = tk.Tk()
window.title('My Window')
window.geometry('500x300')

var = tk.StringVar()
l = tk.Label(window, bg='white', width=20, text='empty')
l.pack()


def print_selection():
	l.config(text='you have selected ' + var.get())


r1 = tk.Radiobutton(window, text='Option A', variable=var, value='A', command=print_selection)
r1.pack()
r2 = tk.Radiobutton(window, text='Option B', variable=var, value='B', command=print_selection)
r2.pack()
r3 = tk.Radiobutton(window, text='Option C', variable=var, value='C', command=print_selection)
r3.pack()

window.mainloop()