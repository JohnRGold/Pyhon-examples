'''Doesn't have sub-windows, but a forum person considered this to be good practice. The class for the app
does not inherit directly from tkinter widgets, but a Frame widget is created inside the class constructor.
Source:
https://stackoverflow.com/questions/17466561/best-way-to-structure-a-tkinter-application
Comment is below the op.'''

from tkinter import *

class App:
      def __init__(self, master):
            frame = Frame(master)
            frame.pack()
            self.button = Button(frame, text="QUIT", fg="red", command=frame.quit)
            self.button.pack(side=LEFT)
            self.slogan = Button(frame, text="Hello", command=self.write_slogan)
            self.slogan.pack(side=LEFT)

      @staticmethod
      def write_slogan():
        print("Tkinter is easy to use!")

root = Tk()
app = App(root)
root.mainloop()