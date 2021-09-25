import os
import shutil

list=os.listdir("C:/Users/Srividya/Desktop/TEMP/dataFolder")
print(list)

def uploadPython(file):
    source="C:/Users/Srividya/Desktop/TEMP/dataFolder/"+file
    destination="C:/Users/Srividya/Desktop/TEMP/python commands/python1"
    shutil.move(source,destination)

def uploadtext(file):
    source="C:/Users/Srividya/Desktop/TEMP/dataFolder/"+file
    destination="C:/Users/Srividya/Desktop/TEMP/python commands/text"
    shutil.move(source,destination)


def uploadfolder(file):
    source="C:/Users/Srividya/Desktop/TEMP/dataFolder/"+file
    destination="C:/Users/Srividya/Desktop/TEMP/python commands/folders"
    shutil.move(source,destination)

for k in list:
    a=os.path.splitext(k)[1]
    if a==".py":
        uploadPython(k)
    elif a==".txt":
        uploadtext(k)
    else:
        uploadfolder(k)
    


