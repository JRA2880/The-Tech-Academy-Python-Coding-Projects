# Programmer: John Adams
# Date: 08 - 17 - 2019
#
# Program Purpose: Develop a GUI that mimics a find textbox with the following:
#
# 1.) A button labeled Browse...(located to the left)
# 2.) A button labeled Browse...(located to the left)
# 3.) A text box for data input spanning several columns
# 4.) A text box for data input spanning several columns
# 5.) a button labeled Close Program in the bottom right corner.

import tkinter
from tkinter import *

class ParentWindow(Frame):
    def __init__(self,master):

        self.master = master
        self.master.resizable(width = True,height = True)
        self.master.geometry('{}x{}'.format(465,200))
        self.master.title('Check Files')
        self.master.config(bg='lightgrey')

        self.varBrowse1 = StringVar()
        self.varBrowse2 = StringVar()
        self.varCheck = StringVar()

        self.btnSubmit = Button(self.master,text="Browse...",width=15,height=1,command=self.browse)
        self.btnSubmit.grid(row=3,column=0,columnspan=2,padx=(20,0),pady=(15,0),sticky=NW)
        
        self.txtBrowse = Entry(self.master,text=self.varBrowse1,font=("Helvetica",16),fg='black',bg='white')
        self.txtBrowse.grid(row=3,column=3,columnspan=20,padx=(20,0),pady=(15,0))
     
        self.btnSubmit = Button(self.master,text="Browse...",width=15,height=1,command=self.browse)
        self.btnSubmit.grid(row=4,column=0,columnspan=2,padx=(20,0),pady=(15,0),sticky=NW)

        self.txtBrowse = Entry(self.master,text=self.varBrowse2,font=("Helvetica",16),fg='black',bg='white')
        self.txtBrowse.grid(row=4,column=3,columnspan=20,padx=(20,0),pady=(15,0))

        self.lblDisplay1 = Label(self.master,text='',font=("Helvetica",16),fg='black',bg='lightgrey')
        self.lblDisplay1.grid(row=8,column=3,padx=(0,0),pady=(0,0),sticky=W+E+N+S)

        self.lblDisplay2 = Label(self.master,text='',font=("Helvetica",16),fg='black',bg='lightgrey')
        self.lblDisplay2.grid(row=9,column=3,padx=(0,0),pady=(0,0),sticky=W+E+N+S) 
        
        self.btnSubmit = Button(self.master,text="Check for files.",width=15,height=2,command=self.check)
        self.btnSubmit.grid(row=5,column=0,columnspan=2,padx=(20,0),pady=(15,0),sticky=S+W)

        self.btnSubmit = Button(self.master,text="Close Program",width=15,height=2,command=self.close)
        self.btnSubmit.grid(row=5,column=22,columnspan=2,padx=(0,3),pady=(15,0),sticky= S+E)

        
    def browse(self):
        self.lblDisplay1.config(text='Searching...')

    def check(self):
        self.lblDisplay2.config(text='Checking files...')

    def close(self):
        self.master.destroy()

if __name__ == "__main__":
    root = Tk()
    App = ParentWindow(root)
    root.mainloop()
        
                             
