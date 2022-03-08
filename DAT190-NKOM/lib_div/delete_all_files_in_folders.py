# Script to clean folders fast
# Version 1
# Author ebk-nkom
# ©NKOM 2021


import os, shutil

# Path to folders to be deleted 
folder_path_files           = "D:\\VS_Code_Projects\\Data_v1\\Files\\"
folder_path_conv            = "D:\\VS_Code_Projects\\Data_v1\\Files_Converted\\"
folder_path_files_error     = "D:\\VS_Code_Projects\\Data_v1\\Files_Error\\"
folder_path_files_moved     = "D:\\VS_Code_Projects\\Data_v1\\Files_Moved\\" 
folder_path_heat_map        = "D:\\VS_Code_Projects\\Data_v1\\Heat_Map\\"
folder_path_max_hold        = "D:\\VS_Code_Projects\\Data_v1\\Max_Hold\\" 
folder_path_jam_png         = "D:\\VS_Code_Projects\\Data_v1\\JAM_PNG\\"
folder_path_rfi_png         = "D:\\VS_Code_Projects\\Data_v1\\RFI_PNG\\" 

all_folders = [folder_path_files, folder_path_conv, folder_path_files_error, folder_path_files_moved,\
     folder_path_heat_map, folder_path_max_hold, folder_path_jam_png, folder_path_rfi_png]

for x in all_folders:
    dir = x
    for files in os.listdir(dir):
        print("| Removing files in | : " + x)
        path = os.path.join(dir, files)
        try:
            shutil.rmtree(path)
        except OSError:
            os.remove(path)
        