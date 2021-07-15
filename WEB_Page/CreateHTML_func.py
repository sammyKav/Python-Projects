
import webbrowser
from tkinter import *
import tkinter as tk
import CreateHTML_GUI
import CreateHTML_main
 


def makeHTML(self):
    f = open("SummerSale.html","w") # creates a new HTML document, will overwrite if document name already exists. 
    
    #add the HTML code for the webpage into a variable
    # create a text variable using get() function to get text entered into textbox on gui
    # and pass it into a variable. Then concatenate. 
    
    self.userText = self.txt.get() 

    self.txt_pt1 = '''
            <html>
                <body>
                    <h1>'''

    self.userText

    self.txt_pt3 ='''    </h1>
                </body>
            </html>'''
                    
    webContent = "{}\n {} {}".format(self.txt_pt1,self.userText,self.txt_pt3)


    # this inserts what the user's input where {} are. 
    f.write(webContent) # use the text variable as the parameter for the write function, this puts the code into the file. 
    f.close()
    
    # use webbrowser module to open html file in new page. 
    webbrowser.open_new_tab("SummerSale.html") # open the webpage. 











