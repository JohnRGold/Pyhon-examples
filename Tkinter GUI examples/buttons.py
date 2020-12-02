"""Buttons are standard widgets in a GUI. They come with the default Tkinter module and you can place them in your window.

A Python function or method can be associated with a button. This function or method is named the callback function. If you click the button, the callback function is called.

A note on buttons: a tkinter button can only show text in a single font. The button text can be multi line. That means that this widget won’t show icons next to the text, for that you’d need another widget."""

from tkinter import *


class Window(Frame):

	def __init__(self, master=None):
		Frame.__init__(self, master)
		self.master = master

		# widget can take all window
		self.pack(fill=BOTH, expand=1)

		# create button, link it to clickExitButton()
		exitButton = Button(self, text="Exit", command=self.clickExitButton)

		# place button at (0,0)
		exitButton.place(x=0, y=0)

	def clickExitButton(self):
		exit()


root = Tk()
app = Window(root)
root.wm_title("example Tkinter button")
root.geometry("320x200")
root.mainloop()

