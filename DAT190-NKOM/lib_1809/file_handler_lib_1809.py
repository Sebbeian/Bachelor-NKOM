# 1809 file handler 
# Version 1
# Author ebk-nkom
# ©NKOM 2021

# Note that datapoints are stored as int not float for the future

import csv
import math
import timeit

#from tqdm import tqdm
import numpy as np



def read_file(filedir):
    file_content = [] 
    with open(filedir, 'r') as file:
        reader = csv.reader(file, dialect='excel', delimiter=',')
        for row in reader:
            file_content.append(row)
    return file_content


def extract_header_info(file_content):
    header_var = []

    # Extract measurement information
    file_type = file_content[0]
    freq_start = file_content[4]
    freq_stop = file_content[5]
    rbw = file_content[7]
    data_points = file_content[10]
    scan_time = file_content[11]

    # Remove extra array elements from measurement information
    file_type = ''.join([str(elem) for elem in file_type])
    freq_start = ''.join([str(elem) for elem in freq_start])
    freq_stop = ''.join([str(elem) for elem in freq_stop])
    rbw = ''.join([str(elem) for elem in rbw])
    data_points = ''.join([str(elem) for elem in data_points])
    scan_time = ''.join([str(elem) for elem in scan_time])

    # Extract measurement variables
    file_type = file_type[9:]
    freq_start = freq_start[10:]
    freq_stop = freq_stop[9:]
    rbw = rbw[16:]
    data_points = data_points[11:]
    scan_time = scan_time[9:]

    # Convert measurement variables to numbers
    freq_start = int(freq_start)
    freq_stop = int(freq_stop)
    rbw = float(rbw)
    data_points = int(data_points)
    scan_time = float(scan_time)

    header_var = [file_type, freq_start, freq_stop, rbw, data_points, scan_time]

    return header_var


def extract_measurement_time(file_content):
    measurement_times = []
    measurements = file_content[17:]
    
    i = 0 
    for row in measurements:
        temp = measurements[i][0]
        measurement_times.append(temp)
        i += 1
  
    return measurement_times

def extract_coordinates(file_type, file_content):
    measurement_coordinates = []
    measurements = file_content[17:]
       
    i = 0
    if file_type.upper().find('MOBILEDATA') != -1:
        for row in measurements:
            temp = measurements[i][1:3]
            measurement_coordinates.append(temp)
            i += 1
        measurement_coordinates = np.array(measurement_coordinates) 
    else:
        measurement_coordinates = 'No coordinates to show'
    
    return measurement_coordinates

def extract_measurement_data(file_type, file_content):
    measurement_data = []
    measurements = file_content[17:]
    
    i = 0
    if file_type.upper().find('MOBILEDATA') != -1:
        for row in measurements:
            del measurements[i][0]
            del measurements[i][0] 
            del measurements[i][0] 
            i += 1
    else:
        for row in measurements:
            del measurements[i][0]
            i += 1
    
    measurement_data = np.asarray(measurements, dtype= int)

    return measurement_data
