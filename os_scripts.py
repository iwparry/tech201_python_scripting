import os

# 1. Create a directory

# Ditrectory
directory = "test_dir"

# Parent Directory
parent_dir = "C:/Users/iwpar"

# Path
path = os.path.join(parent_dir, directory)

# Create the Directory
# os.mkdir(path)
# print("Directory '% s' created" % directory)

# 2. Make a File in the New Directory

filename = "testfile.txt"
filepath = os.path.join(path, filename)

# Write to the new File
with open(os.path.join(path, filename), "w") as file1:
    toFile = "Contents of my new file"
    file1.write(toFile)
print("File " + filename + " created in " + directory + " folder")