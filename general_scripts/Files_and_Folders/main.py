import os

PATH = os.path.dirname(os.path.abspath(__file__))

files, dirs = 0, 0

for root, dirnames, filenames in os.walk(PATH):
    print('Looking in:', root)
    dirs += len(dirnames)
    files += len(filenames)

print(f'Total files: {files}')
print(f'Total directories: {dir}')
print('Total files and directories: ', files + dirs)
