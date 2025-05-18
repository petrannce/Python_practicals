from plyer import filechooser

file_path = filechooser.open_file()
print(f"Selected file: {file_path}")

# Open a file dialog to select multiple files
files_path = filechooser.open_file(multiple=True)
print(f"Selected files: {files_path}")

# Open a file dialog to select a directory
save_path = filechooser.save_file()
print(f"File will be saved at: {save_path}")