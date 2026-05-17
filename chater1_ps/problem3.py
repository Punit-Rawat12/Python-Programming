import os

# Use '.' to list everything in the folder where problem3.py is saved
directory_path = '/' 

# This function gets the list
contents = os.listdir(directory_path)

# This prints the list
for item in contents:
    print(item)
    
