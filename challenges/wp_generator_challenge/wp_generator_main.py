
from tkinter import *
import tkinter as tk
import tkinter.messagebox

import wp_generator_gui
import wp_generator_func


class ParentWindow(Frame):
    def __init__(self,master,*args,**kwargs):
        Frame.__init__(self,master,*args,**kwargs)

        self.master = master
        self.master.minsize(605,605)
        self.master.maxsize(605,605)
        self.master.title("Web Page Generator")

        self.master.protocol("WM_DELETE_WINDOW", lambda: wp_generator_func.ask_quit(self))

        wp_generator_gui.load_gui(self)


if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
