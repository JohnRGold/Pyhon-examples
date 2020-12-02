"""Fully functional. Is capable of completely locking the parent window via wm_attributes() method,
since the main menu inherits from Tk. Second menu is defined explicitly inside the appropriate button
method. However, OOP-ing this would be relatively simple, as the Create_Toplevel() method creates a
Toplevel object anyway."""
import tkinter as tk
from tkinter import ttk

class SampleApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.minsize(300, 100)
        self.button = ttk.Button(self, text="Call toplevel!", command=self.create_toplevel)
        self.button.pack(side="top")

    def create_toplevel(self):
        # THE CLUE
        self.wm_attributes("-disabled", True)
        self.focus_set()

        # Creating the toplevel dialog
        _ = Top(self)


class Top(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.master = master

        self.focus_set()
        self.minsize(300, 100)

        # Tell the window manager, this is the child widget.
        # Interesting, if you want to let the child window
        # flash if user clicks onto parent
        self.transient(self.master)



        # This is watching the window manager close button
        # and uses the same callback function as the other buttons
        # (you can use which ever you want, BUT REMEMBER TO ENABLE
        # THE PARENT WINDOW AGAIN)
        self.protocol("WM_DELETE_WINDOW", self.close)


        self.label = ttk.Label(self, text='Do you want to enable my parent window '
                                                               'again?')
        self.label.pack(side='top')

        self.toplevel_dialog_yes_button = ttk.Button(self, text='Yes',command=self.close)
        self.toplevel_dialog_yes_button.pack(side='left', fill='x', expand=True)

        self.toplevel_dialog_no_button = ttk.Button(self, text='No')
        self.toplevel_dialog_no_button.pack(side='right', fill='x', expand=True)


    def close(self):
        # IMPORTANT!
        self.master.wm_attributes("-disabled", False)  # IMPORTANT!

        self.destroy()

        # Possibly not needed, used to focus parent window again
        self.master.focus_set()
        self.master.grab_set()

if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()
