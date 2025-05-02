from zipfile import ZipFile

with ZipFile('example.zip', 'r') as zObject:

    # Extract all the contents of zip file in current directory
    zObject.extractall()
    print('All files extracted successfully!')

    # Extract a specific file from the zip file
    zObject.extract('example.txt', 'extracted_files/')
    print('example.txt extracted successfully!')
    
    # List all the contents of the zip file
    print(zObject.namelist())