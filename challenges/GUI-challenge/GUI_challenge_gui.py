from tkinter import *
import tkinter as tk
import GUI_challenge_main

def load_gui(self):
    # buttons
    self.btn_brws1 = tk.Button(self.master,width=12,height=2,text="Browse...")
    self.btn_brws1.grid(row=0,column=0,padx=(30,20),pady=(40,10),sticky=W)
    self.btn_brws2 = tk.Button(self.master,width=12,height=2,text="Browse...")
    self.btn_brws2.grid(row=1,column=0,padx=(30,20),pady=(0,10),sticky=W)
    self.btn_chk = tk.Button(self.master,width=12,height=4,text="Check for files...")
    self.btn_chk.grid(row=2,column=0,padx=(0,20),pady=(0,10),sticky=W)
    self.btn_cl = tk.Button(self.master,width=12,height=4,text="Close Program")
    self.btn_cl.grid(row=2,column=2,padx=(20,0),pady=(0,10),sticky=E)

    # inputs
    self.entry1 = tk.Entry(self.master,text='')
    self.entry1.grid(row=0,column=1,rowspan=1,columnspan=2,padx=(30,20),pady=(40,10),sticky=N+E+W)
    self.entry2 = tk.Entry(self.master,text='')
    self.entry2.grid(row=1,column=1,rowspan=1,columnspan=2,padx=(30,20),pady=(10,10),sticky=N+E+W)

if __name__ == "__main__":
    pass