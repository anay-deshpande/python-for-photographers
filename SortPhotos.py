# Copies RAW photos of the sorted JPEG photos to another folder


import os,sys,string,glob,shutil
i = 0
k = 0
sort = "D:\\Photos\\sort\\"      # Directory of sorted JPEG photos

sourceAl1 = "D:\\Photos\\Raw\\"  # Directory of RAW photos

destination = "D:\\Photos\\Toedit\\"  # Directory where sorted RAW photos need to be copied

a = os.listdir(sort)

for _ in a:
    tkn = _.split('.',-1)
    #print tkn[0]
    sN = sourceAl1 + tkn[0] + ".NEF"
    tN = destination + tkn[0] + ".NEF"
    sC = sourceAl1 + tkn[0] + ".CR2"
    tC = destination + tkn[0] + ".CR2"      
    sCc = sourceAl1 + tkn[0] + ".CR3"
    tCc = destination + tkn[0] + ".CR3"
    sS = sourceAl1 + tkn[0] + ".ARW"
    tS = destination + tkn[0] + ".ARW"
    sJ = sourceAl1 + tkn[0] + ".JPG"
    tJ = destination + tkn[0] + ".JPG"

    
    if os.path.isfile(sN):
        i = i+1
        if os.path.isfile(tN):
            pass
        else:
            shutil.copyfile(sN,tN)
    elif os.path.isfile(sC):
        i = i+1
        if os.path.isfile(tC):
            pass
        else:
            shutil.copyfile(sC,tC)
    elif os.path.isfile(sCc):
        i = i+1
        if os.path.isfile(tCc):
            pass
        else:
            shutil.copyfile(sCc,tCc)
    elif os.path.isfile(sS):
        i = i+1
        if os.path.isfile(tS):
            pass
        else:
            shutil.copyfile(sS,tS)
    elif os.path.isfile(sJ):
        i = i+1
        if os.path.isfile(tJ):
            pass
        else:
            shutil.copyfile(sJ,tJ)
    else:
        k = k + 1
        print (_, "NOT FOUND")
            
print (i," Copied")
print (k," Not Found")

