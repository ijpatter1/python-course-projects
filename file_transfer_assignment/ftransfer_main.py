

from tkinter import *
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox

import ftransfer_gui
import ftransfer_func

#Frame is the Tkinter frame class that our own class will inherit from
class ParentWindow(Frame):
    def __init__(self,master,*args,**kwargs):
        Frame.__init__(self,master,*args,**kwargs)

        #define our master frame config
        self.master = master
        self.master.minsize(480,170)
        self.master.maxsize(480,170)
        self.master.title("Transfer files")
        #catch any clicks on windows 'x' box to prevent accidental program closure
        self.master.protocol("WM_DELETE_WINDOW", lambda: ftransfer_func.ask_quit(self))
        #load the gui
        ftransfer_gui.load_gui(self)

if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
