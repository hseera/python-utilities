# -*- coding: utf-8 -*-
        
import pandas as pd
import glob


'''
note glob.glob() is not case sensitive in Windows OS. 
Make sure the files that needs to be merged have unique names from other file. 
https://jdhao.github.io/2019/06/24/python_glob_case_sensitivity/
'''

FILES_TO_READ = "./sample_files/result_TestPlan_results_*.csv"
FILE_TO_WRITE = "./sample_files/merged.csv"

def merge_columns(FILES_TO_READ):
    files = glob.glob(FILES_TO_READ)
    dataframes = [pd.read_csv(p) for p in files]
    merged_dataframe = pd.concat(dataframes, axis=1)
    merged_dataframe.to_csv(FILE_TO_WRITE, index=False)

def main():
    merge_columns(FILES_TO_READ)
    
if __name__ == "__main__":
    main()