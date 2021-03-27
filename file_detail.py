# -*- coding: utf-8 -*-
"""
Recursively list all files present in the directory with File type & permission, File Size, Owner Id, last date modified
Note: Tested on Windows OS. 
"""

import os
import datetime

OUTPUT_RESULT = open("output_result.txt", "w")

def file_detail(folder_path):
    for dirpath, dirs, files in os.walk(folder_path):	 
        path = dirpath.split('/')   
        for paths in path:
            for file in files:
                abs_path = os.path.join(dirpath, file)
                stats = os.stat(abs_path)
                OUTPUT_RESULT.write(str(file)+ "," +str(stats.st_mode)+ "," +str(stats.st_uid)+ "," +str(stats.st_size)+","+str(datetime.datetime.fromtimestamp(os.path.getmtime(abs_path)))+"\n") 

#def file_detail(folder_path):
#    folder_abs_path=os.path.abspath(folder_path)
#    for file in os.listdir(folder_abs_path):
#        #print(file)
#        path = os.path.join(folder_abs_path, file)
#        print(path)
#        current_path = folder_abs_path
#        print(current_path)
#        if os.path.isfile(file):
#            stats = os.stat(file)
#            OUTPUT_RESULT.write(str(file)+ "," +str(stats.st_mode)+ "," +str(stats.st_uid)+ "," +str(stats.st_size)+","+str(datetime.datetime.fromtimestamp(os.path.getmtime(file)))+"\n")
#        if os.path.isdir(file):
#            os.chdir(path)
#            file_detail(path)
#            os.chdir(current_path)

def main():
    folder_path = "C:\\working-folder"  # Sample folder path. Change this to your folder path.
    OUTPUT_RESULT.write("FileName,FileMode,OwnerId,FileSize,LastModified\n")   
    file_detail(folder_path)
    OUTPUT_RESULT.close()

if __name__ == "__main__":
    main()