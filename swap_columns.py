# -*- coding: utf-8 -*-

import pandas as pd
   
'''Rearranged column as per your liking.
Below is an example of rearranging jmeter jtl/csv file.

'''
# rearrange column here
columns =['timeStamp','label','elapsed','Latency','IdleTime','Connect','responseCode',
          'responseMessage','dataType','success','failureMessage',
          'bytes','sentBytes','grpThreads','allThreads','URL','threadName']

df = pd.read_csv('./sample_files/swap_001.csv')
df_reordered = df[columns] 
df_reordered.to_csv('./sample_files/swap_001.csv', index=False)
    