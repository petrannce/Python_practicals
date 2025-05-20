import zipfile

files = ['example1.txt', 'example2.txt']

# Create a ZipFile object
with zipfile.ZipFile('example.zip', 'w') as zipf:

    # Add files to the zip file
    for file in files:
        zipf.write(file)
        
        
print('Zip file created successfully!')