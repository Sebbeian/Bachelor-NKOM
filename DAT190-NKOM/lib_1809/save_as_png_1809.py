# 1809 SAVE 1809 TO PNG
# Version 1
# Author ebk-nkom
# ©NKOM 2021

# Import generic libs
import numpy as np
import matplotlib.pyplot as plt

# Import internal libs
from lib_1809 import file_handler_lib_1809 as fh

def save_1809_png(max_hold, heat_map, filename, filedir, folder_path_heat_map, folder_path_max_hold):
    # Read in data from file
    file_content = fh.read_file(filedir)
    header_var = fh.extract_header_info(file_content)
    measurement_data = fh.extract_measurement_data(header_var[0], file_content)

    # Read current header of 1809 
    header = file_content[0:16]

    if heat_map == True:
        plt.ioff() # Turn off plot
        figure = plt.figure()
        axes3 = figure.add_subplot(111)
        axes3.axis('off')

        a = axes3.imshow(measurement_data, interpolation=None, aspect='auto', cmap='rainbow') 
        plt.colorbar(a, ax=axes3)
        plt.savefig(folder_path_heat_map + filename + " test " + ".png", bbox_inches='tight', dpi = 250)      
        plt.close('all')

    if max_hold == True:
        # Compute absolute max for every freq to scale plot axsis
        measurement_data_max = measurement_data.max(axis=0)
        measurement_data_max = measurement_data_max.reshape(len(measurement_data_max),1)     
        
        # Create freq axis for plot
        freq = np.linspace(start=header_var[1], stop=header_var[2], num=header_var[4], dtype=int)
        
        plt.ioff() # Turn off plot
        figure = plt.figure()
        axes1 = figure.add_subplot(111)
        axes1.plot(freq, measurement_data_max, 'b', linewidth=.4)
        axes1.set_ylim([min(measurement_data_max)-5, max(measurement_data_max)+20])
        plt.savefig(folder_path_max_hold + filename + ".png", bbox_inches='tight', dpi=250)
        plt.close('all')