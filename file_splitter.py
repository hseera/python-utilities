# -*- coding: utf-8 -*-
"""
This script splits a file into multiple small files decided by the number 
defined in the variable "no_of_files_to_generate".

Useful for tools like JMeter where a big file needs to be split and exported across multiple 
slaves that will run same script but with different data set.

Note: Currently the script assumes there is no header in the main file. 
If there is then update the header values (header=None & header=False) in the script accordingly.

"""

import pandas as pd
from pandas.io.common import EmptyDataError

def split_file(no_of_files_to_generate,file_path, file_to_split):
    try:
        no_of_rows = 0
        remainder = 0
        start = 0 # Initial Lower Limit
        df = pd.read_csv(file_path + file_to_split, header=None) # reading file.  
        numline = len(df.index)
        no_of_rows, remainder = divmod(numline, no_of_files_to_generate)
        end = no_of_rows # Initial Higher Limit
        
        file_generator_counter = 1
        
        file_to_split = file_to_split.replace(".csv","")
        
        if numline <= no_of_files_to_generate: #if number of rows in the file is less than number of files to generate  
            df_new = df[start:numline]
            df_new.to_csv("%s%s_%s.csv" %(file_path, file_to_split,file_generator_counter),header=False, index=False)
        else:
            while start < numline:
                df_new = df[start:end]
                if file_generator_counter <= no_of_files_to_generate and remainder == 0:
                    start = end
                    end = end + no_of_rows
                elif file_generator_counter < no_of_files_to_generate and remainder != 0:
                    start = end
                    end = end + no_of_rows
                elif file_generator_counter == no_of_files_to_generate and remainder != 0 :
                    end = numline
                    df_new = df[start:end]
                    start = end
                df_new.to_csv("%s%s_%s.csv" %(file_path, file_to_split,file_generator_counter),header=False, index=False)
                file_generator_counter = file_generator_counter + 1 
        
    except EmptyDataError:
        print("Empty File nothing to split")


def main():
    file_path = "./sample_files/"  # file path
    file_to_split = "file_split.csv" # filename
    No_of_files_to_generate = 3 # define how many files to generate
    split_file(No_of_files_to_generate,file_path, file_to_split)

if __name__ == "__main__":
    main()
