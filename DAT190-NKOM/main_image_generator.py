# Main script for generation of images from 1809 files
# Version 1
# Author ebk-nkom
# ©NKOM 2021

# Import generic libs
import os

# Import internal libs
from lib_1809 import save_as_png_1809 as save_png

########### Interface ################
# Set as False for exluding computation
max_hold                = True
heat_map                = True

# Path to folders
folder_path_files        = "D:\\VS_Code_Projects\\Data_v1\\Files\\"
folder_path_heat_map     = "D:\\VS_Code_Projects\\Data_v1\\Heat_Map\\"
folder_path_max_hold     = "D:\\VS_Code_Projects\\Data_v1\\Max_Hold\\" 

########## End of Interface ###########

# Create global arrays 
filenames = [] 
error_file_list = []

# Make list of dir to all .cef files within the file folder
for root, dirs, files in os.walk(folder_path_files):
    for file in files:
        if(file.endswith(".cef")):
            filenames.append(os.path.join(root,file))

print("| Total files to generate (PNG) | : " + str(len(filenames)))

# Main script run all files
file_processing = 0
for filedir in filenames: 
    filename = filedir[len(folder_path_files):-4]
    file_processing += 1   
    try:
        print("| PNG generation of file | : " + str(file_processing) + " of " + str(len(filenames)) + "   File: " + filedir)
        save_png.save_1809_png(max_hold, heat_map, filename, \
         filedir, folder_path_heat_map, folder_path_max_hold)
    except:
        error_file_list.append(filename)
        print("| PNG not generated    | : " + str(filename))

print("------------------------")     
print("|PNG generation completed|")
print("------------------------")
print("|Files with error       | : " + str(error_file_list))
print("------------------------")
