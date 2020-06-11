
import os
from tkinter import *
import tkinter as tk
import tkinter.messagebox

import wp_generator_main
import wp_generator_gui

def ask_quit(self):
    if messagebox.askokcancel("Exit program", "Okay to exit application?"):
        # This closes app
        self.master.destroy()
        os._exit(0)

def addToBody(self):
    try:
        body = self.txt_body.get(1.0,"end")
        f = open("index.html","w")
        f.write(f"<html>\n \
                \t<body>\n \
                \t\t{body}\n \
                \t</body>\n \
                <html>")
        messagebox.showinfo("Success!","The file was successfully created!")
    except:
        messagebox.showinfo("Oops!","Something went wrong...")


def clearTxt(self):
    self.txt_body.delete(1.0,"end")


if __name__ == "__main__":
    pass
