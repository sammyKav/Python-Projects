from tkinter import *
import tkinter as tk
import CreateHTML_func
import CreateHTML_main



def load_gui(self):

    #create button to submit the text
    self.btnLaunch = tk.Button(self.master, text ="Launch Website",width = 12, height = 2, command = lambda:CreateHTML_func.makeHTML(self))
    self.btnLaunch.grid(row =0, column =0)




    #create a StringVar to keep track of user input

    self.v = tk.StringVar()


    #creating text box for user to customize html file.  

    self.txt = tk.Entry(self.master,textvariable = self.v,width =50)
    self.txt.grid( row = 0,column =1)

   


if __name__ == "__main__":
    pass
