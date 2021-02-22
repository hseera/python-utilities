# -*- coding: utf-8 -*-

import pandas as pd

FILE_TO_WRITE = "./sample_files/pivot.csv" #save pivot table data to pivot.csv

def generate_pivot_table(FILE_TO_READ):
    try:
        df = pd.read_csv(FILE_TO_READ)
        
        df['Date'] = df._time.apply(lambda x: x[:10]) #For each row in _time column, extract the date value
        df['Time'] = df._time.apply(lambda x: x[11:19]) #For each row in _time column, extract the time value
        
        pivot = df.pivot(index='Date', columns='Time', values='Count')
        pivot.to_csv(FILE_TO_WRITE, index=True)
        #print(pivot)
    except Exception as e:
        raise e
            
def main():
    FILE_TO_READ = "./sample_files/pivot_data.csv" #data file
    generate_pivot_table(FILE_TO_READ)

if __name__ == "__main__":
    main()
