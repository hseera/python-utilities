# -*- coding: utf-8 -*-
"""
Recursively search for a file in a folder and all it's subfolders.
Print out the locations where that file is located.

Note: Tested on Windows. The seperate value in split function will need to change based on different OS. 
"""

import os

def search_file(folder_path, file_name):
    for dirpath, dirs, files in os.walk(folder_path):	 
        path = dirpath.split('/')   
        base_folder_path = folder_path.split("\\")
        for paths in path:
            sub_folders=paths.split("\\")
            print ('|', (len(sub_folders)-len(base_folder_path))*'-', '[',os.path.basename(dirpath),']') #print folders
            for f in files:
                if f.find(file_name) != -1: #if file in a folder matches the file to locate, print it
                    print ('|', (len(sub_folders)-len(base_folder_path)+1)*'-', f)

def main():
    folder_path = "."  # Default path is where this script is located.
    file_name = "locate_file" #Default filename to locate is this python script
    search_file(folder_path,file_name)

if __name__ == "__main__":
    main()