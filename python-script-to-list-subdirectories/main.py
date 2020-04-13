from sys import argv
from os import listdir
from os.path import isfile, join

folder_name = argv
print(folder_name[1])

# Fetches sub directories, and file
print(listdir(folder_name[1]))

# Only files
onlyfiles = [f for f in listdir(folder_name[1]) if isfile(join(folder_name[1], f))]

print(onlyfiles)