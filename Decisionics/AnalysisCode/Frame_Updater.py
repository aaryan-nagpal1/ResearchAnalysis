# Open the input file for reading
with open('11thFeb_12hr_pt6_Sensor2.txt', 'r') as input_file:
    # Read the lines from the input file
    lines = input_file.readlines()

# Open the output file for writing
with open('11thFeb_12hr_pt6_Sensor2-1.txt', 'w') as output_file:
    for line in lines:
        # Split the line into values using comma as the delimiter
        values = line.strip().split(', ')
        
        # Check if there are at least three values in the line
        if len(values) >= 3:
            # Convert the first value to an integer, add 421681, and convert it back to a string
            updated_first_value = str((int(((values[0]))) + 1313735))
            #updated_first_value = str(int(float((values[0])) + 511382))
            
            # Write the updated line to the output file
            updated_line = ', '.join([updated_first_value] + values[1:])
            output_file.write(updated_line + '\n')

print("Data has been updated and saved to 'updatedoutput.txt'.")
