import os

filename = "Names.txt"  

if os.path.exists(filename) and os.access(filename, os.R_OK):

    file_info = os.stat(filename)
    

    print(f"File Size: {file_info.st_size} bytes")
    

    print(f"Last Modified: {file_info.st_mtime}")
    

    with open(filename, mode="r") as textFile:
        contents = textFile.read()
        print(contents)
else:
    print(f"The file '{filename}' does not exist or is not readable.")
