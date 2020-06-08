
import os
from tkinter import *
import tkinter as tk
import sqlite3

#create a frame for the application
class ParentWindow(Frame):
    def __init__(self,master,*args,**kwargs):
        Frame.__init__(self,master, *args, **kwargs)

        # define our master frame configuration
        self.master = master
        self.master.title("Check Files")
        
        # call the function that paints the different elements of the gui
        load_gui(self)

#this creates the main gui
def load_gui(self):

    #Define the textbox for typing
    self.txt1 = tk.Entry(self.master,  width = 50)
    self.txt1.grid(row=0,column=2, padx=(10,10),pady=(30,10))


    self.lbl_type = tk.Label(self.master,width = 15, text='Type Text for Website')
    self.lbl_type.grid(row=0,column=0,padx=(10,0),pady=(30,10), sticky=W)
    self.btn_mkWebsite = tk.Button(self.master, width = 15, height=2,text='Create Website', command=lambda: mk_website(self))
    self.btn_mkWebsite.grid(row=2,column=0,padx=(10,0),pady=(10,10),sticky=W)
    self.btn_close = tk.Button(self.master, width = 15, height=2,text='Close Program',command=lambda: ask_quit(self))
    self.btn_close.grid(row=2,column=2,padx=(10,10),pady=(10,10),sticky=E)

def mk_website(self):
    content = self.txt1.get()
    print(content)
    
    f = open("summerwebsite.html", "w")
    f.write("<html>\n<body>\n {} \n</body>\n</html>".format(content))
    f.close()


def ask_quit(self):
    if tk.messagebox.askokcancel("Exit program", "Okay to exit application?"):
        this closes the app
        self.master.destroy()
        os._exit(0)


if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
