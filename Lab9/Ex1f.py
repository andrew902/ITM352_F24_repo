import os

filename = "Names.txt" 


if os.path.exists(filename) and os.access(filename, os.R_OK):
    with open(filename, mode="r") as textFile:
        line = textFile.readline()
        count = 0

        while line:
            print(line.strip())  
            count += 1
            line = textFile.readline()

    print(f"There are {count} names in the file.")
else:
    print(f"The file '{filename}' does not exist or is not readable.")
