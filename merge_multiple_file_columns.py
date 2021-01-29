# -*- coding: utf-8 -*-
        
import pandas as pd
import glob


'''
note glob.glob() is not case sensitive in Windows OS. 
Make sure the files that needs to be merged have unique names from other file. 
https://jdhao.github.io/2019/06/24/python_glob_case_sensitivity/
'''
files = glob.glob("./sample_files/result_TestPlan_results_*.csv")

dataframes = [pd.read_csv(p) for p in files]

merged_dataframe = pd.concat(dataframes, axis=1)
merged_dataframe.to_csv("./sample_files/merged.csv", index=False)

