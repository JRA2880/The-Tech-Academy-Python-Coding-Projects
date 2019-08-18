# Programmer: John R. Adams
#
# Date: 08-17-2019
#
# Python Drill: Directory Database GUI
#
# Requirements:
#
# 1.) Your script will need to use Python 3, the Tkinter module, and the OS module.
#
# 2.) Your script will need to use the listdir() method from the OS module to iterate through all files within a specific directory.
#
# 3.) Your script will need to use the path.join() method from the OS module to concatenate the file name to its file path, forming an absolute path.
#
# 4.) Your script will need to use the getmtime() method from the OS module to find out the latest date the file has been created or last modified.
#
# 5.) Your script will need to create a database to record the qualifying file and corresponding modified time-stamp.
#
# 6.) Your script will need to print each file ending with a “.txt” file extension and its corresponding mtime to the console.
#
# 7.) Your script will need to use the move() method from the Shutil module to cut all qualifying files and paste them within the destination directory.

# Additional Setup Instructions:
#
# To complete this final drill assignment, you will need to use the directory you had previously created on your system from an earlier drill assignment.
#
# This directory should have at least 10 different files types, two of which should be text documents that end with the “.txt” file extension.

from tkinter import *

import tkinter as tk

import os

import Directory_gui

import Directory_func


class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        self.master = master
        self.master.minsize(515,175)
        self.master.maxsize(1030,325)
        self.master.title("Directory Database")
        self.master.configure(bg="lightgrey")

        Directory_gui.runGUI(self)


if __name__ == "__main__":
    root = Tk()
    App = ParentWindow(root)
    root.mainloop()
    


        


