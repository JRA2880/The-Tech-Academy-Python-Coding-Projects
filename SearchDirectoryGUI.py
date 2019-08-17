# John R. Adams
# Date: 08-17-2019
#
# Python GUI Task
#
# DRILL:
#
# Drill Description:
#
# For this drill, you will need to write a script that creates a GUI with a button widget and a text widget.
# Your script will also include a function that when it is called will invoke a dialog modal which will allow users with the ability to select a folder directory from their system.
# Finally, your script will show the user’s selected directory path into the text field.

# Requirements:
# Your script will need to use Python 3 and the Tkinter module.

# Your script will need to use the askdirectory() method from the Tkinter module.

# Your script will need to have a function linked to the button widget so that once the button has been clicked will take the user’s selected file path
# retained by the askdirectory() method and print it within your GUI’s text widget.


import tkinter

import os

import sys

from tkinter import *

from tkinter import filedialog


class ParentWindow(Frame):
    def __init__(self,master):
        self.master = master
        self.master.resizable(width = True,height = True)
        self.master.geometry('{}x{}'.format(600,600))
        self.master.title('Search Directory App')
        self.master.config(bg='lightgrey')
        
        self.btnSubmit = Button(self.master,text="Search Directory",width=50,height=0,font=("Helvetica",16),fg='black',bg='grey',command=self.search)
        self.btnSubmit.grid(row=2,column=1,padx=(20,0),pady=(15,0))

        self.txtBox = Text(self.master,width=50,height=20)
        self.txtBox.grid(row=3,column=1,columnspan=2,padx=(20,0),pady=(15,0))

    def search(self):
        currentDirectory = filedialog.askdirectory()
        testFile = ''
        filePath = os.path.join(currentDirectory,testFile)
        print(filePath)

    def display(self,search):
        txtBox.insert(tk.END,search)


if __name__ == "__main__":
    root = Tk()
    App = ParentWindow(root)
    root.mainloop()



