from tkinter import *
import tkinter as tk
import FileTransfer_GUI
import FileTransfer_func
import os


class ParentWindow(Frame):
        def __init__(self, master):
            self.master = master #self is referring to ParentWindow, #master is referring to Frame
            Frame.__init__(self,master)
            self.master = master
            self.master.title("File Transfer Tool")   
            self.master.minsize =(600,300) 
            self.master.maxsize =(600,300)

            #load GUI
            FileTransfer_GUI.load_gui(self)



                        
if __name__ == "__main__":
        root = tk.Tk()
        App = ParentWindow(root)
        root.mainloop()
