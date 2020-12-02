'''Doesn't work. It is a partial completion of a placeholder scheme I found, and it still doesn't.'''
from tkinter import *

class Window1:
    def __init__(self, master):
        self.master = master
        self.bt1 = Button(self.master, text="Window 2", command=self.button_click)

    def button_click(self):
        _ = Window2(self)


class Window2:
    def __init__(self, master):
        self.master = master
        self.window = Toplevel(master)
        self.bt2 = Button(self.window, text="Exit", command=self.button_method)

    def button_method(self):
        self.master.destroy()

def main(): #run mianloop
    root = Tk()
    _ = Window1(root)
    root.mainloop()

if __name__ == '__main__':
    main()