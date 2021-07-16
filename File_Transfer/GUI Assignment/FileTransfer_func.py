import shutil
import os
from datetime import *
from threading import Timer
import schedule
import time
import tkinter.filedialog as fd
import FileTransfer_GUI
import FileTransfer_Main
from tkinter import *

os.chdir('C:/Users/14236/Documents/GitHub/Python-Projects/File_Transfer/static/')

def getDir_org(self):
    # use fd object to get folder for destination.
    self.source = fd.askdirectory()
    source = self.source
    self.txt1.delete(0,END)
    self.txt1.insert(0,self.source)
    
    


def getDir_dest(self):
    
    # use fd object to get folder for destination.
    self.dest = fd.askdirectory()
    dest = self.dest
    self.txt2.delete(0,END)
    self.txt2.insert(0,dest)
  

def MoveFile(self):
    self.ft= [] # declare a list var for times
    self.lastEdit = [] 

    self.files = os.listdir(self.txt1.get())  #use listdir() method to put paths into list object
    os.chdir(self.txt1.get())
    for i in range(len(self.files)):

        #create os object to enable a variable that has corrrect properties to be stored.
        self.ft.append(os.stat(self.files[i]))
        #pull time from object for each i in files
        self.lastEdit.append(datetime.fromtimestamp(self.ft[i].st_mtime))
        #if less than 24 hours ago then move file
        if self.lastEdit[i]>datetime.now()-timedelta(hours=24) and not self.files[i].endswith(".py"):
            #move the files for each 'i' to their new destination if any changes have been made in the last 24 hours
            shutil.move(self.files[i],self.txt2.get())

'''
schedule.every(24).hours.do(moveModifiedFiles)
       
while 1:
    schedule.run.pending()
    timesleep(1)
    
''' #this will have the code run every 24 hours.

if __name__ == "__main__":
    pass
