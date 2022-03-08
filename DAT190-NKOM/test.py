# Temp Script for finding files
# Version 1
# Author ebk-nkom
# ©NKOM 2021

# Import generic libs
import os
import shutil

# Import internal libs
from lib_1809 import convert_1809 as conv

########### Interface ################

# Path to folders
folder_path_files        = "D:\\VS_Code_Projects\\Data_v1\\Files\\"
folder_path_conv         = "D:\\VS_Code_Projects\\Data_v1\\Files_Converted\\"
########## End of Interface ###########

# Create global arrays 
filenames =  [] 
filenames2 = []
file_list =  []
file_list2 =  []

# Make list of dir to all .cef files within the file folder
for root, dirs, files in os.walk(folder_path_files):
    for file in files:
        if(file.endswith(".cef")):
            filenames.append(os.path.join(root,file))


file_processing = 0
for filedir in filenames: 
        filename = filedir[len(folder_path_files):-4]
        file_processing += 1   
        file_list.append(filename)

# Make list of dir to all .cef files within the conv folder
for root, dirs, files in os.walk(folder_path_conv):
    for file in files:
        if(file.endswith(".cef")):
            filenames2.append(os.path.join(root,file))

file_processing = 0
for filedir2 in filenames2: 
        filename2 = filedir2[len(folder_path_conv):-4]
        file_processing += 1   
        file_list2.append(filename2)


print("Number of files  :   " + str(len(file_list)))
print("Number of files2 :   " + str(len(file_list2)))

diff = len(file_list2) - len(file_list)
print(str(diff))

# res = files that are not in file filder    
res = list(set(file_list)^set(file_list2))
print(str(len(res)))
print(res[0])
i = 0
for x in res:
    try:
        print(res[i]) 
        i += 1
        shutil.move(folder_path_conv + res[i] + ".cef", "D:\\VS_Code_Projects\\Data_v1\\Files_Error\\")
    except:
        print("error")