import os
import sys

path = 'C:\\Users\\JRA\\myProjects\\myProjects\\A'

dirs = os.listdir(path)

for file in dirs:
    if file.lower().endswith('.txt'):
        abPath = os.path.join(path,file)
        timeStamp = os.path.getmtime(path)
        print(abPath)
        print(timeStamp)
        #print(file)
        #print(timeStamp)


        

