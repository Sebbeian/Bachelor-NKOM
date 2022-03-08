# Test data for corruption
# Version 1
# Author ebk-nkom
# ©NKOM 2021


''' NB
Does only test data not header of file*, coordiantes or times
Large files will result in MEM allocation problem, depening on pc setup
'''

# Generic libraries
import csv
import glob
import os
import numpy as np

# nkom-ebk libraries 
from lib_1809 import file_handler_lib_1809 as fh


########### Interface ################

folder_path_files        = "D:\\VS_Code_Projects\\Data_v1\\Files\\"

########## End of Interface ###########

# Create global arrays 
filenames = [] 
error_file_list = []

# Make list of dir to all .cef files within the file folder
for root, dirs, files in os.walk(folder_path_files):
    for file in files:
        if(file.endswith(".cef")):
            filenames.append(os.path.join(root,file))

print("| Files to check | : " + str(len(filenames)))

# Main script run all files
file_processing = 0
for filedir in filenames: 
    filename = filedir[len(folder_path_files):-4]
    file_processing += 1   
    try:
        file_content = fh.read_file(filedir)
        header_var = fh.extract_header_info(file_content)
        measurement_data = fh.extract_measurement_data(header_var[0], file_content)

        print("File: " + str(file_processing) + "  Filename: " + filename + "   GOOD")
    
    except:
        print("File: " + str(file_processing) + "  Filename: " + filename + "   ERROR")
        measurement_data = []
        measurements = file_content[17:]
        
        i = 0
        if header_var[0].upper().find('MOBILEDATA') != -1:
            for row in measurements:
                del measurements[i][0]
                del measurements[i][0] 
                del measurements[i][0] 
                if len(row) != header_var[4]:
                    print("Error in row: " + str(i+19))
                i += 1
        else:
            for row in measurements:
                del measurements[i][0]
                #if len(row) != header_var[4]:
                #    print("Error in row: " + str(i+19))
                i += 1
            print(len(row))
        
        error_file_list.append(filename)
        
print(error_file_list)
#np.savetxt("list_of_1809_file_error.csv", error_file_list, delimiter =", ", fmt ='% s')       

