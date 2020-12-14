import os

dirlist = os.listdir(os.getcwd())
for i in range(0,len(dirlist)):
    if(dirlist[i].find('.jpg') != -1):
        os.rename(dirlist[i], dirlist[i][0:dirlist[i].find('.jpg')]+'.png')
