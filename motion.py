import datetime
import os
import glob
import shutil
location="/media/Storage/PythonProgramming/Test"
#get the date for this day
today=('{date:%Y%m%d}'.format( date=datetime.datetime.now()))
#create a new folder
newpath = r'/media/Storage/PythonProgramming/Test/testfolder/'+today 
if not os.path.exists(newpath):
    os.makedirs(newpath)
#get yesterday date from file
f = open("yesterday.txt", "r")   
yesterday=f.read()
print(yesterday)
#sort files in yesterday folder
f.close()

for data in glob.glob("/media/Storage/PythonProgramming/Test/"+yesterday+"*"):
    if not os.path.isdir(data):
        shutil.move(data,"/media/Storage/PythonProgramming/Test/testfolder/"+yesterday)

#write the new date for yesterday.txt  
f = open("yesterday.txt", "w")  
f.write(today)
f.close()
