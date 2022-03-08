# script for changing name of 1809 file
# Version 1
# Author ebk-nkom
# ©NKOM 2021

import glob, os
import shutil

filenames = [] 

# Change name of these
file_path_1809 = "D:\\VS_Code_Projects\\Data_v1\\Files\\*.cef"

for files in glob.glob(file_path_1809):
    filenames.append(files)

i = 1
for filename in filenames:
    filename_new = filename.replace('HaukenROS', 'ROS')
    os.rename(filename, filename_new)
    i += 1