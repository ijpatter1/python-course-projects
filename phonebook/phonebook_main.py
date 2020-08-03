#!/usr/bin/python
#
# Python Ver:   3.8.3
#
# Author:       Ian Patterson
#
# Purpose:      Phonebook Demo. Demonstrating OOP, Tkinter GUI module
#               using Tkinter Parent and Child relationships.
#
# Tested OS:    This code was written and tested to work with Windows 10.

from tkinter import *
import tkinter as tk
import tkinter.messagebox

# Be sure to import other modules
# so we can have access to them
import phonebook_gui
import phonebook_func

#Frame is the Tkinter frame class that our own class will inherit from
class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        #define our master frame config
        self.master = master
        self.master.minsize(640,400) # W and H
        self.master.maxsize(640,400)
        # This Center Window method will center our app on the user's screen
        phonebook_func.center_window(self, 640, 400)
        self.master.title("The Tkinter PHonebook Demo")
        self.master.configure(bg="#F0F0F0")
        # This protocol method is a tkinter built-in method to catch if
        # the user clicks the upper corner, "X" on Windows OS
        self.master.protocol("WM_DELETE_WINDOW", lambda: phonebook_func.ask_quit(self))

        # Load in the GUI widgets from a separate module,
        # keeping your code compartmentalized and clutter free
        phonebook_gui.load_gui(self)

if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
