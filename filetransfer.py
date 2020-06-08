
import shutil
import time
import os

# set where the sources of the files are
source = '/Users/15095/Desktop/FolderB/'

#set the destination path to folder
destination = '/Users/15095/Desktop/FolderA/'
files = os.listdir(source)
print(files)


for i in time:
    print(i)
    time = os.path.getmtime(i) #NOTE: I think this is struggling with data types. 
    print(time)
##    if time > (datetime.hour()-24): #I'm guesssing this won't work, but the idea is trying to find somethign 24 hrs old or less.
##        shutil.move(source+i, destination)
