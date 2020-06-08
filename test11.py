import datetime as dt
import time

 #establish a sense of time for the opartion
now = dt.datetime.now()
day = now-dt.timedelta(hours=24)

print(day)
##
##    # set where the sources of the files are
##    source = self.browse_src.get()
##
##    #set the destination path to folder
##    destination = self.browse_dst.get()
##
##    #list the files in source
##    files = os.listdir(source)
##
##
##    #iterate through the source files, add full path name, get modified time, compare that time to now, move if less than 24 hrs
##    for i in files:
##        path = os.path.join(source,i)
##        mtime = os.path.getmtime(path)
##        print(mtime)
##        print(day)
