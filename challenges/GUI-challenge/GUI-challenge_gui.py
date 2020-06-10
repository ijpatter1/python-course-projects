from tkinter import *
import tkinter as tk
import GUI-challenge_main

def load_gui(self):
    # buttons
    self.btn_brws1 = tk.Button(self.master,width=12,height=2,text="Browse...")
    self.btn_brws1.grid(row=0,column=0)
    self.btn_brws2 = tk.Button(self.master,width=12,height=2,text="Browse...")
    self.btn_brws2.grid(row=1,column=0)
    self.btn_chk = tk.Button(self.master,width=12,height=4,text="Check for files...")
    self.btn_chk.grid(row=2,column=0)
    self.btn_cl = tk.Button(self.master,width=12,height=4,text="Close Program")
    self.btn_cl.grid(row=2,column=2)

    # inputs
    self.entry1 = tk.Entry(self.master,text='')
    self.entry1.grid(row=0,column=1,rowspan=1,columnspan=2)
    self.entry2 = tk.Entry(self.master,text='')
    self.entry2.grid(row=1,column=1,rowspan=1,columnspan=2)

if __name__ == "__main__":
    pass