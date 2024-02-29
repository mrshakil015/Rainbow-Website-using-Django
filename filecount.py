import os

def list_files_in_folder(folder_path):
    for root, _, files in os.walk(folder_path):
        for file_name in files:
            print(file_name)

folder_path = 'static/images'
list_files_in_folder(folder_path)
