import datetime
import os
import glob
import shutil
#location="/media/Storage/PythonProgramming/Test"
#get the date for this day
#today=('{date:%Y%m%d}'.format( date=datetime.datetime.now()))
#create a new folder
#newpath = r'/media/Storage/PythonProgramming/Test/testfolder/'+today 
#if not os.path.exists(newpath):
#    os.makedirs(newpath)
#get yesterday date from file
#f = open("yesterday.txt", "r")   
#yesterday=f.read()
#print(yesterday)
#sort files in yesterday folder
#f.close()
olddates=["20200426","20200427","20200428"]
for x in olddates:
 newpath = r'/var/lib/motion/'+x
 if not os.path.exists(newpath):
  os.makedirs(newpath)

 for data in glob.glob("/var/lib/motion/"+x+"*"):
  if not os.path.isdir(data):
   shutil.move(data,"/var/lib/motion/"+x)

#write the new date for yesterday.txt  
#f = open("yesterday.txt", "w")  
#f.write(today)
#f.close()
