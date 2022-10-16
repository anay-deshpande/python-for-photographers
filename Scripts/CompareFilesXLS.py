# Compares filenames from a XLS file and prints the list of the missing files/ photos.


import os,sys,xlrd,string,glob,shutil
imageName = ""

destination = "D:\\Photos\\Raw\\"  # Directory of photos
file = "D:\\Photos\\sort.xls"      # Excel sheet containing names of the files


workbook = xlrd.open_workbook(file)
worksheet = workbook.sheet_by_name('Sheet1')   # Sheet name
num_rows = worksheet.nrows - 1
num_cells = worksheet.ncols - 1
curr_row = -1
i = 0
j=0
k=0

while curr_row < num_rows:
    j=j+1
    curr_row += 1
    row = worksheet.row(curr_row)
    curr_cell = -1
    while curr_cell < num_cells:
        curr_cell += 1
        # Cell Types: 0=Empty, 1=Text, 2=Number, 3=Date, 4=Boolean, 5=Error, 6=Blank
        cell_type = worksheet.cell_type(curr_row, curr_cell)
        cell_value = worksheet.cell_value(curr_row, curr_cell)
        
        imageName = str(cell_value)+ ".png"        #change the file extension w.r.t your files
        t = destination + imageName
        if os.path.isfile(t):
            i = i + 1            
        else:
            k = k + 1
            print (imageName)
        #print (i)

print ("found-",i)
print ("not found-",k)