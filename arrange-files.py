# -*- coding: utf-8 -*-
"""
This script iterates through all the JMeter files and arranges them in an appropriate folder.
It will create folders if they don't exist.
"""

import os
import shutil

def search_file(folder_path):
    os.chdir(folder_path)
    files = os.listdir(os.getcwd())
    for filename in files:
        if not os.path.isdir(filename):
            print(filename)               
            if filename.endswith('.jmx'): #jmeter scenario files
               if not os.path.exists('Scripts'):
                   os.mkdir('Scripts')
               shutil.move(filename, 'Scripts')
            elif filename.endswith('.jtl'): #jmeter result files
               if not os.path.exists('Result'):
                  os.mkdir('Result')
               shutil.move(filename, 'Result')
            elif filename.endswith(('.csv','.xls')): #jmeter data files
               if not os.path.exists('Data'):
                   os.mkdir('Data')
               shutil.move(filename, 'Data')
            elif filename.endswith('.zip'): #any zip files
               if not os.path.exists('Zip_files'):
                   os.mkdir('Zip_files')
               shutil.move(filename, 'Zip_files')
            else:
               continue # all other files, do nothing

def main():

    FOLDER_PATH = "C:\\userxxx\\jmeter"  #Change the folder path against which you want to run the script.
    search_file(FOLDER_PATH)

if __name__ == "__main__":
    main()
