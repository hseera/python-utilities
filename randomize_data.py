# -*- coding: utf-8 -*-

import pandas as pd
   
'''Shuffle rows in a file. Useful when you want to have a random order data file for test.

'''
FILE = './sample_files/random.csv'

original_order = pd.read_csv(FILE)
random_order = original_order.sample(frac=1) #frac = 1 means randomize whole data set
random_order.to_csv(FILE, index=False)
