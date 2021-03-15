# -*- coding: utf-8 -*-

import pandas as pd

#RESULT_FILE ='./sample_files/result.csv' <-uncomment it if you want to save stats to a file

def generate_pivot_table(FILE_TO_READ, TRANSPOSE):
    try:
        df = pd.read_csv(FILE_TO_READ)
        
        if (TRANSPOSE == True):
            df = df.describe(percentiles=[0.25,0.5,0.75,0.90,0.95],include='all').transpose() #show basic statistics in column
        else:
            df = df.describe(percentiles=[0.25,0.5,0.75,0.90,0.95],include='all') # show basic statistics as in row
        
        print(df)
        
        #df.to_csv(RESULT_FILE,index=False)   <- uncomment if you want to output the statistics to a file
        
    except Exception as e:
        raise e
            
def main():
    FILE_TO_READ = "./sample_files/basic_statistics.csv" #data file. Replace with your data file.
    TRANSPOSE = False
    generate_pivot_table(FILE_TO_READ, TRANSPOSE)

if __name__ == "__main__":
    main()
