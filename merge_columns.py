# -*- coding: utf-8 -*-

import pandas as pd

def melt_columns(file_to_read):
    df = pd.read_csv(file_to_read) # read the file
    df = pd.melt(df,var_name='locations', value_name='response_time') # name for the new columns
    write_to_file(df)

def write_to_file(dataframe):
    dataframe.to_csv('./sample_files/merged_columns.csv', index=False, header=True)
    
def main():
    FILE_TO_READ = './sample_files/pivoted_columns.csv' #replace with your file name
    
    melt_columns(FILE_TO_READ)
    
if __name__ == "__main__":
    main()
    

