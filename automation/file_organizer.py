import os
import shutil

def organize_files(folder_path):
    for filename in os.listdir(folder_path):
        if os.path.isfile(os.path.join(folder_path, filename)):
            ext = filename.split('.')[-1].lower()
            ext_folder = os.path.join(folder_path, ext + "_files")
            os.makedirs(ext_folder, exist_ok=True)
            shutil.move(os.path.join(folder_path, filename), os.path.join(ext_folder, filename))
