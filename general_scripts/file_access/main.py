import os

PATH = r'C:\Coding\Projects'

files, dirs =0, 0

for root, dirnames, filenames in os.walk(PATH):
    print('looking in: ', root)
    dirs += len(dirnames)
    files += len(filenames)

print('Files:', dirs)
print('Directories:', dirs)
print('Total:', files + dirs)