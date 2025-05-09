import gofile as go

# Define a function 'Store_Files' that takes a 'file' as input

def Store_Files(file):
    # Get the current server for file upload using 'getServer()' function from 'gofile' module
    cur_server = go.getServer()
    # Print the current server to the console
    print(cur_server)

    # Upload the file using 'uploadFile()' function from 'gofile' module
    # 'file' is the path to the file you want to upload
    url = go.uploadFile(file)

    # Print the download link to the uploaded file
    print("Download Link: ", url["downloadPage"])


# Call the 'Store_Files' function and pass the path to the file you want to upload
Store_Files("general_scripts/Cloud_file_sharing/test.txt")
