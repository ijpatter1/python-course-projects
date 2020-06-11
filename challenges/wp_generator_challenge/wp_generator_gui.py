
from tkinter import *
import tkinter as tk
import tkinter.messagebox

import wp_generator_main
import wp_generator_func

def load_gui(self):

    self.label_body = tk.Label(self.master,text="Enter body text here:")
    self.label_body.config(font=10)
    self.label_body.grid(row=0,column=0,padx=(7,0),pady=(10,2),sticky=W)

    self.scrollbar1 = Scrollbar(self.master,orient=VERTICAL)
    self.txt_body = tk.Text(self.master,yscrollcommand=self.scrollbar1.set,font=12,width=52,height=20)
    self.scrollbar1.config(command=self.txt_body.yview)
    self.scrollbar1.grid(row=1,column=3,rowspan=2,columnspan=1,padx=(3,0),pady=(0,0),sticky=N+E+S)
    self.txt_body.grid(row=1,column=0,rowspan=2,columnspan=3,padx=(7,0),pady=(0,0),sticky=N+E+S+W)

    self.btn_create = tk.Button(self.master,width=10,height=3,text="Create\nWeb Page",command=lambda: wp_generator_func.addToBody(self))
    self.btn_create.config(font=12)
    self.btn_create.grid(row=3,column=0,padx=(7,0),pady=(7,7),sticky=N+S+W)
    self.btn_clear = tk.Button(self.master,width=10,height=3, text="Clear\nText",command=lambda: wp_generator_func.clearTxt(self))
    self.btn_clear.config(font=12)
    self.btn_clear.grid(row=3, column=2,padx=(0,0),pady=(7,7),sticky=N+E+S)

if __name__ == "__main__":
    pass
