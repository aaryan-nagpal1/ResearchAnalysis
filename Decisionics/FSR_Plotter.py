# import matplotlib.pyplot as plt

# # Initialize empty lists to store data
# time_ms = []
# max_Pressure_kPa = []

# # Open and read the data from the file
# with open('21stSep_24hour_FSR_Data.txt', 'r') as file:
#     for line in file:
#         # Split each line by comma to separate the values
#         values = line.strip().split(', ')
        
#         # Ensure there are at least three values on each line
#         if len(values) >= 3:
#             time_ms.append(int(values[0])-1017923)  # Convert to int if needed
#             max_Pressure_kPa.append(float(values[2])/0.14762665892464999)  # Convert to float if needed

# # Create the plot
# plt.figure(figsize=(10, 6))
# plt.plot(time_ms, max_Pressure_kPa)
# plt.title('24 Hour FSR Readings')
# plt.xlabel('Time in ms')
# plt.ylabel('Maximum Pressure Value in kPa')
# plt.grid(True)

# # Show the plot or save it to a file
# plt.show()

import matplotlib.pyplot as plt
from matplotlib import rcParams
from matplotlib.ticker import MultipleLocator, FormatStrFormatter
import scipy
import numpy as np

rcParams['font.weight'] = 'bold'

# Initialize empty lists to store data from the first file
time_ms_1 = []
max_pressure_kPa_1 = []
avg_pressure_kPa_1 = []
volume_1 = []

# Read and store data from the first file
with open('8thfeb_test3_2min_output2.txt', 'r') as file:
    for line in file:
        values = line.strip().split(', ')
        if len(values) >= 2:
            time_ms_1.append(float(values[0])/(1000))
            avg_pressure_kPa_1.append(float(values[1]))
            max_pressure_kPa_1.append(float(values[2]))
            volume_1.append(float(values[3]))
            
# Initialize empty lists to store data from the first file
time_ms_2 = []
max_pressure_kPa_2 = []
avg_pressure_kPa_2 = []
volume_2 = []

# Read and store data from the first file
with open('18thMar_1hr_Sensor01-2.txt', 'r') as file:
    for line in file:
        values = line.strip().split(', ')
        if len(values) >= 2:
            time_ms_2.append(float(values[0])/(1000*60))
            avg_pressure_kPa_2.append(float(values[1]))
            max_pressure_kPa_2.append(float(values[2]))
            volume_2.append(float(values[3]))
            
# Initialize empty lists to store data from the first file
time_ms_3 = []
max_pressure_kPa_3 = []
avg_pressure_kPa_3 = []
volume_3 = []

# Read and store data from the first file
with open('11thFeb_12hour_pt1_outputtemp2.txt', 'r') as file:
    for line in file:
        values = line.strip().split(', ')
        if len(values) >= 2:
            time_ms_3.append(float(values[0])/(1000*60*60))
            avg_pressure_kPa_3.append(float(values[1]))
            max_pressure_kPa_3.append(float(values[2]))
            volume_3.append(float(values[3]))
            
#Initialize empty lists to store data from the second file
# time_ms_2 = []
# max_pressure_kPa_2 = []

# # Read and store data from the second file
# with open('NewFSR_2hr.txt', 'r') as file:
#     for line in file:
#         values = line.strip().split(', ')
#         if len(values) >= 2:
#             time_ms_2.append(float(values[0])/(1000*60*60))
#             max_pressure_kPa_2.append(float(values[1]))

# Create the plot
majorLocator = MultipleLocator(5)
majorFormatter = FormatStrFormatter('%d')
#plt.figure(figsize=(10,6))
fig, ax = plt.subplots(figsize=(10, 6))

#from scipy.interpolate import make_interp_spline
 
#X_Y_Spline1 = make_interp_spline(time_ms_1, max_pressure_kPa_1)
#X_Y_Spline2 = make_interp_spline(time_ms_1, avg_pressure_kPa_1)
#X_Y_Spline3 = make_interp_spline(time_ms_2, max_pressure_kPa_2)

# Returns evenly spaced numbers
# over a specified interval.
#X_1 = np.linspace(min(time_ms_1), max(time_ms_1), 1000)
#X_2 = np.linspace(min(time_ms_1), max(time_ms_1), 1000)
#Y_1 = X_Y_Spline1(X_1)
#Y_2 = X_Y_Spline2(X_1)
#Y_3 = X_Y_Spline3(X_2)
#plt.plot(X_1, Y_1, label='F-Socket Max Readings')
#plt.plot(X_1, Y_2, label='F-Socket Average Readings')
#plt.plot(X_2, Y_3, label='FSR Readings')
#plt.plot(time_ms_3, max_pressure_kPa_3, label='F-Socket Max Readings')
#plt.plot(volume_1, avg_pressure_kPa_1, label='F-Socket Average Readings - 2 Minute')
#plt.plot(volume_2, avg_pressure_kPa_2, label='F-Socket Average Readings - 2 Hour')
#plt.plot(volume_3, avg_pressure_kPa_3, label='F-Socket Average Readings - 24 Hour')
plt.plot(volume_1, max_pressure_kPa_1, label='F-Socket Max Readings - 2 Minute')
plt.plot(volume_2, max_pressure_kPa_2, label='F-Socket Max Readings - 2 Hour')
plt.plot(volume_3, max_pressure_kPa_3, label='F-Socket Max Readings - 24 Hour')
#plt.plot(time_ms_3, avg_pressure_kPa_3, label='F-Socket Average Readings')
ax.yaxis.set_major_locator(majorLocator)
ax.yaxis.set_major_formatter(majorFormatter)
plt.ylim(0, 130)
plt.xlim(0, 32.5)
plt.title('Max Pressure vs Volume', fontweight="bold")
plt.xlabel('Volume (in ml)', weight='bold')
plt.ylabel('Pressure Value (kPa)', weight="bold")
plt.legend()
plt.grid(True)

# Show the plot
plt.show()


# #Read the data from the file and store it in a list
# with open('24FSR.txt', 'r') as file:
#     lines = file.readlines()

# # Modify the data by changing the first value
# new_lines = []
# for line in lines:
#     parts = line.strip().split(',')
#     if len(parts) >= 2:
#         value1 = float(parts[0])
#         modified_value1 = value1 * (1000 / 18)
#         new_line = f'{modified_value1:.2f}\t{parts[1]}\n'  # Format and create the new line
#         new_lines.append(new_line)

# # Write the modified data back to the same file
# with open('24FSR.txt', 'w') as file:
#     file.writelines(new_lines)

#print("Data has been updated and saved to 'test_data.txt'.")


# #Read the data from the file and store it in a list
# with open('19thSep_1hour_FSR_Data.txt', 'r') as file:
#     lines = file.readlines()

# # Modify the data by subtracting 1017923 from the first value
# new_lines = []
# for line in lines:
#     parts = line.strip().split(', ')
#     if len(parts) >= 4:
#         value1 = int(parts[0])
#         modified_value1 = value1
#         new_line = f'{modified_value1}, {parts[2]}\n'  # Create the new line
#         new_lines.append(new_line)

# # Write the modified data back to the same file
# with open('19thSep_1hour_FSR_Data.txt', 'w') as file:
#     file.writelines(new_lines)

# print("Data has been updated and saved to '21stSep_24hour_FSR_Data.txt'.")

# #Read the data from the file and store it in a list
# import math
# #with open('19thSep_1hour_FSR_Data.txt', 'r') as file:
# with open('24FSR.txt', 'r') as file:
#     lines = file.readlines()

# #Modify the data by dividing the second value
# new_lines = []
# for line in lines:
#     values = line.strip().split(', ')
#     if len(values) >= 2:
#         value1 = int(values[0])
#         value2 = float(values[2])
#         modified_value2 = value2
#         new_line = f'{value1}, {modified_value2:.4f}\n'  # Create the new line
#         new_lines.append(new_line)

# # Write the modified data back to the same file
# with open('24FSR.txt', 'w') as file:
#     file.writelines(new_lines)

# print("Data has been updated and saved to '2hrFSR.txt'.")


# import re

# # Specify the file path
# file_path = "FSocket_Calibration_30Nov.csv"

# # Read the block of text from the file
# with open(file_path, "r") as file:
#     block_of_text = file.read()

# # Split the text into individual lines
# lines = block_of_text.split('\n')

# # Remove trailing ",,," from each line
# cleaned_lines = [re.sub(r',,,\s*$', '', line) for line in lines]

# # Replace lines with only commas with empty lines
# cleaned_lines = ['' if re.match(r'^\s*,*\s*$', line) else line for line in cleaned_lines]

# # Join the cleaned lines back into a single block
# cleaned_block = '\n'.join(cleaned_lines)

# # If you want to save the result back to the file
# with open("FSocket_Calibration_30Nov.csv", "w") as output_file:
#     output_file.write(cleaned_block)

