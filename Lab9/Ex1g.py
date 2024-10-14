filename = "Names.txt"  # The name of your file

# Step 1: Append the new name to the file
with open(filename, mode="a") as textFile:
    textFile.write("Port, Dan\n")  # Add the new name with a newline

# Step 2: Read and print the entire contents of the file
with open(filename, mode="r") as textFile:
    contents = textFile.read()
    print(contents)
