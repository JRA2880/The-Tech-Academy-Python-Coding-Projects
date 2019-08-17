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
        self.master.geometry('{}x{}'.format(300,300))
        self.master.title('Search Directory App')
        self.master.config(bg='lightgrey')
        
        self.btnSubmit = Button(self.master,text="Search Directory",font=("Helvetica",16),fg='black',bg='grey',command=self.search)
        self.btnSubmit.pack()

        self.txtBox = Text(self.master)
        self.txtBox.pack()

    def search(self):
        currentDirectory = filedialog.askdirectory()
        displayDirectory = currentDirectory
        self.txtBox.insert(END,displayDirectory)
        
        path = 'C:\\Users\\JRA\\myProjects\\myProjects\\The-Tech-Academy-Python-Coding-Projects\\A'
        dirs = os.listdir(path)
        
        for file in dirs:
            if file.lower().endswith('.txt'):
                fullPath = os.path.join(path,file)
                self.txtBox.insert(END,fullPath)
                       
        
if __name__ == "__main__":
    root = Tk()
    App = ParentWindow(root)
    root.mainloop()









