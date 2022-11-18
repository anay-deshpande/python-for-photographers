# Python-for-Photographers
This is a repository for python scripts which can be used to sort photos, list folder contents, delete files, compare files and also can take reference from a XLS file to perform the functions. It majorly helps photographers to automate their daily tasks & save resources.

## Scripts
- CompareFiles.py
  - Compares 2 folders and outputs the list of missing files from one folder which are present in the other.

- CompareFilesXLS.py
  - Compares filenames from an excel sheet and checks if the file exits in the foloder, outputs the missing file names

- DirectoryList.py
  - Outputs the list of files/folders in the specified directory.

- RemoveFilesXLS.py
  - Removes files which are mentioned in the Excel sheet.

- RenameFiles.py
  - Renames files in a folder with specific name and number iterating.  

- SortPhotos.py
  - Will check for RAW photos in a folder with reference to JPEG photos in another folder and then copy RAW versions of the JPEG photos in the third folder and output number of missing photos and their names.

- SortPhotosXLS.py
  - Will check for photos in a folder with reference to Excel sheet and then copy the photos in another folder and output number of missing photos and their names.



## Dependencies

`xlrd` - pip3 install xlrd

## Running the Script

- Download/Clone this Repo into desired folder.
- Install the requirements.
- Change the file location for the photographs in the script.
- Change file extension (if needed, mentioned in the script details) 
- Open up your terminal/ IDE/ Compiler. 
- Run the script.