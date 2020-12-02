from tkinter import *
from PIL import ImageTk # needed to read most non-GIF formats. Would also need to import Image from PIL in order to perform Image.open() before ImageTK.PhotoImage() if JPG file

root = Tk()

textLabel = Label(root,
                  text="Label",
                  justify=LEFT,
                  padx=10)
textLabel.pack(side=LEFT)

photo = ImageTk.PhotoImage(file="cat.gif")
imgLabel = Label(root, image=photo)
imgLabel.pack(side=RIGHT)

mainloop()