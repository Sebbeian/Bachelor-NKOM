# Convert script for 1809
# Version 1
# Author ebk-nkom
# ©NKOM 2021

# Import generic libs
import os
import numpy as np

# Import internal libs
from lib_1809 import file_handler_lib_1809 as fh


def convert_1809(filedir, folder_path_conv, new_d_points):
    
    # Read in data from file
    file_content = fh.read_file(filedir)
    header_var = fh.extract_header_info(file_content)
    measurement_times = fh.extract_measurement_time(file_content)
    measurement_coordinates = fh.extract_coordinates(header_var[0], file_content)
    measurement_data = fh.extract_measurement_data(header_var[0], file_content)

    # Read current header of 1809 
    header = file_content[0:16]

    # Compute data points to be removed
    data_points_to_remove = header_var[4] - new_d_points


    # Temp error ''handler''
    # check if datapoints below new points
    if header_var[4] < new_d_points:
        print("| Cannot upscale data   | : " + str(header_var[4]) + \
            " < " + str(new_d_points))

    # Convertion 1
    # Convert data points if necessary 
    if header_var[4] != new_d_points:

        #print("Converting data points, points to remove:   " + str(data_points_to_remove))

        # Index data to be removed with equal spacing 
        idx = np.round(np.linspace(0, len(measurement_data[1]) - 1, data_points_to_remove)).astype(int)
        
        # Removing datapoints
        measurement_data_converted_d_points = np.delete(measurement_data, idx, axis=1)

        # Filterbandwidth changes 
        freq_span = header_var[2] - header_var[1]
        new_rbw = freq_span / (new_d_points-1)
        header[7] = str(header[7]).replace(str(header_var[3]),str(new_rbw))

        # Add Convertion name to filetype for information
        header[0] = "FileType " + header_var[0] + " Converted " + "FilterBandwidthPrevious " + str(header_var[3]) \
            + " DataPointsPrevious " + str(header_var[4])

        # Change data points in to new header 
        header[10] = str(header[10]).replace(str(header_var[4]),str(new_d_points))

        # Store converted data points into the data array 
        # (This line is only for readability)
        measurement_data = measurement_data_converted_d_points

    
    # Convertion 2
    # Convert samplerate, allways do this when converting
        # Sample data down to 1s if posible
        # (NB does not check that every sec is exsisting but
        # stores all measurments within that sec to one measurment 
        # with MAX Hold of all those lines)

    # Allocate array for new data for one sample time (1,len(measurement_data))
    new_data = np.zeros((1, measurement_data.shape[1]), dtype= int)

    # Allocate array's
    all_idx_new = []
    new_measurement_times = []
    measurement_times_converted = []

    # Compute idx and len of one time xx:xx:xx (for instance 12.10.13)
    # then takes max hold of data within that second
    i = 0
    while i < len(measurement_times):
        current_time = measurement_times[i]
        current_idx = [i for i, x in enumerate(measurement_times) if x == current_time]
        i = i + len(current_idx)
        new_measurement_times.append(current_time)
        new_data_temp = np.max(measurement_data[current_idx[0]:current_idx[-1] + 1], axis=0)
        new_data = np.vstack((new_data, new_data_temp))
        if header_var[0].upper().find('MOBILEDATA') != -1:
            all_idx_new.append(current_idx[0]) 
        # to extract gps data in correct lines (takes first gps and not mean of all times)
    
    # Store new gps coordinates in time array 
    if header_var[0].upper().find('MOBILEDATA') != -1:
        measurements_coordinates_converted = np.array(measurement_coordinates)[all_idx_new]     
    else:
        measurements_coordinates_converted = "No Coordinates"
    #print(measurement_times_converted)
    # Remove first empty v.stack line from converted data
    new_data = new_data[1:]

    # Create new data converted data
    measurement_times_converted = new_measurement_times
    measurements_converted = new_data

    # Convertion of header here 
    new_note_15 = header[15]
    new_note_15 = new_note_15[0] + ', MaxHoldConverted: 1 second, ' + new_note_15[2]
    header[15] = new_note_15

    # We have now
    # Header
    # measurement_times_converted
    # measurements_coordinates_converted
    # array_measurements_converted

    # HAX FIX THIS 
    filename = filedir[34:-4]

    # Save 1809 .cef file in converted folder
    with open(os.path.join (folder_path_conv, filename + ".cef" ), 'w') as filehandle:
        for listitem in header:
            listitem = str(listitem).strip("[]")
            listitem = str(listitem).replace("' ","")
            listitem = str(listitem).replace("'","")
            filehandle.write('%s\n' % listitem)

        filehandle.write('%s\n' % "") # Add newline from header to measurements 

        i = 0
        for listitem in measurement_times_converted:
            temp = listitem
            filehandle.write('%s' % temp)
            filehandle.write('%s' % ",")
            if header_var[0].upper().find('MOBILEDATA') != -1:
                temp2 = measurements_coordinates_converted[i].tolist()
                temp2 = str(temp2).strip("[]")        # For Mobile Measurments
                temp2 = str(temp2).replace(" ","")    # For Mobile Measurments
                temp2 = str(temp2).replace("'","")    # For Mobile Measurments
                filehandle.write('%s' % temp2)
                filehandle.write('%s' % ",") 
            temp3 = measurements_converted[i].tolist()
            temp3 = str(temp3).strip("[]")
            temp3 = str(temp3).replace(" ","")
            filehandle.write('%s\n' % temp3)
            i += 1

    # Print out the convertion variables
    print('| Convertion Stats      | : Data points removed: ' + str(data_points_to_remove)  +\
             ',    Converterted total samples from:  ' + str(len(measurement_times)) + \
                ' to ' + str(len(measurement_times_converted)) + '   Convertion ration:  '\
                     + str(len(measurement_times)/len(measurement_times_converted)))
