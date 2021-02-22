# -*- coding: utf-8 -*-

import pandas as pd


FILE_TO_READ = "./sample_files/dollar_number.csv" #replace with your file name

COMMA = True # add comma after every 3 digits

def conver_to_dollar(FILE_TO_READ,COMMA):
    
    df = pd.read_csv(FILE_TO_READ)
         
    if COMMA == True:
        df['amount'] = df['amount'].map('${:,}'.format) # add dollar & comma
    else:
        df['amount'] = df['amount'].map('${}'.format) # add only dollar next to the number
    
    df.to_csv(FILE_TO_READ, index=False)

        
def main():
    conver_to_dollar(FILE_TO_READ, COMMA)
    
if __name__ == "__main__":
    main()

