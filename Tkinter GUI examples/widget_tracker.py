from tkinter import *

class MyObj:
    def callback(self, event):
        print(event.widget.message)

obj = MyObj()
root = Tk()
btn=Button(root, text="Click")
btn.bind('<1>', obj.callback)
btn.pack()
btn.message = 'Hello'

btn2=Button(root, text="Click too")
btn2.bind('<1>', obj.callback)
btn2.message = 'Salut'
btn2.pack()

root.mainloop()