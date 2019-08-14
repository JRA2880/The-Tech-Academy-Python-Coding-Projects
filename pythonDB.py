#Programmer: John R. Adams
# Date: 08-13-2019
# Program Drill:
#
# For this drill, you will need to write a script that creates a database and adds new data into that database.
#
#Requirements:
#
# 1.) Your script will need to use Python 3 and sqlite3 module.
# 2.) Your database will require two fields, an auto-increment primary integer field and a field with the data type string.
# 3.) Your script will need to read from the supplied list of file names at the bottom of this page and determine only the files from the list which ends with a “.txt” file extension.
# 4.) Next, your script should add those file names from the list ending with “.txt” file extension within your database.
# 5.) Finally, your script should legibly print the qualifying text files to the console.
#
# 6.) File List:
#
#   fileList = ('information.docx','Hello.txt','myImage.png', \
#               'myMovie.mpg','World.txt','data.pdf','myPhoto.jpg')

import sqlite3
import sys

conn = sqlite3.connect('database.db')

with  conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_items(\
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        col_itemName TEXT, \
        col_itemType TEXT)"
        )
    conn.commit()

conn.close()


conn = sqlite3.connect('database.db')

with conn:
    cur = conn.cursor()
    cur.execute("INSERT INTO tbl_items(col_itemName,col_itemType) VALUES (?,?)",\
                ('seedData','test'))
    conn.commit()
conn.close()

conn = sqlite3.connect('database.db')

with conn:
    cur = conn.cursor()
    dirs = ('information.docx','Hello.txt','myImage.png','myMovie.mpg','World.txt','data.pdf','myPhoto.jpg')
    for item in dirs:
        if item.lower().endswith('.txt'):
             cur.execute("INSERT INTO tbl_items(col_itemName,col_itemType) VALUES(?,?)",\
                        (item,'txt file'))
             print(item)
    conn.commit()
conn.close()
                        
        




