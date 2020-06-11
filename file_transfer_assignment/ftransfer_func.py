

from tkinter import *
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import shutil
import os
import time

import ftransfer_main
import ftransfer_gui

def ask_quit(self):
    if messagebox.askokcancel("Exit program", "Okay to exit application?"):
        # This closes app
        self.master.destroy()
        os._exit(0)


def browse(self,btn):
    if btn == "src":
        entry = self.src_disp
    if btn == "des":
        entry = self.des_disp
    entry.config(state='normal')
    entry.delete(0,"end")
    filePath = filedialog.askdirectory()
    if filePath:
        entry.insert(0,filePath+"/")
    entry.config(state='readonly')

def check(self):
    try:
        src = self.src_disp.get()
        des = self.des_disp.get()

        lsdir = os.listdir(src)
        validFiles = []
        period = time.time()-86400

        for i in lsdir:
            mtime = os.path.getmtime(src+i)
            if mtime >= period:
                validFiles.append(i)
        if validFiles:
            for i in validFiles:
                shutil.move(src+i,des)
            messagebox.showinfo("Files transfered","File(s) successfully transferred!")
        else:
            messagebox.showinfo("No valid files","No valid files to transfer.")
    except:
        messagebox.showinfo("Enter valid directories","Please choose Source and Destination directories.")


if __name__ == "__main__":
    pass
