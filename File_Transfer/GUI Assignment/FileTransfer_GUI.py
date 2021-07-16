from tkinter import *
import tkinter as tk
import FileTransfer_func

def load_gui(self):

    #create button widget

    self.b1 = tk.Button(self.master,width=12,text = "Origin Folder", command = lambda:FileTransfer_func.getDir_org(self))
    self.b2 = tk.Button(self.master,width=12,text = "Dest Folder", command = lambda:FileTransfer_func.getDir_dest(self))
    self.b3 = tk.Button(self.master,width=12,height = 3,text = "Move Files", command = lambda:FileTransfer_func.MoveFile(self))
    #add grid to place button on page
    self.b1.grid(row=0, column =0, padx =(10,0), pady =(10,0))
    self.b2.grid(row=1,column =0, padx =(10,0), pady =(10,0))
    self.b3.grid(row=2,column =5, padx =(10,0), pady =(10,0))
    #add text
    self.txt1 = tk.Entry(self.master,text='',width = 50)
    self.txt2 = tk.Entry(self.master,text='',width = 50)
    #add grid for text
    self.txt1.grid(row = 0, column =1,  padx = (10,0), pady = (10,0), sticky = N+E+W)
    self.txt2.grid(row = 1, column =1,  padx = (10,0), pady = (10,0), sticky = N+E+W)

    #remember call your funciton

if __name__ =="__main__":
    pass
