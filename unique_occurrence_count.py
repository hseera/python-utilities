# -*- coding: utf-8 -*-

import pandas as pd
from collections import Counter
   
'''
Count numbers of occurance for each unique value.
'''

FILE_TO_READ = './sample_files/count.csv'
FILE_TO_WRITE = './sample_files/unique_count.csv'
        
def unique_occurance_count(FILE_TO_READ):
    df = pd.read_csv(FILE_TO_READ)
    
    unique_count =df['name'].nunique() #get count of unique value in column called 'name'
    print("Number of Unique values %s" %unique_count)
    
    data = Counter(df['name']) #Occurance of each unique value as a collection
    
    with open(FILE_TO_WRITE, 'a') as the_file:
        for key,value in data.items():
            the_file.write('%s,%s\n' %(key,value))
    
    
def main():
    unique_occurance_count(FILE_TO_READ)
    
if __name__ == "__main__":
    main()

