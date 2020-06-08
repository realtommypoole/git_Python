
import shutil
import time
import datetime as dt
import os
from tkinter import *
import tkinter as tk
from tkinter import filedialog


class ParentWindow(Frame):
    def __init__(self,master,*args,**kwargs):
        Frame.__init__(self,master, *args, **kwargs)

        # define our master frame configuration
        self.master = master
        self.master.title("Check Files")
        
        load_gui(self)

def load_gui(self):

    #Define the listbox with a scrollbar and grid them
    self.browse_src = Entry(self.master, width = 50)
    self.browse_src.grid(row=0,column=2, padx=(10,10),pady=(30,10))
    self.browse_dst = Entry(self.master, width = 50)
    self.browse_dst.grid(row=1,column=2, padx=(10,10),pady=(30,10))


    self.btn_browse = tk.Button(self.master,width = 15, text='Browse Source...',command=lambda: f_src(self))
    self.btn_browse.grid(row=0,column=0,padx=(10,0),pady=(30,10), sticky=W)
    self.btn_browse = tk.Button(self.master,width = 15, text='Browse Destination...',command=lambda: f_dst(self))
    self.btn_browse.grid(row=1,column=0,padx=(10,0),pady=(30,10), sticky=W)
    self.btn_mvFiles = tk.Button(self.master, width = 15, height=2,text='Move files...', command=lambda: f_move(self))
    self.btn_mvFiles.grid(row=2,column=0,padx=(10,0),pady=(10,10),sticky=W)
    self.btn_close = tk.Button(self.master, width = 15, height=2,text='Close Program')
    self.btn_close.grid(row=2,column=2,padx=(10,10),pady=(10,10),sticky=E)


def f_src(self):
    src = tk.filedialog.askdirectory()
    print(str(src))
    self.browse_src.insert(END, str(src) + "/")

def f_dst(self):
    dst = tk.filedialog.askdirectory()
    print(str(dst))
    self.browse_dst.insert(END, str(dst) + "/")
        

def f_move(self): 
    #establish a sense of time for the opartion
##    now = dt.datetime.now()
##    day = now-dt.timedelta(hours=24)
    

    # set where the sources of the files are
    source = self.browse_src.get()

    #set the destination path to folder
    destination = self.browse_dst.get()

    #list the files in source
    files = os.listdir(source)


    #iterate through the source files, add full path name, get modified time, compare that time to now, move if less than 24 hrs
    for i in files:
        path = os.path.join(source,i)
        print(path)
        mtime = os.path.getmtime(path)
        age = time.time()- mtime
        if age < 86400:
            shutil.move(source+i, destination)
            print('Files have moved!')

        
if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
