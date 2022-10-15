# Writes list of files/ folders in a directory in a .txt file


import os,sys,string,glob,shutil

a = "D:\\Photos\\"

i = 0
k = 0


a = os.listdir(a)

myfile = open('D:\\DirectoryList.txt', 'w')
for _ in a:    
    myfile.write(_+"\n")
    
myfile.close()  
              
