# Open the file for reading
with open('zupdate_2024_07_22 7-hour 45 ml_b2.txt', 'r') as file:
    # Read each line from the file
    lines = file.readlines()

# Open the file for writing
with open('zupdate_2024_07_22 7-hour 45 ml_b2.txt', 'w') as file:
    # # Iterate over each line
    # for line in lines:
        
    #     # Strip any leading/trailing whitespace and append 0.0000 as a float to the line
    #     updated_line = line.strip() + ', 0.0000\n'

    #     # Write the updated line to the output file
    #     file.write(updated_line)
    i=1
    j=1
    k=1
    for line in lines:
        
        # Split the line by comma and convert each entry to float
        entries = [float(entry.strip()) for entry in line.split(', ')]

        # Keep adding multiples of 0.0278 until the fourth entry reaches 30
        if entries[0] <= 7.0000:
            entries[3] = entries[3] + 0.00044643*i
            i+=1
            
        # elif entries[0] > 42300083.3333 and entries[0] <= 43200000.0000:
        #     entries[3] = 29.374812+0.00005787*k
        #     k+=1

        # Ensure that the fourth entry remains 30 until the first entry becomes 125000.0000
        elif entries[0] >= 7.0000 and entries[0]<=14.0000:
            entries[3] = 45
            #i+=1
            
        # Keep aubtracting multiples of 0.0278 until the fourth entry reaches 0
        elif entries[0] > 14.0000:
            entries[3] = 45 - 0.00044643*j
            j+=1

        # Write the updated line to the output file
        file.write(', '.join(map(str, entries)) + '\n')
