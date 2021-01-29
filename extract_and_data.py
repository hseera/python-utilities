# -*- coding: utf-8 -*-

import pandas as pd
import os

location = os.getcwd()

FILE_TO_WRITE =""       
for file in os.listdir(location):
    try:
        if file.startswith("TestPlan_") and file.endswith(".csv"):
            FILE_TO_WRITE = "result_"+os.path.basename(file)
            df = pd.read_csv(file)
            x = []
            x = df.loc[df['label'] == 'GetDistribution'] #filter out all the rows for which the label column does not contain value GetDistribution
            with open(FILE_TO_WRITE,'w') as fwrite:
                fwrite.write('elapsed_time_'+FILE_TO_WRITE+'\n')
                for item in range(len(x)):
                   fwrite.write('%s\n' %x['elapsed'].values[item])
    except Exception as e:
        raise e
                
            