# -*- coding: utf-8 -*-

import pandas as pd
   
'''Rearranged column as per your liking.
Below is an example of rearranging jmeter jtl/csv file.

'''
# rearranged column here
COLUMNS =['timeStamp','label','elapsed','Latency','Connect','IdleTime','responseCode',
          'responseMessage','bytes','dataType','success',
          'failureMessage','sentBytes','URL','threadName','allThreads','grpThreads']

FILE_TO_READ = './sample_files/swap_001.csv'

def swap_columns(FILE_TO_READ):
    original_order = pd.read_csv(FILE_TO_READ)
    swapped_order = original_order[COLUMNS] 
    swapped_order.to_csv(FILE_TO_READ, index=False)
    

def main():
    swap_columns(FILE_TO_READ)
    
if __name__ == "__main__":
    main()