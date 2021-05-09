# -*- coding: utf-8 -*-

import pandas as pd
 
FILE_TO_WRITE = "./sample_files/full_list.csv"
 
def split_string_in_column(file_name):
    
    try:
        tools_df = pd.read_csv(file_name)
        new = tools_df['Tools Used'].str.split(", ", expand = True) #split each row in the column with ", "
        new=pd.melt(new) #combine all columns into one column
        (new['value'].dropna()).to_csv(FILE_TO_WRITE,index=False, header=['Tools'])
        
    except Exception as e:
        print(e)
       

def main():
    FILE_TO_READ = "./sample_files/Tools.csv"  # file containing column with tool names seperated by ", ". This is a demo file

    split_string_in_column(FILE_TO_READ)

if __name__ == "__main__":
    main()
