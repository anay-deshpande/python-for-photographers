# Renames files/ photos in a specific folder.


import os,sys,string,glob,shutil

i = 0
k = 0

sourceAl1 = "D:\\Photos\\"

destination = "D:\\Photos\\"

a = os.listdir(sourceAl1)

i=1

for _ in a:
    tkn = _.split('.',-1)
    tkn1 = _.split('.',-1)
    print (tkn)
    sN = sourceAl1 + tkn[0] + "." + tkn[1] 
    tN = destination + "Phot-" + str(i) + "." + tkn[1] 

    print ("SourceName: ", sN)
    print ("DestinationName: ", tN)
    
    os.rename(sN,tN)

    i+=1