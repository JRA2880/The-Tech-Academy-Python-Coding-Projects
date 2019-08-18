# Programmer: John R. Adams
#
# Date: 08-17-2019
#
# Purpose: Directory Database functions

from tkinter import *
from tkinter.filedialog import askdirectory
import tkinter as tk
import sqlite3
import shutil
import os
import sys
import time

import Directory_main
import Directory_gui


def search(self):
    currentDirectory = askdirectory()
    if currentDirectory:
        self.varSource.set(currentDirectory)

def locate(self):
    location = askdirectory()
    if location:
        self.varLocation.set(location)

def transfer(self):

    files = []
    dictionary = {}
    directory = self.varSource.get()
    destination = self.varLocation.get()
    fileDirectory = os.listdir(directory)
    for file in fileDirectory:
        if file.lower().endswith('.txt'):
            files.append(file)
            shutil.move(os.path.join(directory,file),destination) 
            for name in files: 
                apath = os.path.join(destination, name)
                mtime = os.path.getmtime(apath)
                dictionary[name] = mtime
    createDB(self, dictionary)


def createDB(self, dictionary):
    conn = sqlite3.connect("directoryDB.db")
    with conn:
        cur = conn.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS tbl_files( \
                    ID INTEGER PRIMARY KEY AUTOINCREMENT, \
                    col_filename TEXT, \
                    col_time REAL)")
        for file, value in dictionary.items():
            cur.execute("INSERT INTO tbl_files (col_filename,col_time) VALUES (?,?)",
                        (file, dictionary[file]))
            conn.commit()
        cur.execute("SELECT col_filename, col_time FROM tbl_files")
        rows = cur.fetchall()
        for row in rows: 
            print(row)

def close(self):
    self.master.destroy()



if __name__ == "__main__":
    pass
            
    


    
    
