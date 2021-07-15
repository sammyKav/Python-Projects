from tkinter import *
import tkinter as tk
import CreateHTML_func
import CreateHTML_GUI

class ParentWindow(Frame): #self is referring to ParentWindow, #master is referring to Frame
    def __init__(self,master):
        self.master = master
        Frame.__init__(self,master)
        self.master = master
        self.master.title("Submit Web Content")
        self.master.minsize = (600,300)
        self.master.maxsize = (600,300)

        #load gui
        CreateHTML_GUI.load_gui(self)
    


if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
