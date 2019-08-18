# Programmer: John R. Adams
#
# Date: 08-17-2019
#
# Purpose: Directory Database GUI

from tkinter import *
import tkinter as tk

import Directory_main
import Directory_func

def runGUI(self):

    self.varSource = StringVar()
    self.varLocation = StringVar()

    self.btn_browse1 = tk.Button(self.master,width=12,height=1,text='Browse >>',command=lambda: Directory_func.search(self)) 
    self.btn_browse1.grid(row=2,column=0,padx=(20,0),pady=(45,10),sticky=N+W)
    self.btn_browse2 = tk.Button(self.master,width=12,height=1,text='Browse >>',command=lambda: Directory_func.locate(self)) 
    self.btn_browse2.grid(row=3,column=0,padx=(20,0),sticky=N+W)
    self.btn_transfer = tk.Button(self.master,width=12,height=2,text='Transfer files >>',command=lambda: Directory_func.transfer(self)) 
    self.btn_transfer.grid(row=4,column=0,padx=(20,0),pady=(5,0),sticky=N+W)
    self.btn_close = tk.Button(self.master,width=12,height=2,text='Close Program',command=lambda: Directory_func.close(self)) 
    self.btn_close.grid(row=4,column=2,padx=(285,0))

    self.txt_search1 = tk.Entry(self.master,text=self.varSource,width=60) 
    self.txt_search1.grid(row=2,column=1,columnspan=2,padx=(15,0),pady=(40,7))
    self.txt_search2 = tk.Entry(self.master,text=self.varLocation, width=60) 
    self.txt_search2.grid(row=3,column=1,columnspan=2,padx=(15,0),pady=(0,10))

 
if __name__ == "__main__":
    pass
