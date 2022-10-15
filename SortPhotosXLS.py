# Copies files from the list of filenames from a XLS file to the specified folder.

import os,sys,xlrd,string,glob,shutil
imageName = ""

source = "D:\\Photos\\Raw\\"    # Directory of RAW photos

destination = "D:\\Photos\\Toedit\\"   # Directory where sorted RAW photos need to be copied

file = "D:\\Photos\\sort.xls"       # Excel sheet containing names of the files

workbook = xlrd.open_workbook(file)
worksheet = workbook.sheet_by_name('Sheet1')  # Sheet name
num_rows = worksheet.nrows - 1
num_cells = worksheet.ncols - 1
curr_row = -1
i = 0
j=0
k=0
t = ""

while curr_row < num_rows:
    j=j+1
    curr_row += 1
    row = worksheet.row(curr_row)
    curr_cell = -1
    while curr_cell < num_cells:
        curr_cell += 1
        #Cell Types: 0=Empty, 1=Text, 2=Number, 3=Date, 4=Boolean, 5=Error, 6=Blank
        cell_type = worksheet.cell_type(curr_row, curr_cell)
        cell_value = worksheet.cell_value(curr_row, curr_cell)

        #print "Img ",cell_value
        
        imageSony = str(cell_value) + ".ARW"      #change the file extensions w.r.t your files
        imageNikon = str(cell_value) + ".NEF"
        imageCanon = str(cell_value) + ".CR3"
        imageJPG = str(cell_value) + ".JPG"
        imageJPGBW = str(cell_value) + "-2.JPG"
        imagePNG = str(cell_value) + ".PNG"
        
        #imageNikon = cell_value + ".JPG"
        #imageCanon = cell_value + ".JPG"
        
        sS = source + imageSony
        sN = source + imageNikon
        sC = source + imageCanon
        sJ = source + imageJPG
        sJBW = source + imageJPGBW
        sP = source + imagePNG
        
        if os.path.isfile(sS):
            t = destination + imageSony
            i = i + 1
            #print "sS ",sS
            if os.path.isfile(t):
                pass
            else:
                shutil.copyfile(sS,t)
            #shutil.move(sS,t)
        elif os.path.isfile(sN):
            t = destination + imageNikon
            i = i + 1
            #print "sN ",sN
            if os.path.isfile(t):
                pass
            else:
                shutil.copyfile(sN,t)
            #shutil.move(sN,t)
        elif os.path.isfile(sC):
            t = destination + imageCanon
            i = i + 1
            #print "sC ",sC
            if os.path.isfile(t):
                pass
            else:
                shutil.copyfile(sC,t)
            #shutil.move(sC,t)
        elif os.path.isfile(sJ):
            t = destination + imageJPG
            i = i + 1
            #print "sJ ",sJ
            if os.path.isfile(t):
                pass
            else:
                shutil.copyfile(sJ,t)
            #shutil.move(sJ,t)        
        elif os.path.isfile(sP):
            t = destination + imagePNG
            i = i + 1
            #print "sJ ",sJ
            if os.path.isfile(t):
                pass
            else:
                shutil.copyfile(sP,t)
            #shutil.move(sJ,t)        
        else:
            print ("Missing -> ",str(cell_value))
            k = k + 1

        if os.path.isfile(sJBW):
            t = destination + imageJPGBW
            i = i + 1
            #print "sJBW ",sJBW
            if os.path.isfile(t):
                pass
            else:
                shutil.copyfile(sJBW,t)
            #shutil.move(sJBW,t)
            
        #print (i)
            
                
print ('total-',j)                
print ('found-',i)
print ('not found-',k)