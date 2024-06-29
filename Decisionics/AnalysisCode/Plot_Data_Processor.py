# import re

# # Specify the input file path
# input_file_path = "FSocket_Calibration_30Nov.csv"

# # Initialize an empty list for entries
# entries = []

# # Read the content of the input file
# with open(input_file_path, "r") as input_file:
#     lines = input_file.readlines()

# # Initialize variables for the current entry
# current_entry = ""
# in_entry = False

# # Process the lines and create entries
# for line in lines:
#     if "Frame" in line and "Raw Sum=,," in line:
#         # Start of a new entry
#         if in_entry:
#             entries.append(current_entry.strip())
#             current_entry = ""
#         in_entry = True
    
#     # Add the line to the current entry
#     current_entry += line

# # Add the last entry
# if in_entry:
#     entries.append(current_entry.strip())

# # Initialize lists to store extracted values
# frame_numbers = []
# raw_sums = []
# single_max_values = []

# # Process each block of text
# for entry in entries:
#     # Split the entry into lines
#     lines = entry.strip().split('\n')

#     # Extract frame number and raw sum from the first line
#     first_line = lines[0]
#     frame_match = re.search(r"Frame (\d+).*Raw Sum=,,(\d+)", first_line)
#     if frame_match:
#         frame_number = frame_match.group(1)
#         raw_sum = frame_match.group(2)
#         frame_numbers.append(frame_number)
#         raw_sums.append(raw_sum)

#     # Convert the next 16 lines into a list of lists and find the single max value
#     count=0
#     data_lines = lines[1:]
#     int_data = [[int(value) for value in line.split(',')] for line in data_lines]
#     max_value = max(max(int_data, key=lambda x: max(x)))
#     single_max_values.append(max_value)

# # Write the extracted values to the output file in the format "frame, single max value, raw sum"
# with open("FSocket_Calibration_30Nov.csv", "w") as output_file:
#     for i in range(len(frame_numbers)):
#         output_file.write(f"{frame_numbers[i]}, {single_max_values[i]}, {raw_sums[i]}\n")

# print("Extracted values saved to 'caloutput.txt'.")



import re

# Specify the input file path
input_file_path = "2024_06_28 1-hr 45 ml 14-15.csv"
# Initialize an empty list for entries
entries = []

# Read the content of the input file
with open(input_file_path, "r") as input_file:
    lines = input_file.readlines()

# Initialize variables for the current entry
current_entry = ""
in_entry = False

# Process the lines and create entries
for line in lines:
    if "Frame" in line and "Raw Sum=,," in line:
        # Start of a new entry
        if in_entry:
            entries.append(current_entry.strip())
            current_entry = ""
        in_entry = True
    
    # Add the line to the current entry
    current_entry += line

# Add the last entry
if in_entry:
    entries.append(current_entry.strip())

# Initialize lists to store extracted values
frame_numbers = []
raw_sums = []
single_max_values = []
greater_than_0 = []

# Process each block of text
for entry in entries:
    # Split the entry into lines
    lines = entry.strip().split('\n')

    # Extract frame number and raw sum from the first line
    first_line = lines[0]
    frame_match = re.search(r"Frame (\d+).*Raw Sum=,,(\d+)", first_line)
    if frame_match:
        frame_number = frame_match.group(1)
        raw_sum = frame_match.group(2)
        frame_numbers.append(frame_number)
        raw_sums.append(raw_sum)

    # Convert the next 16 lines into a list of lists and find the single max value
    count=0
    data_lines = lines[1:]
    int_data = [[int(value) for value in line.split(',')] for line in data_lines]
    max_value = max(max(int_data, key=lambda x: max(x)))
    single_max_values.append(max_value)
    for i in range(0,len(int_data)):
        for j in range(0,6):
            if int_data[i][j]>0:
                count+=1
            else:
                count+=0
    greater_than_0.append(count)

# Write the extracted values to the output file in the format "frame, single max value, raw sum"
with open("2024_06_28 1-hr 45 ml 14-15.txt", "w") as output_file:
    for i in range(len(frame_numbers)):
        output_file.write(f"{frame_numbers[i]}, {single_max_values[i]}, {raw_sums[i]}, {greater_than_0[i]}\n")

print("Extracted values saved to '16thfeb_2hour_2.txt'.")
