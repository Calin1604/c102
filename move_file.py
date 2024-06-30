import os
import shutil

from_dir = "C:/Users/calin/Downloads"
to_dir = "C:/Users/calin/OneDrive/Documents/Coding/Document_Files"

list_of_files = os.listdir(from_dir)

print("List of files in the source directory:")
print(list_of_files)

for file_name in list_of_files:
    name, extension = os.path.splitext(file_name)
    if extension == '' or extension.lower() in ['.txt', '.doc', '.docx', '.pdf']:
        path1 = os.path.join(from_dir, file_name)
        path2 = os.path.join(to_dir, "Document_Files")
        path3 = os.path.join(to_dir, "Document_Files", file_name)
        
        if os.path.exists(path2):
            print("Moving " + file_name + "...")
            shutil.move(path1, path3)
        else:
            os.makedirs(path2)
            print("Moving " + file_name + "...")
            shutil.move(path1, path3)

print("Files moved successfully!")
