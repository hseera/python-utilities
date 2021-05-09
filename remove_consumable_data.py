# -*- coding: utf-8 -*-

import pandas as pd
 
def remove_consumed_data(original_data_set, consumed_data_set):
    try:
        consumed_df = pd.read_csv(consumed_data_set, header=None)
        original_df = pd.read_csv(original_data_set, header=None)
        original_df = pd.concat([consumed_df, original_df]).drop_duplicates(keep=False)
        original_df.to_csv(original_data_set, index=False, header=None)
    except Exception as e:
        print(e)

def main():
    
    CONSUMED_DATA_SET = "./sample_files/consumed_data_set.csv" #data file containing data that has been used/consumed.
    ORIGINAL_DATA_SET = "./sample_files/original_data_set.csv" #original data file with all the data
    
    remove_consumed_data(ORIGINAL_DATA_SET, CONSUMED_DATA_SET)

if __name__ == "__main__":
    main()
