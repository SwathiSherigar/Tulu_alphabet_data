import os
import zipfile

def zip_files_in_order(folder_path, zip_file_path):
    # Get list of files in the folder and sort them numerically
    files = os.listdir(folder_path)
    files.sort(key=lambda x: int(os.path.splitext(x)[0]))  # Adjust this if your file names have different patterns
    
    # Create a Zip file and add files in the sorted order
    with zipfile.ZipFile(zip_file_path, 'w') as zipf:
        for file in files:
            file_path = os.path.join(folder_path, file)
            zipf.write(file_path, arcname=file)

# Example usage
folder_path = 'a_tulu_data'  # Path to the folder containing files to be zipped
zip_file_path = 'tulu_alphabet1.zip'  # Path to the output zip file

zip_files_in_order(folder_path, zip_file_path)
