import os

# Get the list of all files in the current directory
current_directory = os.getcwd()
files = os.listdir(current_directory)

# Loop through each file in the directory
for filename in files:
    # Check if the file ends with '.npy'
    if filename.endswith('.npy_y'):
        # Remove the '.npy' extension from the filename
        new_filename = filename[:-6]
        new_filename = new_filename + "_y.npy"
        
        # Construct full file paths for old and new filenames
        old_file_path = os.path.join(current_directory, filename)
        new_file_path = os.path.join(current_directory, new_filename)
        
        # Rename the file
        os.rename(old_file_path, new_file_path)

print("All .npy files have been renamed.")
