# Main script for 1809 convertion
# Version 1
# Author ebk-nkom
# ©NKOM 2021

# Import generic libs
import os

# Import internal libs
from lib_1809 import convert_1809 as conv

########### Interface ################

# New number of data points
new_d_points = 8001
# Allways converting to 1s sample time currently

# Path to folders
folder_path_files        = "D:\\VS_Code_Projects\\Data_v1\\Files\\"
folder_path_conv         = "D:\\VS_Code_Projects\\Data_v1\\Files_Converted\\"

########## End of Interface ###########

# Create global arrays 
filenames = [] 
error_file_list = []

# Make list of dir to all .cef files within the file folder
for root, dirs, files in os.walk(folder_path_files):
    for file in files:
        if(file.endswith(".cef")):
            filenames.append(os.path.join(root,file))

print("| Files to be converted | : " + str(len(filenames)))

# Main script run all files
file_processing = 0
for filedir in filenames: 
    filename = filedir[len(folder_path_files):-4]
    file_processing += 1   
    try:
        print("| Converting file       | : " + str(file_processing) + " of " + str(len(filenames)) + "   File: " + filedir)
        conv.convert_1809(filedir, folder_path_conv, new_d_points)

    except:
        error_file_list.append(filename)
        print("| File not converted    | : " + str(filename))
        
    print("-------------------------")

print("|Convertion Completed|")
print("------------------------")
print("|Files with error       | : " + str(error_file_list))
print("------------------------")
