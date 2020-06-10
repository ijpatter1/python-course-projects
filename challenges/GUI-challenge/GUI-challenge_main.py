

# For this assignment, you will write a script that creates a GUI.
# Requirements:
# Your script will need to use Python 3 and the Tkinter module.
# Your script will need to re-create an exact copy of a GUI from the supplied image at the bottom of this page.

from tkinter import *
import tkinter as tkinter
import GUI-challenge_gui

#Frame is the Tkinter frame class that our own class will inherit from
class ParentWindow(Frame):
    def __init__(self,master,*args,**kwargs):
        Frame.__init__(self,master,*args,**kwargs)

        #define our master frame config
        self.master = master
        self.master.minsize(480,200)
        self.master.minsize(480,200)
        self.master.title("Check files")
        self.master.configure(bg="Lightgray")

        GUI-challenge_gui.load_gui(self)

if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()