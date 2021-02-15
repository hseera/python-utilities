# -*- coding: utf-8 -*-

import pandas as pd
   
'''Rearranged column as per your liking.
Below is an example of rearranging jmeter jtl/csv file.

'''
# rearranged column here
columns =['timeStamp','label','elapsed','Latency','Connect','IdleTime','responseCode',
          'responseMessage','bytes','dataType','success',
          'failureMessage','sentBytes','URL','threadName','allThreads','grpThreads']

original_order = pd.read_csv('./sample_files/swap_001.csv')
swapped_order = original_order[columns] 
swapped_order.to_csv('./sample_files/swap_001.csv', index=False)
    