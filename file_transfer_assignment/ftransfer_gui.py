from tkinter import *
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox

import ftransfer_main
import ftransfer_func

def load_gui(self):
    # buttons
    self.btn_brws1 = tk.Button(self.master,width=15,height=1,text="Source...",command=lambda: ftransfer_func.browse(self,"src"))
    self.btn_brws1.grid(row=0,column=0,padx=(20,30),pady=(40,0),sticky=W)
    self.btn_brws2 = tk.Button(self.master,width=15,height=1,text="Destination...",command=lambda: ftransfer_func.browse(self,"des"))
    self.btn_brws2.grid(row=1,column=0,padx=(20,30),pady=(10,0),sticky=W)
    self.btn_chk = tk.Button(self.master,width=15,height=2,text="Check for files...",command=lambda: ftransfer_func.check(self))
    self.btn_chk.grid(row=2,column=0,padx=(20,30),pady=(10,10),sticky=W)
    self.btn_cl = tk.Button(self.master,width=15,height=2,text="Close Program",command=lambda: ftransfer_func.ask_quit(self))
    self.btn_cl.grid(row=2,column=2,padx=(0,20),pady=(10,10),sticky=E)

    # displays for source and destination directory paths
    self.src_disp = tk.Entry(self.master,width=48,text='')
    self.src_disp.config(state='readonly')
    self.src_disp.grid(row=0,column=1,rowspan=1,columnspan=2,padx=(0,20),pady=(40,0),sticky=N+E+W)
    self.des_disp = tk.Entry(self.master,width=48,text='')
    self.des_disp.config(state='readonly')
    self.des_disp.grid(row=1,column=1,rowspan=1,columnspan=2,padx=(0,20),pady=(10,0),sticky=N+E+W)

if __name__ == "__main__":
    pass
