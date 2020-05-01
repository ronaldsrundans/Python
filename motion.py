
import datetime
import os
import glob
import shutil
#location="/media/Storage/PythonProgramming/Test"
#get the date for this day
today=('{date:%Y%m%d}'.format( date=datetime.datetime.now()))
#create a new folder
newpath = r'/var/lib/motion/'+today 
if not os.path.exists(newpath):
    os.makedirs(newpath)
#get yesterday date from file
f = open("/media/PythonProgramming/yesterday.txt", "r")   
yesterday=f.read()
#print(yesterday)
#sort files in yesterday folder
f.close()

for data in glob.glob("/var/lib/motion/"+yesterday+"*"):
    if not os.path.isdir(data):
        shutil.move(data,"/var/lib/motion/"+yesterday)

#write the new date for yesterday.txt  
f = open("yesterday.txt", "w")  
f.write(today)
f.close()
