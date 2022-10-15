# Compares files/ photos from 2 folders and prints the list of the missing files/ photos.


import os,sys,string,glob,shutil

i = 0
s = "D:\\Photos_1\\"
d = "D:\\Photos_2\\"

a = os.listdir(s)
  
for each in a:
    s1 = d + each
    if os.path.isfile(s1)!=1:
        i = i+1
        print (each)
    '''
    else:
        print ("exists : ",each)
    '''
print (i)
