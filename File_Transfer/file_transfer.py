import shutil
import os
from datetime import *
from threading import Timer
import schedule
import time

os.chdir('C:/Users/14236/Documents/GitHub/Python-Projects/File_Transfer/static/')
def moveModifiedFiles():

    #change working directory so python checks the correct folder
    #os.chdir('C:/Users/14236/Documents/GitHub/Python-Projects/File_Transfer/static/')
    #set where the source of the files are

    source = 'C:/Users/14236/Documents/GitHub/Python-Projects/File_Transfer/static/'

    #set the destination path to folderB

    destination = 'C:/Users/14236/Documents/GitHub/Python-Projects/File_Transfer/modified/'

    files = os.listdir(source)  #use listdir() method to put paths into list object

    ft= []
    lastEdit = []

    for i in range(len(files)):

        #create os object to enable a variable that has corrrect properties to be stored.
        ft.append(os.stat(files[i]))
        #pull time from object for each i in files
        lastEdit.append(datetime.fromtimestamp(ft[i].st_mtime))
        #if less than 24 hours ago then move file
        if lastEdit[i]>datetime.now()-timedelta(hours=24) and not files[i].endswith(".py"):
            #we are saying move the files represented by 'i' to their new destination
            shutil.move(files[i],destination)

'''
schedule.every(24).hours.do(moveModifiedFiles)
       
while 1:
    schedule.run.pending()
    timesleep(1)
    
''' #this will have the code run every 24 hours. 
