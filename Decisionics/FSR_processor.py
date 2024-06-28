#Read the data from the file and store it in a list
import math
with open('2024_06_26 1 - min 45 ml 14-15 no drop.txt', 'r') as file:
#with open('Fsocket_24hr_withentries.txt', 'r') as file:
    lines = file.readlines()

#Modify the data by dividing the second value
new_lines = []
for line in lines:
    values = line.strip().split(', ')
    #values = line.strip().split('\t')
    if len(values) >= 2:
        value1 = float(values[0])*(1000/8)
        value2 = float(values[1])
        value3 = float(values[2])
        value4 = float(values[3])
        modified_value3 = value3/value4
        new_line = f'{value1:.4f}, {modified_value3:.4f}, {value2:.4f}\n'  # Create the new line
        #new_line = f'{value1:.4f}, {value2:.4f}, {value3:.4f}, {value4:.4f}\n'  # Create the new line
        #new_line = f'{value1:.4f}, {modified_value3:.4f}\n'  # Create the new line
        #new_line = f'{value1:.4f}, {value2:.4f}\n'  # Create the new line
        new_lines.append(new_line)

# Write the modified data back to the same file
with open('update_2024_06_26 1 - min 45 ml 14-15 no drop.txt', 'w') as file:
    file.writelines(new_lines)

print("Data has been updated and saved to '8thfeb_test3_2min_output.txt'.")


# #Read the data from the file and store it in a list
# import math
# #with open('19thSep_1hour_FSR_Data.txt', 'r') as file:
# with open('24FSR.txt', 'r') as file:
#     lines = file.readlines()

# #Modify the data by dividing the second value
# new_lines = []
# for line in lines:
#     values = line.strip().split(', ')
#     #values = line.strip().split('\t')
#     if len(values) >= 2:
#         value1 = float(values[0])
#         value2 = float(values[2])*(5/9.07)
#         #value3 = float(values[2])
#         modified_value2 = math.e**((value2-2.3364)/0.7505)
#         #new_line = f'{value1:.4f}, {modified_value2:.4f}, {value3:.4f}\n'  # Create the new line
#         new_line = f'{value1:.4f}, {modified_value2:.4f}\n'  # Create the new line
#         new_lines.append(new_line)

# # Write the modified data back to the same file
# with open('NewFSR.txt', 'w') as file:
#     file.writelines(new_lines)

# print("Data has been updated and saved to '2hrFSR.txt'.")