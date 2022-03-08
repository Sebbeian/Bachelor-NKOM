# TEMP Script for moving JAM labeled data from Files to Files_Moved
# Using labeled data in JAM_PNG
# Version 1
# Author ebk-nkom
# ©NKOM 2021

import glob, os
import shutil

filenames = [] 

# Copies png file names in this folder
file_path_png = "D:\\VS_Code_Projects\\Data_v1\\JAM_PNG\\*.png"
file_path_len = len(file_path_png) - 5

# Moves files from this folder
file_path_1809 = "D:\\VS_Code_Projects\\Data_v1\\Files\\"

# To this folder
file_path_TEMP = "D:\\VS_Code_Projects\\Data_v1\\Files_Moved\\"

for files in glob.glob(file_path_png):
    filenames.append(files)

i = 1
for filename in filenames:
    filename_current = []
    filename_current = file_path_1809 + filename[file_path_len:-4] + ".cef"
    print("-------------- | Starting to move file | ------------")
    shutil.move(filename_current, file_path_TEMP)
    print("|    Moved File:    |  " + str(i) + "   " + file_path_1809 + filename[file_path_len:-4])
    i += 1
