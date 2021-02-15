# -*- coding: utf-8 -*-

import pandas as pd
   
'''Shuffle rows in a file. Useful when you want to have a random order data file for test.

'''
FILE_TO_READ = './sample_files/random.csv'


def randomize(FILE_TO_READ):
    original_order = pd.read_csv(FILE_TO_READ)
    random_order = original_order.sample(frac=1) #frac = 1 means randomize whole data set
    random_order.to_csv(FILE_TO_READ, index=False)

def main():
    randomize(FILE_TO_READ)
    
if __name__ == "__main__":
    main()