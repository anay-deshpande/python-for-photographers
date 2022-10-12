import os,sys,xlrd,string,glob,shutil
imageName = ""

source = "D:\\Photos\\Raw\\"      # Folder containing the files

file = "D:\\Photos\\sort.xls"      # Excel sheet containing names of the files


workbook = xlrd.open_workbook(file)
worksheet = workbook.sheet_by_name('Sheet1')   # Sheet name
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
        cell_type = worksheet.cell_type(curr_row, curr_cell)
        cell_value = worksheet.cell_value(curr_row, curr_cell)

               
        imageJPG = str(cell_value) + ".png"   #change the file extension w.r.t your files
        
        sJ = source + imageJPG        

        if os.path.isfile(sJ):
            #print "sJ ",sJ
            os.remove(sJ)
            i = i + 1
            #shutil.move(sJ,t)
        else:
            print ("Missing ",imageJPG)
            pass

print ("Removed ",i)